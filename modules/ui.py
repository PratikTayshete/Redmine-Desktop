from PySide2.QtWidgets import QMainWindow, QApplication
from gui.RDMainUI import Ui_RDMain


class RedmineDesktopMain(QMainWindow, Ui_RDMain):
    def __init__(self, redmine_manager):
        QMainWindow.__init__(self)
        Ui_RDMain.__init__(self)
        self.setupUi(self)
        self.redmine_manager = redmine_manager

    def launch(self):
        self.showMaximized()
