from PySide2.QtWidgets import QMainWindow, QApplication
from gui.RDLoginUI import Ui_RDLogin
from libs.redmine import RedMineManager


class RedmineDesktop(QMainWindow, Ui_RDLogin):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_RDLogin.__init__(self)
        self.setupUi(self)
        self.redmine_user = None
        self.connect_interface()

    def connect_interface(self):
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = str(self.usernameLoginLinedit.text())
        password = str(self.passwordLoginLinedit.text())
        self.redmine_user = RedMineManager(username=username, password=password)
        print(self.redmine_user.get_projects())


if __name__ == '__main__':
    app = QApplication()
    rd_window = RedmineDesktop()
    rd_window.show()
    app.exec_()