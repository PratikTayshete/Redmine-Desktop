# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IssueDialogUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateIssue(object):
    def setupUi(self, CreateIssue):
        if not CreateIssue.objectName():
            CreateIssue.setObjectName(u"CreateIssue")
        CreateIssue.resize(744, 667)
        CreateIssue.setMinimumSize(QSize(722, 578))
        CreateIssue.setMaximumSize(QSize(744, 667))
        font = QFont()
        font.setFamily(u"Segoe UI")
        CreateIssue.setFont(font)
        CreateIssue.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 25px;\n"
"}")
        CreateIssue.setSizeGripEnabled(False)
        CreateIssue.setModal(False)
        self.gridLayout_2 = QGridLayout(CreateIssue)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.newIssueTitleFrame = QFrame(CreateIssue)
        self.newIssueTitleFrame.setObjectName(u"newIssueTitleFrame")
        self.newIssueTitleFrame.setMinimumSize(QSize(0, 60))
        self.newIssueTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.newIssueTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.newIssueTitleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.newIssueTitleFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.newIssueTitleText = QLabel(self.newIssueTitleFrame)
        self.newIssueTitleText.setObjectName(u"newIssueTitleText")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(25)
        self.newIssueTitleText.setFont(font1)
        self.newIssueTitleText.setStyleSheet(u"QLabel {\n"
"	\n"
"	color: rgb(217, 215, 52);\n"
"}")
        self.newIssueTitleText.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.newIssueTitleText, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.newIssueTitleFrame, 0, 0, 1, 1)

        self.createIssueFrame = QFrame(CreateIssue)
        self.createIssueFrame.setObjectName(u"createIssueFrame")
        self.createIssueFrame.setMinimumSize(QSize(722, 578))
        self.createIssueFrame.setMaximumSize(QSize(722, 578))
        self.createIssueFrame.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgb(97, 97, 97);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid white;\n"
"	padding-left: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(97, 97, 97);\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
" 	width: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(97, 97, 97);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid white;\n"
"	padding-left: 14px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(97, 97, 97);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid white;\n"
"	padding-left: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(66, 66, 66);\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);	\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {"
                        "\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"	color: rgb(255, 255, 255);\n"
"	border-width: 1px;\n"
"	border-color:  rgb(255, 255, 255);\n"
"	border-style: inset;\n"
"}")
        self.createIssueFrame.setFrameShape(QFrame.StyledPanel)
        self.createIssueFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.createIssueFrame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.selectProjectFrame = QFrame(self.createIssueFrame)
        self.selectProjectFrame.setObjectName(u"selectProjectFrame")
        self.selectProjectFrame.setMinimumSize(QSize(671, 51))
        self.selectProjectFrame.setMaximumSize(QSize(671, 51))
        self.selectProjectFrame.setFrameShape(QFrame.StyledPanel)
        self.selectProjectFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.selectProjectFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.projectLabel = QLabel(self.selectProjectFrame)
        self.projectLabel.setObjectName(u"projectLabel")
        self.projectLabel.setMinimumSize(QSize(100, 0))
        self.projectLabel.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(12)
        self.projectLabel.setFont(font2)
        self.projectLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.projectLabel, 0, 0, 1, 1)

        self.projectComboBox = QComboBox(self.selectProjectFrame)
        self.projectComboBox.setObjectName(u"projectComboBox")
        self.projectComboBox.setMinimumSize(QSize(0, 30))
        self.projectComboBox.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(9)
        self.projectComboBox.setFont(font3)
        self.projectComboBox.setIconSize(QSize(10, 10))
        self.projectComboBox.setFrame(True)

        self.gridLayout_3.addWidget(self.projectComboBox, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.selectProjectFrame, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.selectTrackerFrame = QFrame(self.createIssueFrame)
        self.selectTrackerFrame.setObjectName(u"selectTrackerFrame")
        self.selectTrackerFrame.setMinimumSize(QSize(671, 51))
        self.selectTrackerFrame.setMaximumSize(QSize(671, 51))
        self.selectTrackerFrame.setFrameShape(QFrame.StyledPanel)
        self.selectTrackerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.selectTrackerFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.trackerLabel = QLabel(self.selectTrackerFrame)
        self.trackerLabel.setObjectName(u"trackerLabel")
        self.trackerLabel.setMinimumSize(QSize(100, 0))
        self.trackerLabel.setMaximumSize(QSize(100, 16777215))
        self.trackerLabel.setFont(font2)
        self.trackerLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.trackerLabel, 0, 0, 1, 1)

        self.trackerComboBox = QComboBox(self.selectTrackerFrame)
        self.trackerComboBox.setObjectName(u"trackerComboBox")
        self.trackerComboBox.setMinimumSize(QSize(0, 30))
        self.trackerComboBox.setMaximumSize(QSize(16777215, 30))
        self.trackerComboBox.setFont(font3)

        self.gridLayout_4.addWidget(self.trackerComboBox, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.selectTrackerFrame, 3, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.addSubjectFrame = QFrame(self.createIssueFrame)
        self.addSubjectFrame.setObjectName(u"addSubjectFrame")
        self.addSubjectFrame.setMinimumSize(QSize(671, 51))
        self.addSubjectFrame.setMaximumSize(QSize(671, 51))
        self.addSubjectFrame.setFrameShape(QFrame.StyledPanel)
        self.addSubjectFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.addSubjectFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.subjectLabel = QLabel(self.addSubjectFrame)
        self.subjectLabel.setObjectName(u"subjectLabel")
        self.subjectLabel.setMinimumSize(QSize(0, 30))
        self.subjectLabel.setMaximumSize(QSize(16777215, 30))
        self.subjectLabel.setFont(font2)
        self.subjectLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.subjectLabel, 0, 0, 1, 1)

        self.subjectLineEdit = QLineEdit(self.addSubjectFrame)
        self.subjectLineEdit.setObjectName(u"subjectLineEdit")
        self.subjectLineEdit.setMinimumSize(QSize(540, 30))
        self.subjectLineEdit.setMaximumSize(QSize(540, 30))
        self.subjectLineEdit.setFont(font3)

        self.gridLayout_6.addWidget(self.subjectLineEdit, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.addSubjectFrame, 5, 1, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 5, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 6, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 7, 0, 1, 1)

        self.addDescriptionFrame = QFrame(self.createIssueFrame)
        self.addDescriptionFrame.setObjectName(u"addDescriptionFrame")
        self.addDescriptionFrame.setMinimumSize(QSize(671, 100))
        self.addDescriptionFrame.setMaximumSize(QSize(671, 100))
        self.addDescriptionFrame.setFrameShape(QFrame.StyledPanel)
        self.addDescriptionFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.addDescriptionFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.descriptionLabel = QLabel(self.addDescriptionFrame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setFont(font2)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.descriptionLabel, 0, 0, 1, 1)

        self.descriptionTextEdit = QPlainTextEdit(self.addDescriptionFrame)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setMinimumSize(QSize(540, 80))
        self.descriptionTextEdit.setMaximumSize(QSize(540, 80))
        self.descriptionTextEdit.setFont(font3)

        self.gridLayout_5.addWidget(self.descriptionTextEdit, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.addDescriptionFrame, 7, 1, 1, 3)

        self.horizontalSpacer_8 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 7, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 8, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_9, 9, 0, 1, 1)

        self.selectPriorityFrame = QFrame(self.createIssueFrame)
        self.selectPriorityFrame.setObjectName(u"selectPriorityFrame")
        self.selectPriorityFrame.setMinimumSize(QSize(671, 51))
        self.selectPriorityFrame.setMaximumSize(QSize(671, 51))
        self.selectPriorityFrame.setFrameShape(QFrame.StyledPanel)
        self.selectPriorityFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.selectPriorityFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.priorityLabel = QLabel(self.selectPriorityFrame)
        self.priorityLabel.setObjectName(u"priorityLabel")
        self.priorityLabel.setFont(font2)

        self.gridLayout_7.addWidget(self.priorityLabel, 0, 0, 1, 1)

        self.priorityComboBox = QComboBox(self.selectPriorityFrame)
        self.priorityComboBox.setObjectName(u"priorityComboBox")
        self.priorityComboBox.setMinimumSize(QSize(540, 30))
        self.priorityComboBox.setMaximumSize(QSize(540, 30))
        self.priorityComboBox.setFont(font3)

        self.gridLayout_7.addWidget(self.priorityComboBox, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.selectPriorityFrame, 9, 1, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 9, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 10, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 11, 1, 1, 1)

        self.newIssueButton = QPushButton(self.createIssueFrame)
        self.newIssueButton.setObjectName(u"newIssueButton")
        self.newIssueButton.setMinimumSize(QSize(111, 31))
        self.newIssueButton.setMaximumSize(QSize(111, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        self.newIssueButton.setFont(font4)

        self.gridLayout_8.addWidget(self.newIssueButton, 11, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 11, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 12, 2, 1, 1)


        self.gridLayout_2.addWidget(self.createIssueFrame, 1, 0, 1, 1)


        self.retranslateUi(CreateIssue)

        QMetaObject.connectSlotsByName(CreateIssue)
    # setupUi

    def retranslateUi(self, CreateIssue):
        CreateIssue.setWindowTitle(QCoreApplication.translate("CreateIssue", u"Redmine Desktop V0.1", None))
        self.newIssueTitleText.setText(QCoreApplication.translate("CreateIssue", u"NEW ISSUE", None))
        self.projectLabel.setText(QCoreApplication.translate("CreateIssue", u"Project :", None))
        self.trackerLabel.setText(QCoreApplication.translate("CreateIssue", u"Trackers :", None))
        self.subjectLabel.setText(QCoreApplication.translate("CreateIssue", u"Subject :", None))
        self.descriptionLabel.setText(QCoreApplication.translate("CreateIssue", u"Description :", None))
        self.priorityLabel.setText(QCoreApplication.translate("CreateIssue", u"Priority :", None))
        self.newIssueButton.setText(QCoreApplication.translate("CreateIssue", u"Create", None))
    # retranslateUi

