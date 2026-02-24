import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Physic
from theory import Theory


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Choose(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('choose.ui', self)
        print("UI загружен успешно")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()


        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)

        self.theoryButton.clicked.connect(self.theory)
        self.backButton.clicked.connect(self.back)


    def theory(self):
        self.close()
        self.main_form = Theory()
        self.main_form.show()

    def back(self):
        from welcome import Welcome
        self.close()

        self.welcome_form = Welcome()
        self.welcome_form.show()






