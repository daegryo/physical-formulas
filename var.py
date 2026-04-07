import os
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, right
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from finish import Finish
from main import Physic


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Var(QMainWindow):
    def __init__(self, var):
        super().__init__()
        uic.loadUi('var.ui', self)
        print("UI загружен успешно")

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.var = var
        if self.var == 1:
            self.label.setText("  Пробный вариант ЕГЭ 2025 от ЕГКР В956 ")
        elif self.var == 2:
            self.label.setText("  Пробный вариант ЕГЭ 2025 от ЕГКР В955 ")
        elif self.var == 3:
            self.label.setText(" Вариант ЕГЭ 2025 | Основная волна резерв | Москва ")
        elif self.var == 4:
            self.label.setText("    Вариант ЕГЭ 2025 | Досрочная волна ")
        elif self.var == 5:
            self.label.setText("  Пробный вариант ЕГЭ 2026 от ЕГКР | Вариант 951 ")
        elif self.var == 6:
            self.label.setText(" Вариант ЕГЭ 2025 | Основная волна | Центральный округ ")
        elif self.var == 7:
            self.label.setText(" Вариант ЕГЭ 2025 | Основная волна | Юго-западный округ ")
        elif self.var == 8:
            self.label.setText(" Вариант ЕГЭ 2025 | Основная волна | Северо-западный округ ")
        elif self.var == 9:
            self.label.setText(" Вариант ЕГЭ 2025 | Основная волна | Северо-западный округ ")
        elif self.var == 10:
            self.label.setText(" Пробный вариант ЕГЭ 2026 от ЕГКР 18.12.25 | Вариант 952 ")

        self.result = self.cur.execute(f"""SELECT * FROM prob
                                                WHERE var= '{self.var}'""").fetchall()
        self.right_answers = []
        self.your_answers = ["-"] * 26
        for el in self.result:
            self.right_answers.append(el[3])
        self.k = 0
        self.num = self.k
        count = 0
        st = '<br>'
        note = []
        for i in range(len(self.result[self.k][2])):
            st += self.result[self.k][2][i]
            count += 1
            if self.num+1 != 5 and self.num+1 != 6 and self.num+1 != 18 and self.num+1 != 26 and self.num+1 != 21 and self.num+1 != 23 and self.num+1 != 18 and self.num+1 != 25 and self.num+1 != 14 and self.num+1 != 15:
                if count == 46:
                    st += '<br>'  # Исправлено: только <br> без /
                    note.append(st)
                    count = 0
                    st = ''
                if len(self.result[self.k][2]) - i < 46:  # Исправлено: self.count
                    if i == len(self.result[self.k][2]) - 1:
                        st += '<br>'  # Исправлено
                        note.append(st)
                        count = 0
                        st = ''
            else:
                if count == 65:
                    st += '<br>'  # Исправлено
                    note.append(st)
                    count = 0
                    st = ''
                if len(self.result[self.k][2]) - i < 65:  # Исправлено
                    if i == len(self.result[self.k][2]) - 1:
                        st += '<br>'  # Исправлено
                        note.append(st)
                        count = 0
                        st = ''

        self.textLabel.setText(f'{"".join(note)}')
        if self.num + 1 != 5 and self.num + 1 != 6 and self.num + 1 != 18 and self.num + 1 != 26 and self.num + 1 != 21 and self.num + 1 != 23 and self.num + 1 != 18 and self.num + 1 != 25 and self.num + 1 != 14 and self.num + 1 != 15:
            self.textLabel.setStyleSheet(
                """font: 14pt "Palatino Linotype";""")
        else:
            self.textLabel.setStyleSheet(
                """font: 10pt "Palatino Linotype";""")

        image_path = f"images/prob/{self.var}/{self.result[self.k][5]}"
        if os.path.exists(image_path) and self.result[self.k][5] != "0":
            self.pixmap_formulas = QPixmap(image_path)
            if not self.pixmap_formulas.isNull():
                self.photoLabel.setPixmap(self.pixmap_formulas)

                self.photoLabel.setScaledContents(True)
        else:
            self.pixmap_formulas = QPixmap("images/practise/mech/0.png")
            if not self.pixmap_formulas.isNull():
                self.photoLabel.setPixmap(self.pixmap_formulas)
                self.photoLabel.setScaledContents(True)
        self.answerEdit.setStyleSheet(
            """background-color: rgba(255, 255, 255);
                color: rgb(0, 0, 0);
                border-color: rgb(255, 255, 255);
                font: 63 14pt "Sitka Text Semibold";
                background-color: rgba(194, 194, 194, 100);
                border-radius: 3px;
                """)

        self.numLabel.setText(f"{self.k + 1}/{len(self.result)}")



        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)
        self.backButton.clicked.connect(self.back)
        self.nextButton.clicked.connect(self.next)
        self.flag = True
       # self.showButton.clicked.connect(self.sh)
        self.returnButton.clicked.connect(self.returnn)
     #   self.checkButton.clicked.connect(self.check)
        self.rememberButton.clicked.connect(self.remember)
        self.finishButton.clicked.connect(self.finish)

    def back(self):
        from prob import Prob
        self.close()
        self.practise_form = Prob()
        self.practise_form.show()

    def next(self):
        self.photoLabel.clear()
        self.decisionLabel.clear()
        self.answerEdit.clear()
        if self.k + 1 < 26 and self.flag:
            self.k += 1
            if self.your_answers[self.k] != "-":
                self.answerEdit.setText(self.your_answers[self.k])
            self.num = self.k
            if self.k <= len(self.result):
                self.numLabel.setText(f"{self.k+1}/{len(self.result)}")
            image_path = f"images/prob/{self.var}/{self.result[self.k][5]}"
            if os.path.exists(image_path) and self.result[self.k][5] != "0":
                self.pixmap_formulas = QPixmap(image_path)
                if not self.pixmap_formulas.isNull():
                    self.photoLabel.setPixmap(self.pixmap_formulas)
                    self.photoLabel.setScaledContents(True)
            else:
                self.pixmap_formulas = QPixmap("images/practise/mech/0.png")
                if not self.pixmap_formulas.isNull():
                    self.photoLabel.setPixmap(self.pixmap_formulas)
                    self.photoLabel.setScaledContents(True)
            count = 0
            st = '<br>'
            note = []
            for i in range(len(self.result[self.k][2])):
                st += self.result[self.k][2][i]
                count += 1
                if self.num+1 != 5 and self.num+1 != 6 and self.num+1 != 18 and self.num+1 != 26 and self.num+1 != 21 and self.num+1 != 23 and self.num+1 != 18 and self.num+1 != 25 and self.num+1 != 14 and self.num+1 != 15:
                    if count == 46:
                        st += '<br>'  # Исправлено: только <br> без /
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.k][2]) - i < 46:  # Исправлено: self.count
                        if i == len(self.result[self.k][2]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
                else:
                    if count == 65:
                        st += '<br>'  # Исправлено
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.k][2]) - i < 65:  # Исправлено
                        if i == len(self.result[self.k][2]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
            self.textLabel.setText(f'{"".join(note)}')

            if self.num+1 != 5 and self.num+1 != 6 and self.num+1 != 18 and self.num+1 != 26 and self.num+1 != 21 and self.num+1 != 23 and self.num+1 != 18 and self.num+1 != 25 and self.num+1 != 14 and self.num+1 != 15 and self.num+1 != 9 and self.num+1!=24:
                self.textLabel.setStyleSheet(
                    """font: 14pt "Palatino Linotype";""")
            else:

                self.textLabel.setStyleSheet(
                    """font: 11pt "Palatino Linotype";""")
            self.answerEdit.setStyleSheet(
                """background-color: rgba(255, 255, 255);
                    color: rgb(0, 0, 0);
                    border-color: rgb(255, 255, 255);
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(194, 194, 194, 100);
                    border-radius: 3px;
                    """)
    def returnn(self):
        self.decisionLabel.clear()
        self.answerEdit.clear()

        if self.k >=1 and self.flag:
            self.k -= 1
            if self.your_answers[self.k] != "-":
                self.answerEdit.setText(self.your_answers[self.k])
            self.num = self.k
            if self.k + 1 <= len(self.result):
                self.numLabel.setText(f"{self.k + 1}/{len(self.result)}")
            image_path = f"images/prob/{self.var}/{self.result[self.k][5]}"
            if os.path.exists(image_path) and self.result[self.k][5] != "0":
                self.pixmap_formulas = QPixmap(image_path)
                if not self.pixmap_formulas.isNull():
                    self.photoLabel.setPixmap(self.pixmap_formulas)
                    self.photoLabel.setScaledContents(True)
            else:
                self.pixmap_formulas = QPixmap("images/practise/mech/0.png")
                if not self.pixmap_formulas.isNull():
                    self.photoLabel.setPixmap(self.pixmap_formulas)
                    self.photoLabel.setScaledContents(True)
            count = 0
            st = '<br>'
            note = []
            for i in range(len(self.result[self.k][2])):
                st += self.result[self.k][2][i]
                count += 1
                if self.num+1 != 5 and self.num+1 != 6 and self.num+1 != 18 and self.num+1 != 26 and self.num+1 != 21 and self.num+1 != 23 and self.num+1 != 18 and self.num+1 != 25 and self.num+1 != 14 and self.num+1 != 15:
                    if count == 46:
                        st += '<br>'  # Исправлено: только <br> без /
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.k][2]) - i < 46:  # Исправлено: self.count
                        if i == len(self.result[self.k][2]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
                else:
                    if count == 65:
                        st += '<br>'  # Исправлено
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.k][2]) - i < 65:  # Исправлено
                        if i == len(self.result[self.k][2]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
            self.textLabel.setText(f'{"".join(note)}')

            if self.num+1 != 5 and self.num+1 != 6 and self.num+1 != 18 and self.num+1 != 26 and self.num+1 != 21 and self.num+1 != 23 and self.num+1 != 18 and self.num+1 != 25 and self.num+1 != 14 and self.num+1 != 15:
                self.textLabel.setStyleSheet(
                    """font: 14pt "Palatino Linotype";""")
            else:

                self.textLabel.setStyleSheet(
                    """font: 10pt "Palatino Linotype";""")
            self.answerEdit.setStyleSheet(
                """background-color: rgba(255, 255, 255);
                    color: rgb(0, 0, 0);
                    border-color: rgb(255, 255, 255);
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(194, 194, 194, 100);
                    border-radius: 3px;
                    """)
    def remember(self):
        st=self.answerEdit.text()
        removee = self.your_answers.pop(self.k)
        self.your_answers.insert(self.k, st)



    def finish(self):
        self.finish_form = Finish(self.your_answers, self.right_answers, self.result, self.var, self)
        self.finish_form.show()
        self.hide()

