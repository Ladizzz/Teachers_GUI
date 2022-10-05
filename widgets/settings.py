import os
import sqlite3
import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from .ui_settings import Ui_MainWindow

import lxml.html
import lxml.etree
import requests
import re
from pathlib import Path


class SettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Step 2: Create a QThread object
        self.worker = Worker()
        # Step 3: Create a worker object
        self.thread = QThread(parent=None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        title = "Settings"
        self.setWindowTitle(title)
        self.ui.comboBox.addItems(["Светлая", "Темная"])
        self.ui.pushButton.clicked.connect(self.update)

    def update(self):
        print('Update button clicked')
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.parse_faculties)
        self.worker.finished.connect(self.thread.quit)
        self.worker.progressed.connect(self.progress_edit)
        # Step 6: Start the thread
        self.thread.start()
        self.worker.finished.connect(self.update_finished)

    def progress_edit(self, number):
        print(f'ProgressBar value - {number}')
        self.ui.progressBar.setValue(number)

    def update_finished(self):
        print('Update finished')
        self.thread.started.disconnect(self.worker.parse_faculties)
        self.worker.finished.disconnect(self.thread.quit)
        self.worker.finished.disconnect(self.update_finished)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Инофрмационно-поисковая система")
        if self.worker.successful_exit:
            msgBox.setText("Сохранено успешно!")
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setText("Произошла ошибка!")
            msgBox.setIcon(QMessageBox.Critical)
        msgBox.exec()

    def selection_changed(self):
        if self.settings_window.ui.comboBox.currentIndex() == 0:
            themeFile = "themes\white.qss"
            str = open(themeFile, 'r').read()
            self.ui.centralwidget.setStyleSheet(str)
        else:
            themeFile = "themes\dark.qss"
            str = open(themeFile, 'r').read()
            self.ui.centralwidget.setStyleSheet(str)


# Step 1: Create a worker class
class Worker(QObject):
    finished = Signal()
    progressed = Signal(float)

    def __init__(self):
        super().__init__()
        self.faculty_name = ''
        self.start_url = 'https://bntu.by/faculties'
        # self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIR = Path(__file__).parents[1]
        self.db_path = os.path.join(self.BASE_DIR, "db\\teachers.db")
        self.db_connection = ''
        self.cursor = ''
        self.university_name = 'BNTU'
        self.successful_exit = False

    def show_table_data(self, faculty='poist'):
        sql_str = f'SELECT * FROM {faculty}'
        for row in self.cursor.result.execute(sql_str):
            print(row)

    def parse_faculties(self):
        """Long-running task (Update Database)"""
        print('Parse started')
        print(self.db_path)
        try:
            os.remove(self.db_path)
            print(f'File {self.db_path} deleted')
        except OSError:
            print('File not exists, creating new file...')
        try:
            self.db_connection = sqlite3.connect(self.db_path)
            self.cursor = self.db_connection.cursor()
            self.db_connection.execute(
                "CREATE TABLE " + self.university_name + " (faculty_name text, full_name text)"
            )
            print('DB connected')
            # page - full code
            page = requests.get(self.start_url)
            # tree = lxml.html.parse('source.txt').getroot()  # DEBUG

            # make a lxml tree
            tree = lxml.html.fromstring(page.content)

            # search for trains by ccs
            faculty_res = tree.cssselect('div.blockone')
            print('Site loaded')
            # for each faculty
            for number, data in enumerate(faculty_res):
                print((number + 1)/len(faculty_res) * 100)
                self.progressed.emit((number + 1)/len(faculty_res) * 100)
                # strip - without spaces
                full_name = data.cssselect('div.fullname')[0].text.strip()
                url_name = data.cssselect('a.btn')[0].attrib['href'] + '/cathedras'
                temp_name = re.split('/|-', url_name)
                faculty_name = temp_name[len(temp_name) - 2]
                print(f'{full_name} - {faculty_name} ')
                self.db_connection.execute(
                    f"INSERT INTO {self.university_name} VALUES ('{faculty_name}', '{full_name}')"
                )
                self.db_connection.execute(
                    "CREATE TABLE " + faculty_name + " (cathedra_name text, full_name text)"
                )
                self.parse_cathedras(url_name, faculty_name)

            self.db_connection.commit()
            self.successful_exit = True

        except:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

        self.db_connection.close()
        self.finished.emit()

    def parse_cathedras(self, cur_url, faculty_name):
        # page - full code
        page = requests.get(cur_url)
        # tree = lxml.html.parse('source.txt').getroot()  # DEBUG

        # make a lxml tree
        tree = lxml.html.fromstring(page.content)

        # search for trains by ccs
        cathedras_res = tree.cssselect('div.blockone')

        # for each faculty
        for number, data in enumerate(cathedras_res):
            # strip - without spaces
            full_name = data.cssselect('div.fullname')[0].text.strip()
            url_name = data.cssselect('a.btn')[0].attrib['href']
            temp_name = re.split('/|-', url_name)
            cathedra_name = f'{faculty_name}_{temp_name[len(temp_name) - 1]}'
            print(f'{cathedra_name} - {full_name}')
            self.db_connection.execute(
                f"INSERT INTO {faculty_name} VALUES ('{cathedra_name}', '{full_name}')"
            )
            self.parse(url_name, cathedra_name)

        self.db_connection.commit()

    def parse(self, cur_url, cathedra_name):
        print(cathedra_name)

        # result = []
        ans = ''

        try:
            self.db_connection.execute("CREATE TABLE " + cathedra_name + " (number int, name text, science_role text, role text, phone text, email text, photo text)")

            if not os.path.exists(f'images/teacher_images/{cathedra_name}'):
                os.mkdir(f'images/teacher_images/{cathedra_name}')

            # page - full code
            page = requests.get(cur_url)
            # tree = lxml.html.parse('source.txt').getroot()  # DEBUG

            # make a lxml tree
            tree = lxml.html.fromstring(page.content)

            # search for trains by ccs
            teacher_res = tree.cssselect('div.facultyDeaneryOne')

            # for each teacher
            for number, data in enumerate(teacher_res, start=1):
                phone = '-'
                # strip - without spaces
                name = data.cssselect('div.deanLastName')[0].text_content().strip()

                try:
                    science_role = data.cssselect('div.deanScienceRole')[0].text.strip()
                except IndexError:
                    science_role = ''

                photo_raw = data.cssselect('div.deanPhoto')
                photo_style = photo_raw[0].attrib['style']

                # IMAGES
                # for url in re.findall(r'https?://\S+', photo_style):
                #     print(url[:-2])
                #     img = requests.get(url)
                #     img_file = open(f'images/teacher_images/{cathedra_name}/{number}.jpg', 'wb+')
                #     img_file.write(img.content)
                #     img_file.close()
                # /IMAGES

                role_raw = data.cssselect('div.deanRole')
                role = role_raw[0].text.strip()
                faculties = data.cssselect('a.nameSmall')
                for idx in range(len(faculties)):
                    faculties[idx] = faculties[idx].text.strip()
                # print(f'{faculties}')
                contacts = data.cssselect('a.btnSmall')
                email = ''
                for idx in range(1, len(contacts)):
                    contacts[idx] = contacts[idx].attrib['href']
                    if contacts[idx].find('mailto') != -1:
                        print(contacts[idx])
                        contacts[idx] = contacts[idx][7:-34]
                        email = contacts[idx]
                print(contacts)
                print(email)
                if email != '':
                    contacts.remove(email)
                if len(contacts) > 1:
                    phone = contacts[1]
                # print for debug
                ans += f'{number}: {name} {science_role} {role} {phone}\n'
                ans += '\n'
                # полная информация о преподавателе
                # teacher_info = {'number': number, 'name': name, 'science_role': science_role,
                #                 'role': role, 'phone': phone, 'image': f'images/teacher_images/{number}.jpg',
                #                 'email': email}

                self.db_connection.execute(
                    f"INSERT INTO {cathedra_name} VALUES ('{number}', '{name}', '{science_role}', '{role}', '{phone}', '{email}', 'images/teacher_images/{cathedra_name}/{number}.jpg')")

                # result.append(teacher_info)

        except sqlite3.OperationalError:
            print('already exists, rewrite!')
            sql_str = f'SELECT * FROM {cathedra_name}'
            # for row in self.db_connection.execute(sql_str):
            # result.append(row)

        print(ans)

        self.db_connection.commit()

        # return result


if __name__ == '__main__':
    worker = Worker()
    worker.parse_faculties()
