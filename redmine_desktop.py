from PySide2.QtWidgets import QMainWindow, QApplication
from gui.RDAppUI import Ui_RDApp
from libs.redmine import RedMineManager
from utils import operations


class RedmineDesktop(QMainWindow, Ui_RDApp):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_RDApp.__init__(self)
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
        self.refreshButton.clicked.connect(self.load_data)

    def login(self):
        """
        Validates the user and logs in.
        """
        username = str(self.usernameLoginLinedit.text())
        password = str(self.passwordLoginLinedit.text())
        self.redmine_manager = RedMineManager(username=username, password=password)
        self.is_user_valid = self.redmine_manager.validate_login()
        if self.is_user_valid:
            self.usernameLoginLinedit.clear()
            self.passwordLoginLinedit.clear()
            print("[INFO]User [{}] successfully logged in.".format(username))
            self.rdStackWidget.setCurrentIndex(1)
            self.load_data()
        else:
            print("[INFO] Invalid login.")
            operations.display_message("Invalid Login", "Please check the login credentials.")

    def load_data(self):
        """
        Loads the data in the application.
        """
        self.load_total_projects()
        self.load_total_issues()
        self.load_total_issues_resolved()
        self.load_total_pending_issues()

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
