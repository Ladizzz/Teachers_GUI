# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlIcavq.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 430)
        MainWindow.setMinimumSize(QSize(890, 430))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#frame_top_menus .QPushButton {\n"
"	border: 0px solid;\n"
"	text-align: left;\n"
"	padding: 0px 25px 0px 25px;\n"
"	font: 600 11pt \"Mulish SemiBold\";\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_toggle .QPushButton {	\n"
"	border: 0px solid;\n"
"	text-align: left;\n"
"	padding: 0px 25px 0px 23px;\n"
"	font: 600 11pt \"Mulish SemiBold\";\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_top .QPushButton {	\n"
"	border: 0px solid;\n"
"	border-left: 0px solid transparent;\n"
"	text-align: left;\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_top_menus .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#frame_top_menus .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"QListWidget */\n"
"QListWidget {\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 13"
                        "3, 255);\n"
"	font-size: 18pt\n"
"}\n"
"QListWidget::item {\n"
"   height: 40px;\n"
"}\n"
"QListWidget  QScrollBar:vertical {\n"
"    width: 20px;\n"
" }\n"
"QListWidget  QScrollBar:horizontal {\n"
"    height: 20px;\n"
" }\n"
"QListWidget:hover {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QListWidget:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"#list_teachers QLabel{\n"
"	border-color: #e2e2e2;\n"
"	font: 12pt;\n"
"}\n"
"#list_favorites QLabel{\n"
"	border-color: #e2e2e2;\n"
"	font: 12pt;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #e2e2e2;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(40, 44, 52);\n"
"    color: #323232;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}\n"
"/* ////////"
                        "/////////////////////////////////////////////////////////\n"
"TimeEdit */\n"
"QTimeEdit {\n"
"	background-color: #e2e2e2;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 133, 255);\n"
"    color: #323232;\n"
"}\n"
"QTimeEdit:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QTimeEdit:focus {\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QDateEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover{\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QDateEdit::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #939393;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
""
                        "	background-image: url(:/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"/* /////////////////////////////////////////////////////////////////\n"
"QCalendarWidget */\n"
"QCalendarWidget QToolButton{\n"
"color: #000;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#frame_pages QPushButton {\n"
"	border: 2px solid #939393;\n"
"	border-radius: 5px;	\n"
"	background-color: #e2e2e2;\n"
"    color: #000;\n"
"}\n"
"#frame_pages QPushButton:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"#frame_pages QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}\n"
"\n"
"#top_bar QFrame{\n"
"     background-color: #f0f0f0;\n"
"}\n"
"\n"
"#frame_settings QPushButton{\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"#frame_pages QComboBox {\n"
"	border: 2px solid #939393;\n"
"	border-radius: 5px;\n"
"	background-color: #e2e2e2;\n"
"    color: #000;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
""
                        "{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(images/icons/arrow.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 40))
        self.top_bar.setMaximumSize(QSize(16777215, 60))
        self.top_bar.setStyleSheet(u"")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 60))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(0, 133, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_date = QLabel(self.frame_top)
        self.label_date.setObjectName(u"label_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy1)
        self.label_date.setMinimumSize(QSize(600, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_date.setFont(font)
        self.label_date.setStyleSheet(u"font: 500 12pt \"Mulish\";")

        self.horizontalLayout_6.addWidget(self.label_date)

        self.frame_settings = QFrame(self.frame_top)
        self.frame_settings.setObjectName(u"frame_settings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_settings.sizePolicy().hasHeightForWidth())
        self.frame_settings.setSizePolicy(sizePolicy2)
        self.frame_settings.setMaximumSize(QSize(25, 16777215))
        self.frame_settings.setStyleSheet(u"")
        self.frame_settings.setFrameShape(QFrame.NoFrame)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_settings)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.frame_settings)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_settings)


        self.horizontalLayout_6.addWidget(self.frame_settings)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_page_1.sizePolicy().hasHeightForWidth())
        self.btn_page_1.setSizePolicy(sizePolicy3)
        self.btn_page_1.setMinimumSize(QSize(0, 50))
        self.btn_page_1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon2)
        self.btn_page_1.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 50))
        self.btn_page_2.setStyleSheet(u"background-color: rgb(157, 157, 157);")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 50))
        self.btn_page_3.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 50))
        self.btn_page_4.setStyleSheet(u"background-color: rgb(120, 120, 120);")
        icon5 = QIcon()
        icon5.addFile(u"images/icons/favorite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_4.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.btn_page_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setEnabled(True)
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_info = QLabel(self.page_1)
        self.label_info.setObjectName(u"label_info")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_info.setFont(font1)
        self.label_info.setStyleSheet(u"")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_info)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QHeaderView { font-size: 10pt; }")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_table_header = QFrame(self.page_3)
        self.frame_table_header.setObjectName(u"frame_table_header")
        self.frame_table_header.setStyleSheet(u"")
        self.frame_table_header.setFrameShape(QFrame.StyledPanel)
        self.frame_table_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_table_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cb_table_faculty = QComboBox(self.frame_table_header)
        self.cb_table_faculty.setObjectName(u"cb_table_faculty")
        self.cb_table_faculty.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(11)
        self.cb_table_faculty.setFont(font2)

        self.horizontalLayout_9.addWidget(self.cb_table_faculty)

        self.cb_table_cathedra = QComboBox(self.frame_table_header)
        self.cb_table_cathedra.setObjectName(u"cb_table_cathedra")
        self.cb_table_cathedra.setMinimumSize(QSize(0, 30))
        self.cb_table_cathedra.setFont(font2)

        self.horizontalLayout_9.addWidget(self.cb_table_cathedra)

        self.btn_save = QPushButton(self.frame_table_header)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(100, 30))
        self.btn_save.setFont(font2)

        self.horizontalLayout_9.addWidget(self.btn_save)


        self.verticalLayout_7.addWidget(self.frame_table_header)

        self.tableWidget = QTableWidget(self.page_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.Pages_Widget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_header = QFrame(self.page_2)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cb_faculty = QComboBox(self.frame_header)
        self.cb_faculty.setObjectName(u"cb_faculty")
        self.cb_faculty.setMinimumSize(QSize(0, 30))
        self.cb_faculty.setFont(font2)

        self.horizontalLayout_10.addWidget(self.cb_faculty)

        self.cb_cathedra = QComboBox(self.frame_header)
        self.cb_cathedra.setObjectName(u"cb_cathedra")
        self.cb_cathedra.setMinimumSize(QSize(0, 30))
        self.cb_cathedra.setFont(font2)

        self.horizontalLayout_10.addWidget(self.cb_cathedra)

        self.btn_search = QPushButton(self.frame_header)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(100, 30))
        self.btn_search.setFont(font2)

        self.horizontalLayout_10.addWidget(self.btn_search)


        self.verticalLayout_11.addWidget(self.frame_header)

        self.frame_search = QFrame(self.page_2)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_list = QFrame(self.frame_search)
        self.frame_list.setObjectName(u"frame_list")
        self.frame_list.setMaximumSize(QSize(500, 16777215))
        self.frame_list.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.frame_list.setFrameShape(QFrame.StyledPanel)
        self.frame_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_list)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.line_search = QLineEdit(self.frame_list)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setMinimumSize(QSize(100, 30))

        self.verticalLayout_10.addWidget(self.line_search)

        self.tableView = QTableView(self.frame_list)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMaximumSize(QSize(16777215, 16777215))
        self.tableView.horizontalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.tableView)


        self.horizontalLayout_8.addWidget(self.frame_list)

        self.list_teachers = QListWidget(self.frame_search)
        self.list_teachers.setObjectName(u"list_teachers")

        self.horizontalLayout_8.addWidget(self.list_teachers)


        self.verticalLayout_11.addWidget(self.frame_search)

        self.Pages_Widget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_8 = QVBoxLayout(self.page_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(16)
        self.label.setFont(font3)

        self.verticalLayout_8.addWidget(self.label)

        self.list_favorites = QListWidget(self.page_4)
        self.list_favorites.setObjectName(u"list_favorites")

        self.verticalLayout_8.addWidget(self.list_favorites)

        self.Pages_Widget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_settings.setText("")
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u043f\u043e\u0438\u0441\u043a\u043e\u0432\u0443\u044e </p><p>\u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0435\u0439!</p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.line_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
    # retranslateUi

