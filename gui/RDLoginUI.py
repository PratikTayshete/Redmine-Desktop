# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RDLoginUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RDLogin(object):
    def setupUi(self, RDLogin):
        if not RDLogin.objectName():
            RDLogin.setObjectName(u"RDLogin")
        RDLogin.resize(1000, 600)
        RDLogin.setMinimumSize(QSize(1000, 600))
        RDLogin.setMaximumSize(QSize(1000, 600))
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        RDLogin.setFont(font)
        RDLogin.setStyleSheet(u"background-color: rgb(37, 37, 37);")
        self.centralwidget = QWidget(RDLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AppTitleFrame = QFrame(self.centralwidget)
        self.AppTitleFrame.setObjectName(u"AppTitleFrame")
        self.AppTitleFrame.setMinimumSize(QSize(0, 100))
        self.AppTitleFrame.setMaximumSize(QSize(16777215, 100))
        self.AppTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.AppTitleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.AppTitleFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(247, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.title1_frame = QFrame(self.AppTitleFrame)
        self.title1_frame.setObjectName(u"title1_frame")
        self.title1_frame.setFrameShape(QFrame.StyledPanel)
        self.title1_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.title1_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title1_label = QLabel(self.title1_frame)
        self.title1_label.setObjectName(u"title1_label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(35)
        self.title1_label.setFont(font1)
        self.title1_label.setStyleSheet(u"color: rgb(183, 28, 28);")

        self.gridLayout.addWidget(self.title1_label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.title1_frame, 0, 1, 1, 1)

        self.title2_frame = QFrame(self.AppTitleFrame)
        self.title2_frame.setObjectName(u"title2_frame")
        self.title2_frame.setFrameShape(QFrame.StyledPanel)
        self.title2_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.title2_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title2_label = QLabel(self.title2_frame)
        self.title2_label.setObjectName(u"title2_label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(35)
        self.title2_label.setFont(font2)
        self.title2_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.title2_label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.title2_frame, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(246, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.AppTitleFrame, 0, 0, 1, 1)

        self.LoginFrame = QFrame(self.centralwidget)
        self.LoginFrame.setObjectName(u"LoginFrame")
        self.LoginFrame.setFrameShape(QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.LoginFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame = QFrame(self.LoginFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 371))
        self.frame.setMaximumSize(QSize(300, 371))
        self.frame.setStyleSheet(u"QFrame {\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"	border-radius: 25px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(12, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.usernameLoginLinedit = QLineEdit(self.frame)
        self.usernameLoginLinedit.setObjectName(u"usernameLoginLinedit")
        self.usernameLoginLinedit.setMinimumSize(QSize(0, 41))
        self.usernameLoginLinedit.setMaximumSize(QSize(16777215, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(12)
        self.usernameLoginLinedit.setFont(font3)
        self.usernameLoginLinedit.setStyleSheet(u"QLineEdit {\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"	border-style: inset;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_9.addWidget(self.usernameLoginLinedit, 1, 1, 1, 3)

        self.horizontalSpacer_8 = QSpacerItem(12, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(12, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 3, 0, 1, 1)

        self.passwordLoginLinedit = QLineEdit(self.frame)
        self.passwordLoginLinedit.setObjectName(u"passwordLoginLinedit")
        self.passwordLoginLinedit.setMinimumSize(QSize(0, 41))
        self.passwordLoginLinedit.setMaximumSize(QSize(16777215, 41))
        self.passwordLoginLinedit.setFont(font3)
        self.passwordLoginLinedit.setStyleSheet(u"QLineEdit {\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"	border-style: inset;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.passwordLoginLinedit.setEchoMode(QLineEdit.Password)

        self.gridLayout_9.addWidget(self.passwordLoginLinedit, 3, 1, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(12, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 3, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 5, 1, 1, 1)

        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(151, 41))
        self.loginButton.setMaximumSize(QSize(151, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        self.loginButton.setFont(font4)
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(66, 66, 66);\n"
"	border-radius: 20px;\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"	color: rgb(255, 255, 255);\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);\n"
"	border-style: inset;\n"
"}")

        self.gridLayout_9.addWidget(self.loginButton, 5, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(36, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 5, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 6, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.LoginFrame, 1, 0, 1, 1)

        RDLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(RDLogin)

        QMetaObject.connectSlotsByName(RDLogin)
    # setupUi

    def retranslateUi(self, RDLogin):
        RDLogin.setWindowTitle(QCoreApplication.translate("RDLogin", u"Redmine Desktop V0.1", None))
        self.title1_label.setText(QCoreApplication.translate("RDLogin", u"REDMINE", None))
        self.title2_label.setText(QCoreApplication.translate("RDLogin", u"DESKTOP", None))
        self.usernameLoginLinedit.setPlaceholderText(QCoreApplication.translate("RDLogin", u"Username", None))
        self.passwordLoginLinedit.setPlaceholderText(QCoreApplication.translate("RDLogin", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("RDLogin", u"Login", None))
    # retranslateUi

