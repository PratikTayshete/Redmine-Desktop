# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RDMainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RDMain(object):
    def setupUi(self, RDMain):
        if not RDMain.objectName():
            RDMain.setObjectName(u"RDMain")
        RDMain.resize(1124, 826)
        RDMain.setMinimumSize(QSize(1124, 826))
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        RDMain.setFont(font)
        RDMain.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.centralwidget = QWidget(RDMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.infoFrame = QFrame(self.centralwidget)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.infoFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 5, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.totalIssuesFrame = QFrame(self.infoFrame)
        self.totalIssuesFrame.setObjectName(u"totalIssuesFrame")
        self.totalIssuesFrame.setMinimumSize(QSize(141, 181))
        self.totalIssuesFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalIssuesFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.totalIssuesFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.totalIssuesCountFrame = QFrame(self.totalIssuesFrame)
        self.totalIssuesCountFrame.setObjectName(u"totalIssuesCountFrame")
        self.totalIssuesCountFrame.setMinimumSize(QSize(120, 111))
        self.totalIssuesCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.totalIssuesCountFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.totalIssuesCountLabel = QLabel(self.totalIssuesCountFrame)
        self.totalIssuesCountLabel.setObjectName(u"totalIssuesCountLabel")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(50)
        self.totalIssuesCountLabel.setFont(font1)
        self.totalIssuesCountLabel.setStyleSheet(u"color: rgb(239, 83, 80);")
        self.totalIssuesCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.totalIssuesCountLabel, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.totalIssuesCountFrame, 0, 0, 1, 1)

        self.totalIssuesTextFrame = QFrame(self.totalIssuesFrame)
        self.totalIssuesTextFrame.setObjectName(u"totalIssuesTextFrame")
        self.totalIssuesTextFrame.setMinimumSize(QSize(101, 31))
        self.totalIssuesTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalIssuesTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.totalIssuesTextFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.totalIssuesTextLabel = QLabel(self.totalIssuesTextFrame)
        self.totalIssuesTextLabel.setObjectName(u"totalIssuesTextLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(10)
        self.totalIssuesTextLabel.setFont(font2)
        self.totalIssuesTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalIssuesTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.totalIssuesTextLabel, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.totalIssuesTextFrame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.totalIssuesFrame, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.totalProjectsFrame = QFrame(self.infoFrame)
        self.totalProjectsFrame.setObjectName(u"totalProjectsFrame")
        self.totalProjectsFrame.setMinimumSize(QSize(141, 181))
        self.totalProjectsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalProjectsFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.totalProjectsFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.totalProjectsCountFrame = QFrame(self.totalProjectsFrame)
        self.totalProjectsCountFrame.setObjectName(u"totalProjectsCountFrame")
        self.totalProjectsCountFrame.setMinimumSize(QSize(120, 111))
        self.totalProjectsCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.totalProjectsCountFrame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.totalProjectsCountLabel = QLabel(self.totalProjectsCountFrame)
        self.totalProjectsCountLabel.setObjectName(u"totalProjectsCountLabel")
        self.totalProjectsCountLabel.setFont(font1)
        self.totalProjectsCountLabel.setStyleSheet(u"color: rgb(236, 64, 122);")
        self.totalProjectsCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.totalProjectsCountLabel, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.totalProjectsCountFrame, 0, 0, 1, 1)

        self.totalProjectsTextFrame = QFrame(self.totalProjectsFrame)
        self.totalProjectsTextFrame.setObjectName(u"totalProjectsTextFrame")
        self.totalProjectsTextFrame.setMinimumSize(QSize(101, 31))
        self.totalProjectsTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalProjectsTextFrame.setFrameShadow(QFrame.Raised)
        self.totalProjectsTextLabel = QLabel(self.totalProjectsTextFrame)
        self.totalProjectsTextLabel.setObjectName(u"totalProjectsTextLabel")
        self.totalProjectsTextLabel.setGeometry(QRect(30, 10, 55, 16))
        self.totalProjectsTextLabel.setFont(font2)
        self.totalProjectsTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalProjectsTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.totalProjectsTextFrame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.totalProjectsFrame, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.totalResolvedFrame = QFrame(self.infoFrame)
        self.totalResolvedFrame.setObjectName(u"totalResolvedFrame")
        self.totalResolvedFrame.setMinimumSize(QSize(141, 181))
        self.totalResolvedFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalResolvedFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.totalResolvedFrame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.totalResolvedCountFrame = QFrame(self.totalResolvedFrame)
        self.totalResolvedCountFrame.setObjectName(u"totalResolvedCountFrame")
        self.totalResolvedCountFrame.setMinimumSize(QSize(120, 111))
        self.totalResolvedCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.totalResolvedCountFrame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.totalResolvedCountLabel = QLabel(self.totalResolvedCountFrame)
        self.totalResolvedCountLabel.setObjectName(u"totalResolvedCountLabel")
        self.totalResolvedCountLabel.setFont(font1)
        self.totalResolvedCountLabel.setStyleSheet(u"color: rgb(38, 166, 154);")
        self.totalResolvedCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.totalResolvedCountLabel, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.totalResolvedCountFrame, 0, 0, 1, 1)

        self.totalResolvedTextFrame = QFrame(self.totalResolvedFrame)
        self.totalResolvedTextFrame.setObjectName(u"totalResolvedTextFrame")
        self.totalResolvedTextFrame.setMinimumSize(QSize(101, 31))
        self.totalResolvedTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalResolvedTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.totalResolvedTextFrame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.totalResolvedTextLabel = QLabel(self.totalResolvedTextFrame)
        self.totalResolvedTextLabel.setObjectName(u"totalResolvedTextLabel")
        self.totalResolvedTextLabel.setFont(font2)
        self.totalResolvedTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalResolvedTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.totalResolvedTextLabel, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.totalResolvedTextFrame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.totalResolvedFrame, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.totalPendingFrame = QFrame(self.infoFrame)
        self.totalPendingFrame.setObjectName(u"totalPendingFrame")
        self.totalPendingFrame.setMinimumSize(QSize(141, 181))
        self.totalPendingFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        self.totalPendingFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.totalPendingFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.totalPendingCountFrame = QFrame(self.totalPendingFrame)
        self.totalPendingCountFrame.setObjectName(u"totalPendingCountFrame")
        self.totalPendingCountFrame.setMinimumSize(QSize(120, 111))
        self.totalPendingCountFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingCountFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.totalPendingCountFrame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.totalPendingCountLabel = QLabel(self.totalPendingCountFrame)
        self.totalPendingCountLabel.setObjectName(u"totalPendingCountLabel")
        self.totalPendingCountLabel.setFont(font1)
        self.totalPendingCountLabel.setStyleSheet(u"color: rgb(212, 225, 87);")
        self.totalPendingCountLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.totalPendingCountLabel, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.totalPendingCountFrame, 0, 0, 1, 1)

        self.totalPendingTextFrame = QFrame(self.totalPendingFrame)
        self.totalPendingTextFrame.setObjectName(u"totalPendingTextFrame")
        self.totalPendingTextFrame.setMinimumSize(QSize(101, 31))
        self.totalPendingTextFrame.setFrameShape(QFrame.StyledPanel)
        self.totalPendingTextFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.totalPendingTextFrame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.totalPendingTextLabel = QLabel(self.totalPendingTextFrame)
        self.totalPendingTextLabel.setObjectName(u"totalPendingTextLabel")
        self.totalPendingTextLabel.setFont(font2)
        self.totalPendingTextLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalPendingTextLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.totalPendingTextLabel, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.totalPendingTextFrame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.totalPendingFrame, 1, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 8, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 2, 5, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 2, 7, 1, 1)


        self.gridLayout_5.addWidget(self.infoFrame, 0, 0, 1, 1)

        self.buttonsFrame = QFrame(self.centralwidget)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.buttonsFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.createIssueButton = QPushButton(self.buttonsFrame)
        self.createIssueButton.setObjectName(u"createIssueButton")
        self.createIssueButton.setMinimumSize(QSize(151, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.createIssueButton.setFont(font3)
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

        self.gridLayout_4.addWidget(self.createIssueButton, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.refreshContentButton = QPushButton(self.buttonsFrame)
        self.refreshContentButton.setObjectName(u"refreshContentButton")
        self.refreshContentButton.setMinimumSize(QSize(151, 41))
        self.refreshContentButton.setFont(font3)
        self.refreshContentButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.refreshContentButton, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.logoutButton = QPushButton(self.buttonsFrame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setMinimumSize(QSize(151, 41))
        self.logoutButton.setFont(font3)
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

        self.gridLayout_4.addWidget(self.logoutButton, 0, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 0, 6, 1, 1)


        self.gridLayout_5.addWidget(self.buttonsFrame, 1, 0, 1, 1)

        self.issuesFrame = QFrame(self.centralwidget)
        self.issuesFrame.setObjectName(u"issuesFrame")
        self.issuesFrame.setMinimumSize(QSize(1111, 511))
        self.issuesFrame.setFrameShape(QFrame.StyledPanel)
        self.issuesFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.issuesFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.issuesFrame, 2, 0, 1, 1)

        RDMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(RDMain)

        QMetaObject.connectSlotsByName(RDMain)
    # setupUi

    def retranslateUi(self, RDMain):
        RDMain.setWindowTitle(QCoreApplication.translate("RDMain", u"Redmine Desktop V0.1", None))
        self.totalIssuesCountLabel.setText(QCoreApplication.translate("RDMain", u"25", None))
        self.totalIssuesTextLabel.setText(QCoreApplication.translate("RDMain", u"Issues", None))
        self.totalProjectsCountLabel.setText(QCoreApplication.translate("RDMain", u"2", None))
        self.totalProjectsTextLabel.setText(QCoreApplication.translate("RDMain", u"Projects", None))
        self.totalResolvedCountLabel.setText(QCoreApplication.translate("RDMain", u"10", None))
        self.totalResolvedTextLabel.setText(QCoreApplication.translate("RDMain", u"Resolved", None))
        self.totalPendingCountLabel.setText(QCoreApplication.translate("RDMain", u"15", None))
        self.totalPendingTextLabel.setText(QCoreApplication.translate("RDMain", u"Pending", None))
        self.createIssueButton.setText(QCoreApplication.translate("RDMain", u"Create Issue", None))
        self.refreshContentButton.setText(QCoreApplication.translate("RDMain", u"Refresh", None))
        self.logoutButton.setText(QCoreApplication.translate("RDMain", u"Log Out", None))
    # retranslateUi

