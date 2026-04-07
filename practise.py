import sys
import sqlite3
from tabnanny import check

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


from el1 import El1

from mech1 import Mech1
from mkt1 import Mkt1

from quant1 import Quant1


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)





class Practise(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('practise.ui', self)
        print("UI загружен успешно")

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()

        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)
        self.mechButton.clicked.connect(self.mech)
        self.elButton.clicked.connect(self.el)
        self.mktButton.clicked.connect(self.mkt)
        self.quantButton.clicked.connect(self.quant)
        self.backButton.clicked.connect(self.back)

    def mech(self):
        self.close()
        self.mech_form = Mech1()
        self.mech_form.show()

    def el(self):
        self.close()
        self.el_form = El1()
        self.el_form.show()

    def mkt(self):
        self.close()
        self.mkt_form = Mkt1()
        self.mkt_form.show()

    def quant(self):
        self.close()
        self.quant_form = Quant1()
        self.quant_form.show()

    def back(self):
        from chose import Choose
        self.close()

        self.choose_form = Choose()
        self.choose_form.show()









