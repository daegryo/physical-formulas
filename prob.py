import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Physic
from var import Var

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Prob(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('prob.ui', self)
        print("UI загружен успешно")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()


        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)
        self.backButton.clicked.connect(self.back)
        self.oneButton.clicked.connect(self.one)
        self.twoButton.clicked.connect(self.two)
        self.threeButton.clicked.connect(self.three)
        self.fourButton.clicked.connect(self.four)


    def back(self):
        from chose import Choose
        self.close()

        self.choose_form = Choose()
        self.choose_form.show()

    def one(self):
        self.close()
        self.var_form = Var(1)
        self.var_form.show()

    def two(self):
        self.close()
        self.var_form = Var(2)
        self.var_form.show()

    def three(self):
        self.close()
        self.var_form = Var(3)
        self.var_form.show()

    def four(self):
        self.close()
        self.var_form = Var(4)
        self.var_form.show()

    def five(self):
        self.close()
        self.var_form = Var(5)
        self.var_form.show()

    def six(self):
        self.close()
        self.var_form = Var(6)
        self.var_form.show()

    def seven(self):
        self.close()
        self.var_form = Var(7)
        self.var_form.show()

    def eight(self):
        self.close()
        self.var_form = Var(8)
        self.var_form.show()

    def nine(self):
        self.close()
        self.var_form = Var(9)
        self.var_form.show()

    def ten(self):
        self.close()
        self.var_form = Var(10)
        self.var_form.show()

