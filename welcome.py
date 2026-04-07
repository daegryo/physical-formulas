import torch
import multiprocessing
import sys
import sqlite3
from venSpeakerPy import lib_speak
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from chose import Choose


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome.ui', self)
        print("UI загружен успешно")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.pixmap = QPixmap("images/logo.jpg")
        self.photoLabel.setPixmap(self.pixmap)

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")



        self.pushButton.clicked.connect(self.sh)
        self.setup_animation()
        self.setGeometry(0, 0, 3000, 1000)

    def setup_animation(self):
        try:
            self.animation = QPropertyAnimation(self.photoLabel, b"pos")
            self.animation.setDuration(2000)  # 2 секунды
            self.animation.setStartValue(self.photoLabel.pos())
            end_pos = self.photoLabel.pos() + QPoint(350, 0)
            self.animation.setEndValue(end_pos)
            self.animation.setEasingCurve(QEasingCurve.InOutQuad)
            self.animation.start()
        except Exception as e:
            print(f"Ошибка анимации: {e}")

    def sh(self):
        self.main_form = Choose()
        self.main_form.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    multiprocessing.freeze_support()
    form = Welcome()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())