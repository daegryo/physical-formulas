import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Physic


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Quant(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('quant.ui', self)
        print("UI загружен успешно")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()


        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)
        self.text = self.comboBox.currentText()
       # self.theoryButton.clicked.connect(self.theory)
        self.backButton.clicked.connect(self.back)
        self.nextButton.clicked.connect(self.next)
        self.showButton.clicked.connect(self.sh)
        self.returnButton.clicked.connect(self.returnn)

        with open(f"theory/quant/1.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            self.textLabel.setText(text)
            self.textLabel.setStyleSheet(
                """font: 13pt "Palatino Linotype";""")
            self.textLabel.setTextFormat(Qt.RichText)
        self.pixmap_formulas = QPixmap(f"images/theory/quant/1/0.png")
        self.photoLabel.setPixmap(self.pixmap_formulas)


        self.flag = False
        self.count = 0
        self.counter = 0



    def back(self):
        from theory import Theory
        self.close()

        self.theory_form = Theory()
        self.theory_form.show()

    def sh(self):
        self.count = 0
        self.flag = True
        self.parameter = self.comboBox.currentText()
        self.result = self.cur.execute(f"""SELECT * FROM quant
                                        WHERE name = '{self.parameter}'""").fetchone()
        if self.parameter == "Корпускулярно-волновой дуализм":
            self.counter = 4
        elif self.parameter == "Физика атома":
            self.counter = 1
        elif self.parameter == "Физика атомного ядра":
            self.counter = 1



        with open(f"theory/quant/{self.result[1]}", 'r', encoding='utf-8') as file:
            text = file.read()
            self.textLabel.setText(text)
            self.textLabel.setStyleSheet(
                """font: 13pt "Palatino Linotype";""")
        self.pixmap_formulas = QPixmap(f"images/theory/quant/{self.result[2]}/{self.count}.png")
        self.photoLabel.setPixmap(self.pixmap_formulas)
        self.photoLabel.setScaledContents(True)

    def next(self):
        if self.count < self.counter and self.flag:
            self.count += 1
            self.pixmap_formulas = QPixmap(f"images/theory/quant/{self.result[2]}/{self.count}.png")
            self.photoLabel.setPixmap(self.pixmap_formulas)
            self.photoLabel.setScaledContents(True)

    def returnn(self):
        if self.count>=1 and self.flag:
            self.count -= 1
            self.pixmap_formulas = QPixmap(f"images/theory/quant/{self.result[2]}/{self.count}.png")
            self.photoLabel.setPixmap(self.pixmap_formulas)
            self.photoLabel.setScaledContents(True)







