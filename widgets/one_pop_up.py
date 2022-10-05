from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# GUI FILE
from .ui_one_pop_up import Ui_Form


class OnePopUp(QWidget):
    def __init__(self):
        super(OnePopUp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
