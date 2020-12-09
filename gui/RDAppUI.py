# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RDAppUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RDApp(object):
    def setupUi(self, RDApp):
        if not RDApp.objectName():
            RDApp.setObjectName(u"RDApp")
        RDApp.resize(1124, 826)
        RDApp.setMinimumSize(QSize(1124, 826))
        RDApp.setMaximumSize(QSize(1124, 826))
        font = QFont()
        font.setFamily(u"Segoe UI")
        RDApp.setFont(font)
        RDApp.setStyleSheet(u"background-color: rgb(37, 37, 37);")
        self.centralwidget = QWidget(RDApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QHeaderView::section {\n"
"	\n"
"	background-color: rgb(66, 66, 66);\n"
"	\n"
"	color: rgb(252, 162, 68);\n"
"	border-style: inset;\n"
"}\n"
"QTableWidget {\n"
"	\n"
"	background-color: rgb(66, 66, 66);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rdStackWidget = QStackedWidget(self.centralwidget)
        self.rdStackWidget.setObjectName(u"rdStackWidget")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.gridLayout_6 = QGridLayout(self.loginPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AppTitleFrame = QFrame(self.loginPage)
        self.AppTitleFrame.setObjectName(u"AppTitleFrame")
        self.AppTitleFrame.setMinimumSize(QSize(0, 100))
        self.AppTitleFrame.setMaximumSize(QSize(16777215, 100))
        self.AppTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.AppTitleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.AppTitleFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.title1_frame = QFrame(self.AppTitleFrame)
        self.title1_frame.setObjectName(u"title1_frame")
        self.title1_frame.setFrameShape(QFrame.StyledPanel)
        self.title1_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.title1_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title1_label = QLabel(self.title1_frame)
        self.title1_label.setObjectName(u"title1_label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(35)
        self.title1_label.setFont(font1)
        self.title1_label.setStyleSheet(u"color: rgb(183, 28, 28);")

        self.gridLayout_2.addWidget(self.title1_label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.title1_frame, 0, 1, 1, 1)

        self.title2_frame = QFrame(self.AppTitleFrame)
        self.title2_frame.setObjectName(u"title2_frame")
        self.title2_frame.setFrameShape(QFrame.StyledPanel)
        self.title2_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.title2_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.title2_label = QLabel(self.title2_frame)
        self.title2_label.setObjectName(u"title2_label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(35)
        self.title2_label.setFont(font2)
        self.title2_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.title2_label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.title2_frame, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(297, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.AppTitleFrame, 0, 0, 1, 1)

        self.LoginFrame = QFrame(self.loginPage)
        self.LoginFrame.setObjectName(u"LoginFrame")
        self.LoginFrame.setFrameShape(QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.LoginFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(368, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame = QFrame(self.LoginFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 371))
        self.frame.setMaximumSize(QSize(300, 371))
        self.frame.setStyleSheet(u"QFrame {\n"
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

        self.horizontalSpacer_4 = QSpacerItem(368, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.LoginFrame, 1, 0, 1, 1)

        self.rdStackWidget.addWidget(self.loginPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.gridLayout_22 = QGridLayout(self.mainPage)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.infoFrame = QFrame(self.mainPage)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setMinimumSize(QSize(0, 250))
        self.infoFrame.setMaximumSize(QSize(16777215, 250))
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.infoFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_7 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 0, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 0, 5, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_10, 0, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.totalIssuesFrame = QFrame(self.infoFrame)
        self.totalIssuesFrame.setObjectName(u"totalIssuesFrame")
        self.totalIssuesFrame.setMinimumSize(QSize(141, 181))
        self.totalIssuesFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalIssuesFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.totalIssuesFrame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.totalIssuesCountFrame = QFrame(self.totalIssuesFrame)
        self.totalIssuesCountFrame.setObjectName(u"totalIssuesCountFrame")
        self.totalIssuesCountFrame.setMinimumSize(QSize(120, 111))
        self.totalIssuesCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.totalIssuesCountFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.totalIssuesCountLabel = QLabel(self.totalIssuesCountFrame)
        self.totalIssuesCountLabel.setObjectName(u"totalIssuesCountLabel")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Light")
        font5.setPointSize(50)
        self.totalIssuesCountLabel.setFont(font5)
        self.totalIssuesCountLabel.setStyleSheet(u"color: rgb(239, 83, 80);")
        self.totalIssuesCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.totalIssuesCountLabel, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.totalIssuesCountFrame, 0, 0, 1, 1)

        self.totalIssuesTextFrame = QFrame(self.totalIssuesFrame)
        self.totalIssuesTextFrame.setObjectName(u"totalIssuesTextFrame")
        self.totalIssuesTextFrame.setMinimumSize(QSize(101, 31))
        self.totalIssuesTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.totalIssuesTextFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.totalIssuesTextLabel = QLabel(self.totalIssuesTextFrame)
        self.totalIssuesTextLabel.setObjectName(u"totalIssuesTextLabel")
        font6 = QFont()
        font6.setFamily(u"Segoe UI Light")
        font6.setPointSize(10)
        self.totalIssuesTextLabel.setFont(font6)
        self.totalIssuesTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalIssuesTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.totalIssuesTextLabel, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.totalIssuesTextFrame, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.totalIssuesFrame, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.totalProjectsFrame = QFrame(self.infoFrame)
        self.totalProjectsFrame.setObjectName(u"totalProjectsFrame")
        self.totalProjectsFrame.setMinimumSize(QSize(141, 181))
        self.totalProjectsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalProjectsFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.totalProjectsFrame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.totalProjectsCountFrame = QFrame(self.totalProjectsFrame)
        self.totalProjectsCountFrame.setObjectName(u"totalProjectsCountFrame")
        self.totalProjectsCountFrame.setMinimumSize(QSize(120, 111))
        self.totalProjectsCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.totalProjectsCountFrame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.totalProjectsCountLabel = QLabel(self.totalProjectsCountFrame)
        self.totalProjectsCountLabel.setObjectName(u"totalProjectsCountLabel")
        self.totalProjectsCountLabel.setFont(font5)
        self.totalProjectsCountLabel.setStyleSheet(u"color: rgb(236, 64, 122);")
        self.totalProjectsCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.totalProjectsCountLabel, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.totalProjectsCountFrame, 0, 0, 1, 1)

        self.totalProjectsTextFrame = QFrame(self.totalProjectsFrame)
        self.totalProjectsTextFrame.setObjectName(u"totalProjectsTextFrame")
        self.totalProjectsTextFrame.setMinimumSize(QSize(101, 31))
        self.totalProjectsTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsTextFrame.setFrameShadow(QFrame.Raised)
        self.totalProjectsTextLabel = QLabel(self.totalProjectsTextFrame)
        self.totalProjectsTextLabel.setObjectName(u"totalProjectsTextLabel")
        self.totalProjectsTextLabel.setGeometry(QRect(30, 10, 55, 16))
        self.totalProjectsTextLabel.setFont(font6)
        self.totalProjectsTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalProjectsTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.totalProjectsTextFrame, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.totalProjectsFrame, 1, 3, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_13, 1, 4, 1, 1)

        self.totalResolvedFrame = QFrame(self.infoFrame)
        self.totalResolvedFrame.setObjectName(u"totalResolvedFrame")
        self.totalResolvedFrame.setMinimumSize(QSize(141, 181))
        self.totalResolvedFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalResolvedFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.totalResolvedFrame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.totalResolvedCountFrame = QFrame(self.totalResolvedFrame)
        self.totalResolvedCountFrame.setObjectName(u"totalResolvedCountFrame")
        self.totalResolvedCountFrame.setMinimumSize(QSize(120, 111))
        self.totalResolvedCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.totalResolvedCountFrame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.totalResolvedCountLabel = QLabel(self.totalResolvedCountFrame)
        self.totalResolvedCountLabel.setObjectName(u"totalResolvedCountLabel")
        self.totalResolvedCountLabel.setFont(font5)
        self.totalResolvedCountLabel.setStyleSheet(u"color: rgb(38, 166, 154);")
        self.totalResolvedCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.totalResolvedCountLabel, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.totalResolvedCountFrame, 0, 0, 1, 1)

        self.totalResolvedTextFrame = QFrame(self.totalResolvedFrame)
        self.totalResolvedTextFrame.setObjectName(u"totalResolvedTextFrame")
        self.totalResolvedTextFrame.setMinimumSize(QSize(101, 31))
        self.totalResolvedTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.totalResolvedTextFrame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.totalResolvedTextLabel = QLabel(self.totalResolvedTextFrame)
        self.totalResolvedTextLabel.setObjectName(u"totalResolvedTextLabel")
        self.totalResolvedTextLabel.setFont(font6)
        self.totalResolvedTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalResolvedTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.totalResolvedTextLabel, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.totalResolvedTextFrame, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.totalResolvedFrame, 1, 5, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_14, 1, 6, 1, 1)

        self.totalPendingFrame = QFrame(self.infoFrame)
        self.totalPendingFrame.setObjectName(u"totalPendingFrame")
        self.totalPendingFrame.setMinimumSize(QSize(141, 181))
        self.totalPendingFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalPendingFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.totalPendingFrame)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.totalPendingCountFrame = QFrame(self.totalPendingFrame)
        self.totalPendingCountFrame.setObjectName(u"totalPendingCountFrame")
        self.totalPendingCountFrame.setMinimumSize(QSize(120, 111))
        self.totalPendingCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.totalPendingCountFrame)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.totalPendingCountLabel = QLabel(self.totalPendingCountFrame)
        self.totalPendingCountLabel.setObjectName(u"totalPendingCountLabel")
        self.totalPendingCountLabel.setFont(font5)
        self.totalPendingCountLabel.setStyleSheet(u"color: rgb(212, 225, 87);")
        self.totalPendingCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.totalPendingCountLabel, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.totalPendingCountFrame, 0, 0, 1, 1)

        self.totalPendingTextFrame = QFrame(self.totalPendingFrame)
        self.totalPendingTextFrame.setObjectName(u"totalPendingTextFrame")
        self.totalPendingTextFrame.setMinimumSize(QSize(101, 31))
        self.totalPendingTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.totalPendingTextFrame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.totalPendingTextLabel = QLabel(self.totalPendingTextFrame)
        self.totalPendingTextLabel.setObjectName(u"totalPendingTextLabel")
        self.totalPendingTextLabel.setFont(font6)
        self.totalPendingTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalPendingTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.totalPendingTextLabel, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.totalPendingTextFrame, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.totalPendingFrame, 1, 7, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_15, 1, 8, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_12, 2, 3, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_13, 2, 5, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_14, 2, 7, 1, 1)


        self.gridLayout_22.addWidget(self.infoFrame, 0, 0, 1, 1)

        self.buttonsFrame = QFrame(self.mainPage)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.buttonsFrame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_17 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.createIssueButton = QPushButton(self.buttonsFrame)
        self.createIssueButton.setObjectName(u"createIssueButton")
        self.createIssueButton.setMinimumSize(QSize(151, 41))
        self.createIssueButton.setFont(font4)
        self.createIssueButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(66, 66, 66);\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);	\n"
"	border-radius: 15px;\n"
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

        self.gridLayout_20.addWidget(self.createIssueButton, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_18, 0, 4, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_19, 0, 6, 1, 1)

        self.logoutButton = QPushButton(self.buttonsFrame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setMinimumSize(QSize(151, 41))
        self.logoutButton.setFont(font4)
        self.logoutButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	\n"
"	background-color: rgb(213, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-width: 1px;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	\n"
"	background-color: rgb(183, 28, 28);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_20.addWidget(self.logoutButton, 0, 5, 1, 1)

        self.refreshButton = QPushButton(self.buttonsFrame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setMinimumSize(QSize(151, 41))
        self.refreshButton.setFont(font4)
        self.refreshButton.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(66, 66, 66);\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);	\n"
"	border-radius: 15px;\n"
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

        self.gridLayout_20.addWidget(self.refreshButton, 0, 3, 1, 1)


        self.gridLayout_22.addWidget(self.buttonsFrame, 1, 0, 1, 1)

        self.issuesTableFrame = QFrame(self.mainPage)
        self.issuesTableFrame.setObjectName(u"issuesTableFrame")
        self.issuesTableFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.issuesTableFrame.setFrameShape(QFrame.StyledPanel)
        self.issuesTableFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.issuesTableFrame)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.issuesTableWidget = QTableWidget(self.issuesTableFrame)
        if (self.issuesTableWidget.columnCount() < 5):
            self.issuesTableWidget.setColumnCount(5)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font7);
        self.issuesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font7);
        self.issuesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font7);
        self.issuesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font7);
        self.issuesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font7);
        self.issuesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.issuesTableWidget.setObjectName(u"issuesTableWidget")
        font8 = QFont()
        font8.setPointSize(12)
        self.issuesTableWidget.setFont(font8)
        self.issuesTableWidget.setAutoScrollMargin(10)
        self.issuesTableWidget.setTextElideMode(Qt.ElideRight)
        self.issuesTableWidget.setShowGrid(False)
        self.issuesTableWidget.setWordWrap(False)
        self.issuesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.issuesTableWidget.verticalHeader().setVisible(False)

        self.gridLayout_21.addWidget(self.issuesTableWidget, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.issuesTableFrame, 2, 0, 1, 1)

        self.rdStackWidget.addWidget(self.mainPage)

        self.gridLayout.addWidget(self.rdStackWidget, 0, 0, 1, 1)

        RDApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(RDApp)

        self.rdStackWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RDApp)
    # setupUi

    def retranslateUi(self, RDApp):
        RDApp.setWindowTitle(QCoreApplication.translate("RDApp", u"Redmine Desktop V0.1", None))
        self.title1_label.setText(QCoreApplication.translate("RDApp", u"REDMINE", None))
        self.title2_label.setText(QCoreApplication.translate("RDApp", u"DESKTOP", None))
        self.usernameLoginLinedit.setPlaceholderText(QCoreApplication.translate("RDApp", u"Username", None))
        self.passwordLoginLinedit.setPlaceholderText(QCoreApplication.translate("RDApp", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("RDApp", u"Login", None))
        self.totalIssuesCountLabel.setText(QCoreApplication.translate("RDApp", u"25", None))
        self.totalIssuesTextLabel.setText(QCoreApplication.translate("RDApp", u"Issues", None))
        self.totalProjectsCountLabel.setText(QCoreApplication.translate("RDApp", u"5", None))
        self.totalProjectsTextLabel.setText(QCoreApplication.translate("RDApp", u"Projects", None))
        self.totalResolvedCountLabel.setText(QCoreApplication.translate("RDApp", u"10", None))
        self.totalResolvedTextLabel.setText(QCoreApplication.translate("RDApp", u"Resolved", None))
        self.totalPendingCountLabel.setText(QCoreApplication.translate("RDApp", u"15", None))
        self.totalPendingTextLabel.setText(QCoreApplication.translate("RDApp", u"Pending", None))
        self.createIssueButton.setText(QCoreApplication.translate("RDApp", u"Create Issue", None))
        self.logoutButton.setText(QCoreApplication.translate("RDApp", u"Log Out", None))
        self.refreshButton.setText(QCoreApplication.translate("RDApp", u"Refresh", None))
        ___qtablewidgetitem = self.issuesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RDApp", u"ID", None));
        ___qtablewidgetitem1 = self.issuesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RDApp", u"SUBJECT", None));
        ___qtablewidgetitem2 = self.issuesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RDApp", u"STATUS", None));
        ___qtablewidgetitem3 = self.issuesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RDApp", u"PRIORITY", None));
        ___qtablewidgetitem4 = self.issuesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("RDApp", u"DESCRIPTION", None));
    # retranslateUi

