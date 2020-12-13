from PySide2.QtWidgets import QMainWindow, QApplication, QDialog
from PySide2.QtCore import Qt
from gui.RDAppUI import Ui_RDApp
from gui.IssueDialogUI import Ui_CreateIssue
from libs.redmine import RedMineManager
from utils import operations, constants


class RedmineDesktop(QMainWindow, Ui_RDApp):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_RDApp.__init__(self)
        self.create_issue_dialog_ui = Ui_CreateIssue()
        self.setupUi(self)
        self.redmine_manager = None
        self.is_user_valid = None
        self.rdStackWidget.setCurrentIndex(0)
        self.connect_interface()

    def connect_interface(self):
        """
        Connects actions performed on widgets to its functionalities.
        """
        self.loginButton.clicked.connect(self.login)
        self.logoutButton.clicked.connect(self.logout)
        self.refreshButton.clicked.connect(self.refresh_data)
        self.createIssueButton.clicked.connect(self.create_issue)

    def login(self):
        """
        Validates the user and logs in.
        """
        print("[INFO] Loading data........")
        username = str(self.usernameLoginLinedit.text())
        password = str(self.passwordLoginLinedit.text())
        self.redmine_manager = RedMineManager(username=username, password=password)
        self.is_user_valid = self.redmine_manager.validate_login()
        if self.is_user_valid:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.usernameLoginLinedit.clear()
            self.passwordLoginLinedit.clear()
            print("[INFO]User [{}] successfully logged in.".format(username))
            self.rdStackWidget.setCurrentIndex(1)
            self.refresh_data()
            QApplication.restoreOverrideCursor()
        else:
            print("[INFO] Invalid login.")
            operations.display_message("Invalid Login", "Please check the login credentials.")

    def refresh_data(self):
        """
        Loads the latest data in the application.
        """
        operations.clear_issues_table(self.issuesTableWidget)
        self.load_total_projects()
        self.load_total_issues()
        self.load_total_issues_resolved()
        self.load_total_pending_issues()
        self.load_issues_table()

    def load_total_pending_issues(self):
        """
        Display total pending issues.
        """
        total_issues_pending = self.redmine_manager.total_issues_pending_count()
        self.totalPendingCountLabel.setText(total_issues_pending)

    def load_total_issues_resolved(self):
        """
        Display total issues resolved.
        """
        total_issues_resolved = self.redmine_manager.total_issues_resolved_count()
        self.totalResolvedCountLabel.setText(total_issues_resolved)

    def load_total_issues(self):
        """
        Display total issues.
        """
        total_issues = self.redmine_manager.total_issues_count()
        self.totalIssuesCountLabel.setText(total_issues)

    def load_total_projects(self):
        """
        Display total projects.
        """
        total_projects = self.redmine_manager.total_projects_count()
        self.totalProjectsCountLabel.setText(total_projects)

    def create_issue(self):
        """
        Opens a QDialog to create new Issue.
        """
        # Load the QDialog to create new issue.
        issue_dialog = QDialog()
        issue_dialog.setWindowFlags(Qt.WindowTitleHint)
        issue_dialog.setWindowFlags(Qt.WindowSystemMenuHint)
        issue_dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        self.create_issue_dialog_ui.setupUi(issue_dialog)
        # Add the list of current projects from redmine.
        projects_list = self.redmine_manager.get_projects()
        self.create_issue_dialog_ui.projectComboBox.addItems(projects_list)
        # Add the trackers of the selected project.
        self.create_issue_dialog_ui.projectComboBox.currentIndexChanged.connect(self.add_project_trackers)
        # Add priorities for the new issue.
        priorities_list = [priority_name for priority_name in constants.PRIORITIES_DICT]
        self.create_issue_dialog_ui.priorityComboBox.addItems(priorities_list)
        # Detect clicked signal for the create button.
        self.create_issue_dialog_ui.newIssueButton.clicked.connect(self.create_new_issue_clicked)
        issue_dialog.exec_()

    def create_new_issue_clicked(self):
        """
        Performs the operation that creates a new issue in redmine.
        """
        project_name = self.create_issue_dialog_ui.projectComboBox.currentText()
        tracker = self.create_issue_dialog_ui.trackerComboBox.currentText()
        subject = self.create_issue_dialog_ui.subjectLineEdit.text()
        description = self.create_issue_dialog_ui.descriptionTextEdit.toPlainText()
        priority_name = self.create_issue_dialog_ui.priorityComboBox.currentText()
        priority_id = constants.PRIORITIES_DICT[priority_name]
        if project_name and tracker and subject and description and priority_name:
            try:
                self.redmine_manager.create_new_issue(project_name, tracker, subject, description, priority_id)
                print("[INFO] New issue created successfully.")
                operations.display_message("Create Issue", "Issue created successfully.")
            except Exception as error:
                print(error)
                print("[INFO] Unable to create new issue.")
        else:
            operations.display_message("Create Issue Error", "Please fill all the fields before creating the issue.")

    def add_project_trackers(self):
        self.create_issue_dialog_ui.trackerComboBox.clear()
        project_name = self.create_issue_dialog_ui.projectComboBox.currentText()
        project_trackers_list = self.redmine_manager.get_project_trackers(project_name)
        self.create_issue_dialog_ui.trackerComboBox.addItems(project_trackers_list)

    def load_issues_table(self):
        """
        Display the issues created by the user.
        """
        issues_dict = self.redmine_manager.get_issues()
        operations.load_issues_table_data(table_widget=self.issuesTableWidget, issues_dict=issues_dict)

    def logout(self):
        """
        Logs out the user from the application.
        """
        self.redmine_manager.clear_data_on_logout()
        self.redmine_manager = None
        self.is_user_valid = None
        self.rdStackWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication()
    rd_window = RedmineDesktop()
    rd_window.show()
    app.exec_()
