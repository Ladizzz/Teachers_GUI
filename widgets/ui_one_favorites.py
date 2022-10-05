# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_favoritesKnyafB.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(506, 326)
        Form.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        Form.setFont(font)
        Form.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        Form.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame_header = QFrame(Form)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMinimumSize(QSize(0, 50))
        self.frame_header.setStyleSheet(u"")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_name = QLabel(self.frame_header)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_delete = QPushButton(self.frame_header)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy1)
        self.btn_delete.setFont(font)
        icon = QIcon()
        icon.addFile(u"icons/prohibition.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setIconSize(QSize(16, 16))
        self.btn_delete.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_main = QFrame(Form)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy2)
        self.frame_main.setMinimumSize(QSize(500, 0))
        self.frame_main.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_photo = QFrame(self.frame_main)
        self.frame_photo.setObjectName(u"frame_photo")
        self.frame_photo.setMinimumSize(QSize(200, 250))
        self.frame_photo.setMaximumSize(QSize(210, 300))
        self.frame_photo.setFrameShape(QFrame.StyledPanel)
        self.frame_photo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_photo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_image = QLabel(self.frame_photo)
        self.label_image.setObjectName(u"label_image")

        self.horizontalLayout_3.addWidget(self.label_image)


        self.horizontalLayout.addWidget(self.frame_photo)

        self.frame_info = QFrame(self.frame_main)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setStyleSheet(u"QLabel {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"}")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_info)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_role = QLabel(self.frame_info)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setMargin(5)

        self.verticalLayout_3.addWidget(self.label_role)

        self.label_science_role = QLabel(self.frame_info)
        self.label_science_role.setObjectName(u"label_science_role")
        self.label_science_role.setMargin(5)

        self.verticalLayout_3.addWidget(self.label_science_role)

        self.laberl_email = QLabel(self.frame_info)
        self.laberl_email.setObjectName(u"laberl_email")
        self.laberl_email.setMargin(5)

        self.verticalLayout_3.addWidget(self.laberl_email)

        self.label_phone = QLabel(self.frame_info)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setMargin(5)

        self.verticalLayout_3.addWidget(self.label_phone)


        self.horizontalLayout.addWidget(self.frame_info)


        self.verticalLayout.addWidget(self.frame_main)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_image.setText(QCoreApplication.translate("Form", u"Image", None))
        self.label_role.setText(QCoreApplication.translate("Form", u"Role", None))
        self.label_science_role.setText(QCoreApplication.translate("Form", u"ScienceRole", None))
        self.laberl_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_phone.setText(QCoreApplication.translate("Form", u"Phone", None))
    # retranslateUi

