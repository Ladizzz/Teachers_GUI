################################################################################
#
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.2.1
#
################################################################################
import ctypes
import datetime
import locale
import os
import sqlite3
import sys
import time

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PyQt6.QtCore import pyqtSlot
from PySide6.QtCore import Slot

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from modules import *
from widgets import *
from datetime import date

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings_window = SettingsWindow()

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Информационно-поисковая система преподавателей"
        # APPLY TEXTS
        self.setWindowTitle(title)

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/db'
        self.db_path = os.path.join(self.BASE_DIR, "teachers.db")
        self.db_connection = ''
       
        self.teacher_list = []
        self.faculties_raw = []
        self.departments_raw = []
        self.faculty_idx = 0
        self.department_idx = 0
        self.department_name = ''
        self.faculty_name = ''
        
        today = date.today()
        locale.setlocale(locale.LC_TIME, "ru_RU")
        self.ui.label_date.setText(today.strftime("%d.%m.%Y, %A"))

        # TOGGLE/BURGER MENU
        ########################################################################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggle_menu(self, 200, True))

        # PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(self.change_page)

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(self.change_page)

        self.ui.cb_table_faculty.currentIndexChanged.connect(self.faculty_index_changed_table)
        self.ui.cb_table_cathedra.currentIndexChanged.connect(self.department_index_changed_table)

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(self.change_page)

        # PAGE 3 - Search button
        self.ui.cb_faculty.currentIndexChanged.connect(self.faculty_index_changed)
        self.ui.cb_cathedra.currentIndexChanged.connect(self.department_index_changed)
        self.ui.btn_search.clicked.connect(self.faculty_loaded)
        self.ui.btn_save.clicked.connect(self.save_table)

        # PAGE 4
        self.ui.btn_page_4.clicked.connect(self.change_page)

        self.ui.btn_settings.clicked.connect(self.settings)

        self.ui.btn_page_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END

    def change_page(self):
        self.ui.btn_page_1.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.ui.btn_page_2.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.ui.btn_page_3.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.ui.btn_page_4.setStyleSheet("background-color: rgb(120, 120, 120);")
        page = ''
        sender = self.sender()
        if sender == self.ui.btn_page_1:
            print('PyQt5 button click 1\n')
            page = self.ui.page_1
        elif sender == self.ui.btn_page_2:
            print('PyQt5 button click 2\n')
            try:
                self.faculties_raw = self.show_table_data('BNTU')
                page = self.ui.page_2
            except sqlite3.OperationalError:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Произошла ошибка! Обновите базу данных")
                msgBox.setWindowTitle("Инофрмационно-поисковая система")
                msgBox.exec()
            self.ui.cb_faculty.clear()
            names = []
            for name in self.faculties_raw:
                names.append(name[1])
            # print(self.faculties_raw)
            self.ui.cb_faculty.addItems(names)
        elif sender == self.ui.btn_page_3:
            print('PyQt5 button click 3\n')
            try:
                self.faculties_raw = self.show_table_data('BNTU')
                page = self.ui.page_3
            except sqlite3.OperationalError:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Произошла ошибка! Обновите базу данных")
                msgBox.setWindowTitle("Инофрмационно-поисковая система")
                msgBox.exec()
            self.ui.cb_table_faculty.clear()
            names = []
            for name in self.faculties_raw:
                names.append(name[1])
            self.ui.cb_table_faculty.addItems(names)
        else:
            print('PyQt5 button click 4\n')
            page = self.ui.page_4

        if page != '':
            self.ui.Pages_Widget.setCurrentWidget(page)
            sender.setStyleSheet("background-color: white; border-radius: 30px;")

    def settings(self):
        print('PyQt5 button click Settings\n')
        self.settings_window.ui.comboBox.currentIndexChanged.connect(lambda: SettingsWindow.selection_changed(self))
        self.settings_window.show()

    def faculty_index_changed(self):
        print('faculty_index_changed')
        self.faculty_idx = self.ui.cb_faculty.currentIndex()
        faculty = self.faculties_raw[self.faculty_idx][0]
        print(faculty)
        self.faculty_name = faculty
        self.departments_raw = self.show_table_data(faculty)
        names = []
        for name in self.departments_raw:
            names.append(name[1])
        self.ui.cb_cathedra.clear()
        self.ui.cb_cathedra.addItems(names)

    def faculty_index_changed_table(self):
        print('faculty_index_changed_table')
        self.faculty_idx = self.ui.cb_table_faculty.currentIndex()
        faculty = self.faculties_raw[self.faculty_idx][0]
        print(faculty)
        self.departments_raw = self.show_table_data(faculty)
        names = []
        for name in self.departments_raw:
            names.append(name[1])
        self.ui.cb_table_cathedra.clear()
        self.ui.cb_table_cathedra.addItems(names)

    def department_index_changed(self):
        print('department_index_changed')
        self.department_idx = self.ui.cb_cathedra.currentIndex()
        self.department_name = self.departments_raw[self.department_idx][0]
        print(self.department_name)
        self.faculty_loaded()

    def department_index_changed_table(self):
        print('department_index_changed_table')
        self.department_idx = self.ui.cb_table_cathedra.currentIndex()
        self.department_name = self.departments_raw[self.department_idx][0]
        print(self.department_name)
        self.faculty_loaded_table()

    # after getting data
    def faculty_loaded(self):
        print('faculty_loaded')
        # saving list
        print(self.department_name)
        self.teacher_list = self.show_table_data(self.department_name)
        print(self.teacher_list)
        data = []

        for number, item in enumerate(self.teacher_list):
            data.append(item[1])

        model = QStandardItemModel(len(data), 1)
        print(data)
        for row, person in enumerate(data):
            item = QStandardItem(person)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0)

        self.ui.line_search.textChanged.connect(filter_proxy_model.setFilterRegularExpression)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setModel(filter_proxy_model)

        selection = self.ui.tableView.selectionModel()
        selection.selectionChanged.connect(self.selection_changed)

    def faculty_loaded_table(self):
        print('faculty_loaded_table')
        print(self.department_name)
        self.teacher_list = self.show_table_data(self.department_name)
        print(self.teacher_list)
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(len(self.teacher_list))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Science role", "Role", "Phone", "Email", "Photo"])

        for number, item in enumerate(self.teacher_list):
            self.ui.tableWidget.setItem(number, 0, QTableWidgetItem(item[1]))
            self.ui.tableWidget.setItem(number, 1, QTableWidgetItem(item[2]))
            self.ui.tableWidget.setItem(number, 2, QTableWidgetItem(item[3]))
            self.ui.tableWidget.setItem(number, 3, QTableWidgetItem(item[4]))
            self.ui.tableWidget.setItem(number, 4, QTableWidgetItem(item[5]))
            self.ui.tableWidget.setItem(number, 5, QTableWidgetItem(item[6]))

        self.ui.tableWidget.resizeColumnsToContents()

    def save_table(self):
        self.db_connection = sqlite3.connect(self.db_path)
        for row in range(self.ui.tableWidget.rowCount()):
            sql_str = f"UPDATE {self.department_name} " \
                f"SET name = '{self.ui.tableWidget.item(row, 0).text()}'," \
                f" science_role = '{self.ui.tableWidget.item(row, 1).text()}'," \
                f" role = '{self.ui.tableWidget.item(row, 2).text()}'," \
                f" phone = '{self.ui.tableWidget.item(row, 3).text()}'," \
                f" email = '{self.ui.tableWidget.item(row, 4).text()}'," \
                f" photo = '{self.ui.tableWidget.item(row, 5).text()}'" \
                f" WHERE number = {row + 1}"
            self.db_connection.execute(sql_str)
        self.db_connection.commit()
        self.db_connection.close()
        self.db_connection = ''
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Сохранено успешно!")
        msgBox.setWindowTitle("Инофрмационно-поисковая система")
        msgBox.exec()
        print('SUCCESSFULLY SAVED!')

    def show_table_data(self, table='BNTU', column='*'):
        self.db_connection = sqlite3.connect(self.db_path)
        result = []
        sql_str = f'SELECT {column} FROM {table}'
        # print(sql_str)
        for row in self.db_connection.execute(sql_str):
            result.append(row)
        self.db_connection.close()
        self.db_connection = ''
        return result

    def selection_changed(self):
        self.ui.list_teachers.clear()
        for index in self.ui.tableView.selectionModel().selectedRows():
            item = ''
            int_index = 0
            for idx in range(len(self.teacher_list)):
                if self.teacher_list[idx][1] == index.data():
                    item = self.teacher_list[idx]
                    int_index = idx
                    break

            list_widget_item = QListWidgetItem(self.ui.list_teachers)
            inst_pop_up = OnePopUp()
            list_widget_item.setSizeHint(inst_pop_up.frameSize())
            inst_pop_up.ui.label_name.setText(f"{item[0]}: {item[1]}")
            inst_pop_up.ui.label_science_role.setText(f"{item[2]}")
            inst_pop_up.ui.label_role.setText(f"{item[3]}")
            inst_pop_up.ui.label_phone.setText(f"{item[4]}")
            inst_pop_up.ui.laberl_email.setText(f"{item[5]}")
            pixmap = QPixmap(f"{item[6]}")
            scaled_pixmap = pixmap.scaled(inst_pop_up.ui.frame_photo.size(), Qt.KeepAspectRatio)
            inst_pop_up.ui.label_image.setPixmap(scaled_pixmap)
            inst_pop_up.ui.label_image.setAlignment(Qt.AlignCenter)
            inst_pop_up.ui.btn_to_favorites.clicked.connect(self.to_favorites_search)
            list_widget_item.setData(41, int_index)
            list_widget_item.setData(42, inst_pop_up.ui.btn_to_favorites)
            self.ui.list_teachers.setItemWidget(list_widget_item, inst_pop_up)

    def to_favorites_search(self):
        print(f'To_favorites request came from {self.sender()}\n')
        number = ''
        # finding selected train
        for train in range(self.ui.list_teachers.count()):
            # print(f'{str(self.ui.list_teachers.item(train).data(42))}')
            # 42 - button address, 41 - train number
            if str(self.sender()) == str(self.ui.list_teachers.item(train).data(42)):
                number = self.ui.list_teachers.item(train).data(41)
        print(f'Selected {number} to_favorites button\n')
        self.to_favorites_add([self.teacher_list[number]])

    def to_favorites_add(self, in_list):
        print('To_favorites_ADD\n')
        # print(rw_list)
        for number, item in enumerate(in_list):
            list_widget_item = QListWidgetItem(self.ui.list_favorites)
            inst_pop_up = OneFavorites()
            list_widget_item.setSizeHint(inst_pop_up.frameSize())
            inst_pop_up.ui.label_name.setText(f"{item[0]}: {item[1]}")
            inst_pop_up.ui.label_science_role.setText(f"{item[2]}")
            inst_pop_up.ui.label_role.setText(f"{item[3]}")
            inst_pop_up.ui.label_phone.setText(f"{item[4]}")
            inst_pop_up.ui.laberl_email.setText(f"{item[5]}")
            pixmap = QPixmap(f"{item[6]}")
            scaled_pixmap = pixmap.scaled(inst_pop_up.ui.frame_photo.size(), Qt.KeepAspectRatio)
            inst_pop_up.ui.label_image.setPixmap(scaled_pixmap)
            inst_pop_up.ui.label_image.setAlignment(Qt.AlignCenter)
            inst_pop_up.ui.btn_delete.clicked.connect(self.to_favorites_delete)
            list_widget_item.setData(41, number)
            list_widget_item.setData(42, inst_pop_up.ui.btn_delete)
            self.ui.list_favorites.setItemWidget(list_widget_item, inst_pop_up)
            # Finally adding the itemWidget to the list
            # ui->listWidget->setItemWidget(listWidgetItem, theWidgetItem);

    def to_favorites_delete(self):
        print(f'To_favorites delete request came from {self.sender()}\n')
        number = ''
        # finding selected train
        for teacher_idx in range(self.ui.list_favorites.count()):
            print(f'{str(self.ui.list_favorites.item(teacher_idx).data(42))}')
            # 42 - button address, 41 - train number
            if str(self.sender()) == str(self.ui.list_favorites.item(teacher_idx).data(42)):
                number = teacher_idx
        print(f'Selected {number} delete button\n')
        self.ui.list_favorites.takeItem(number)


if __name__ == "__main__":
    myappid = u'bntu.teachers_gui'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication()
    app.setWindowIcon(QIcon("images/icons/icon.svg"))
    window = MainWindow()
    sys.exit(app.exec())
