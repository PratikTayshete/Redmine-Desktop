from PySide2.QtWidgets import QMainWindow, QApplication
from gui.RDLoginUI import Ui_RDLogin
from libs.redmine import RedMineManager
from modules.ui import RedmineDesktopMain


class RedmineDesktop(QMainWindow, Ui_RDLogin):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_RDLogin.__init__(self)
        self.setupUi(self)
        self.redmine_manager = None
        self.is_user_valid = None
        self.main_rd_app = None
        self.connect_interface()

    def connect_interface(self):
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = str(self.usernameLoginLinedit.text())
        password = str(self.passwordLoginLinedit.text())
        self.redmine_manager = RedMineManager(username=username, password=password)
        self.is_user_valid = self.redmine_manager.validate_login()
        if self.is_user_valid:
            print("[INFO]User [{}] successfully logged in.".format(username))
            self.close()
            self.main_rd_app = RedmineDesktopMain(redmine_manager=self.redmine_manager)
            self.main_rd_app.launch()

        else:
            print("[INFO] Invalid login.")


if __name__ == '__main__':
    app = QApplication()
    rd_window = RedmineDesktop()
    rd_window.show()
    app.exec_()
