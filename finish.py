import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Physic

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Finish(QMainWindow):
    def __init__(self, your_answers, right_answers, results, var, form):
        super().__init__()
        uic.loadUi('prov.ui', self)
        print("UI загружен успешно")

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.your_answers = your_answers
        self.right_answers = right_answers
        self.result = results
        self.var = var
        self.form = form

        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)

        self.y1.setText(str(self.your_answers[0]))
        self.r1.setText(str(self.right_answers[0]))
        self.y2.setText(str(self.your_answers[1]))
        self.r2.setText(str(self.right_answers[1]))
        self.y3.setText(str(self.your_answers[2]))
        self.r3.setText(str(self.right_answers[2]))
        self.y4.setText(str(self.your_answers[3]))
        self.r4.setText(str(self.right_answers[3]))
        self.y5.setText(str(self.your_answers[4]))
        self.r5.setText(str(self.right_answers[4]))
        self.y6.setText(str(self.your_answers[5]))
        self.r6.setText(str(self.right_answers[5]))
        self.y7.setText(str(self.your_answers[6]))
        self.r7.setText(str(self.right_answers[6]))
        self.y8.setText(str(self.your_answers[7]))
        self.r8.setText(str(self.right_answers[7]))
        self.y9.setText(str(self.your_answers[8]))
        self.r9.setText(str(self.right_answers[8]))
        self.y10.setText(str(self.your_answers[9]))
        self.r10.setText(str(self.right_answers[9]))
        self.y11.setText(str(self.your_answers[10]))
        self.r11.setText(str(self.right_answers[10]))
        self.y12.setText(str(self.your_answers[11]))
        self.r12.setText(str(self.right_answers[11]))
        self.y13.setText(str(self.your_answers[12]))
        self.r13.setText(str(self.right_answers[12]))
        self.y14.setText(str(self.your_answers[13]))
        self.r14.setText(str(self.right_answers[13]))
        self.y15.setText(str(self.your_answers[14]))
        self.r15.setText(str(self.right_answers[14]))
        self.y16.setText(str(self.your_answers[15]))
        self.r16.setText(str(self.right_answers[15]))
        self.y17.setText(str(self.your_answers[16]))
        self.r17.setText(str(self.right_answers[16]))
        self.y18.setText(str(self.your_answers[17]))
        self.r18.setText(str(self.right_answers[17]))
        self.y19.setText(str(self.your_answers[18]))
        self.r19.setText(str(self.right_answers[18]))
        self.y20.setText(str(self.your_answers[19]))
        self.r20.setText(str(self.right_answers[19]))
        self.y21.setText(str(self.your_answers[20]))
        self.r21.setText(str(self.right_answers[20]))
        self.y22.setText(str(self.your_answers[21]))
        self.r22.setText(str(self.right_answers[21]))
        self.y23.setText(str(self.your_answers[22]))
        self.r23.setText(str(self.right_answers[22]))
        self.y24.setText(str(self.your_answers[23]))
        self.r24.setText(str(self.right_answers[23]))
        self.y25.setText(str(self.your_answers[24]))
        self.r25.setText(str(self.right_answers[24]))
        self.y26.setText(str(self.your_answers[25]))
        self.r26.setText(str(self.right_answers[25]))
        if self.right_answers[0] == self.your_answers[0]:
            self.y1.setStyleSheet("""
                                    font: 63 14pt "Sitka Text Semibold";
                                    background-color: rgba(45, 143, 34, 100);
                                    color: rgb(0, 0, 0);
                                    border-radius: 20px;
                                """)
        else:
            self.y1.setStyleSheet("""
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(145, 0, 0,100);
                    color: rgb(0, 0, 0);
                    border-radius: 20px;
                                            """)
        if self.right_answers[1] == self.your_answers[1]:
            self.y2.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y2.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[2] == self.your_answers[2]:
            self.y3.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y3.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[3] == self.your_answers[3]:
            self.y4.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y4.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[4] == self.your_answers[4]:
            self.y5.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y5.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[5] == self.your_answers[5]:
            self.y6.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y6.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[6] == self.your_answers[6]:
            self.y7.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y7.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[7] == self.your_answers[7]:
            self.y8.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y8.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[8] == self.your_answers[8]:
            self.y9.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y9.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[9] == self.your_answers[9]:
            self.y10.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y10.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[10] == self.your_answers[10]:
            self.y11.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y11.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[11] == self.your_answers[11]:
            self.y12.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y12.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[12] == self.your_answers[12]:
            self.y13.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y13.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[13] == self.your_answers[13]:
            self.y14.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y14.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[14] == self.your_answers[14]:
            self.y15.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y15.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[15] == self.your_answers[15]:
            self.y16.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y16.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[16] == self.your_answers[16]:
            self.y17.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y17.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[17] == self.your_answers[17]:
            self.y18.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y18.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[18] == self.your_answers[18]:
            self.y19.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y19.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)
        if self.right_answers[19] == self.your_answers[19]:
            self.y20.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
        else:
            self.y20.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                                                   """)

        # self.text = self.comboBox.currentText()
        # self.theoryButton.clicked.connect(self.theory)
        self.backButton.clicked.connect(self.back)
        self.nextButton.clicked.connect(self.next)
        self.checkButton.clicked.connect(self.check)
        self.returnButton.clicked.connect(self.returnn)
        self.count = 20

        self.pixmap_krit = QPixmap("images/prob/krit/21.png")
        self.kritLabel.setPixmap(self.pixmap_krit)
        self.kritLabel.setScaledContents(True)
        self.pixmap_photo = QPixmap(f"images/prob/{self.var}/decision/{self.result[self.count][6]}")
        self.photoLabel.setPixmap(self.pixmap_photo)
        self.photoLabel.setScaledContents(True)

        self.flag = False
        self.counter = 0

    def back(self):
        self.form.show()
        self.close()

    def next(self):
        if self.count < 26:
            self.count += 1
            self.pixmap_krit = QPixmap(f"images/prob/krit/{self.count + 1}.png")
            self.kritLabel.setPixmap(self.pixmap_krit)
            self.kritLabel.setScaledContents(True)
            self.pixmap_photo = QPixmap(f"images/prob/{self.var}/decision/{self.result[self.count][6]}")
            self.photoLabel.setPixmap(self.pixmap_photo)
            self.photoLabel.setScaledContents(True)

    def returnn(self):
        if self.count > 20:
            self.count -= 1
            self.pixmap_krit = QPixmap(f"images/prob/krit/{self.count + 1}.png")
            self.kritLabel.setPixmap(self.pixmap_krit)
            self.kritLabel.setScaledContents(True)
            self.pixmap_photo = QPixmap(f"images/prob/{self.var}/decision/{self.result[self.count][6]}")
            self.photoLabel.setPixmap(self.pixmap_photo)
            self.photoLabel.setScaledContents(True)

    def check(self):
        st = self.answerEdit.text()
        if self.count + 1 == 21:
            if st == "0":
                self.y21.setStyleSheet("""
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(145, 0, 0,100);
                    color: rgb(0, 0, 0);
                    border-radius: 20px;
                """)
            elif st == "3":
                self.y21.setStyleSheet("""
                                    font: 63 14pt "Sitka Text Semibold";
                                    background-color: rgba(45, 143, 34, 100);
                                    color: rgb(0, 0, 0);
                                    border-radius: 20px;
                                """)
            else:
                self.y21.setStyleSheet("""
                                    font: 63 14pt "Sitka Text Semibold";
                                    background-color: rgba(211, 205, 29, 100);
                                    color: rgb(0, 0, 0);
                                    border-radius: 20px;
                                    """)
        if self.count + 1 == 24:
            if st == "0":
                self.y24.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                       """)
            elif st == "3":
                self.y24.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
            else:
                self.y24.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(211, 205, 29, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                           """)
        if self.count + 1 == 25:
            if st == "0":
                self.y25.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                       """)
            elif st == "3":
                self.y25.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
            else:
                self.y25.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(211, 205, 29, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                           """)
        if self.count + 1 == 22:
            if st == "0":
                self.y22.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                       """)
            elif st == "2":
                self.y22.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
            else:
                self.y22.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(211, 205, 29, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                           """)
        if self.count + 1 == 23:
            if st == "0":
                self.y23.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                       """)
            elif st == "2":
                self.y23.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
            else:
                self.y23.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(211, 205, 29, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                           """)
        if self.count + 1 == 26:
            if st == "0":
                self.y26.setStyleSheet("""
                           font: 63 14pt "Sitka Text Semibold";
                           background-color: rgba(145, 0, 0,100);
                           color: rgb(0, 0, 0);
                           border-radius: 20px;
                       """)
            elif st == "4":
                self.y26.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(45, 143, 34, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                       """)
            else:
                self.y26.setStyleSheet("""
                                           font: 63 14pt "Sitka Text Semibold";
                                           background-color: rgba(211, 205, 29, 100);
                                           color: rgb(0, 0, 0);
                                           border-radius: 20px;
                                           """)
