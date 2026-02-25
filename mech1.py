import os
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, right
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import Physic


try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Mech1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mech1.ui', self)
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
        self.checkButton.clicked.connect(self.check)

        self.result = self.cur.execute(f"""SELECT * FROM mech1
                                                WHERE number= '{1}'""").fetchall()
        self.flag = False
        self.count = 0
        self.counter = 0
        count = 0
        st = '<br>'
        note = []
        for i in range(len(self.result[self.count][1])):
            st += self.result[self.count][1][i]
            count += 1

            if count == 46:
                st += '<br>'  # Исправлено: только <br> без /
                note.append(st)
                count = 0
                st = ''
            if len(self.result[self.count][1]) - i < 46:  # Исправлено: self.count
                if i == len(self.result[self.count][1]) - 1:
                    st += '<br>'  # Исправлено
                    note.append(st)
                    count = 0
                    st = ''

        self.textLabel.setText(f'{"".join(note)}')
        self.decisionLabell.setText("")
        self.decisionLabell.setStyleSheet(
            """
                """)
        self.textLabel.setStyleSheet(
            """font: 14pt "Palatino Linotype";""")
        image_path = f"images/practise/mech/{self.result[0][4]}"
        if os.path.exists(image_path) and self.result[0][4] != "0":
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





    def back(self):
        from practise import Practise
        self.close()

        self.practise_form = Practise()
        self.practise_form.show()

    def sh(self):
        self.decisionLabell.setText("")
        self.decisionLabell.setStyleSheet(
            """
                """)
        self.decisionLabel.clear()
        self.answerEdit.clear()
        self.rightLabel.setText("")
        self.count = 0
        self.flag = True
        self.parameter = self.comboBox.currentText()
        if self.parameter == "Задание 1":
            self.num = 1
        elif self.parameter == "Задание 2":
            self.num = 2
        elif self.parameter == "Задание 3":
            self.num = 3
        elif self.parameter == "Задание 4":
            self.num = 4
        elif self.parameter == "Задание 5":
            self.num = 5
        elif self.parameter == "Задание 6":
            self.num = 6
        elif self.parameter == "Задание 18":
            self.num = 18
        elif self.parameter == "Задание 22":
            self.num = 22
        elif self.parameter == "Задание 26":
            self.num = 26
        self.result = self.cur.execute(f"""SELECT * FROM mech1
                                        WHERE number= '{self.num}'""").fetchall()
        self.counter = len(self.result)
        self.numLabel.setText(f"{self.count + 1}/{len(self.result)}")


        count = 0
        st = '<br>'
        note = []
        for i in range(len(self.result[self.count][1])):
            st += self.result[self.count][1][i]
            count += 1
            if self.num != 5 and self.num!=6 and self.num != 18 and self.num != 26:
                if count == 46:
                    st += '<br>'  # Исправлено: только <br> без /
                    note.append(st)
                    count = 0
                    st = ''
                if len(self.result[self.count][1]) - i < 46:  # Исправлено: self.count
                    if i == len(self.result[self.count][1]) - 1:
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
                if len(self.result[self.count][1]) - i < 65:  # Исправлено
                    if i == len(self.result[self.count][1]) - 1:
                        st += '<br>'  # Исправлено
                        note.append(st)
                        count = 0
                        st = ''

        self.textLabel.setText(f'{"".join(note)}')
        if self.num != 5 and self.num!=6  and self.num != 18 and self.num != 26:
            self.textLabel.setStyleSheet(
                """font: 14pt "Palatino Linotype";""")
        else:
            self.textLabel.setStyleSheet(
                """font: 10pt "Palatino Linotype";""")



        image_path = f"images/practise/mech/{self.result[0][4]}"
        if os.path.exists(image_path) and self.result[0][4] != "0":
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


    def next(self):
        self.decisionLabell.setText("")
        self.decisionLabell.setStyleSheet(
            """
                """)
        self.decisionLabel.clear()
        self.answerEdit.clear()
        self.rightLabel.setText("")

        if self.count < self.counter and self.flag:
            self.count += 1
            if self.count + 1 <= len(self.result):
                self.numLabel.setText(f"{self.count + 1}/{len(self.result)}")
            image_path = f"images/practise/mech/{self.result[self.count][4]}"
            if os.path.exists(image_path) and self.result[self.count][4] != "0":
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
            for i in range(len(self.result[self.count][1])):
                st += self.result[self.count][1][i]
                count += 1
                if self.num != 5 and self.num!=6  and self.num != 18 and self.num != 26:
                    if count == 46:
                        st += '<br>'  # Исправлено: только <br> без /
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.count][1]) - i < 46:  # Исправлено: self.count
                        if i == len(self.result[self.count][1]) - 1:
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
                    if len(self.result[self.count][1]) - i < 65:  # Исправлено
                        if i == len(self.result[self.count][1]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
            self.textLabel.setText(f'{"".join(note)}')

            if self.num != 5 and self.num!=6  and self.num != 18 and self.num != 26:
                self.textLabel.setStyleSheet(
                    """font: 14pt "Palatino Linotype";""")
            else:

               # self.textLabel.adjustSize()
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

    def returnn(self):
        self.decisionLabell.setText("")
        self.decisionLabell.setStyleSheet(
            """
                """)
        self.decisionLabel.clear()
        self.answerEdit.clear()
        self.rightLabel.setText("")

        if self.count>=1 and self.flag:
            self.count -= 1
            if self.count != len(self.result):
                self.numLabel.setText(f"{self.count + 1}/{len(self.result)}")
            image_path = f"images/practise/mech/{self.result[self.count][4]}"
            if os.path.exists(image_path) and self.result[self.count][4] != "0":
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
            for i in range(len(self.result[self.count][1])):
                st += self.result[self.count][1][i]
                count += 1
                if self.num != 5 and self.num!=6  and self.num != 18 and self.num != 26:
                    if count == 46:
                        st += '<br>'  # Исправлено: только <br> без /
                        note.append(st)
                        count = 0
                        st = ''
                    if len(self.result[self.count][1]) - i < 46:  # Исправлено: self.count
                        if i == len(self.result[self.count][1]) - 1:
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
                    if len(self.result[self.count][1]) - i < 65:  # Исправлено
                        if i == len(self.result[self.count][1]) - 1:
                            st += '<br>'  # Исправлено
                            note.append(st)
                            count = 0
                            st = ''
            self.textLabel.setText(f'{"".join(note)}')
            if self.num != 5 and self.num!=6  and self.num != 18 and self.num != 26:
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
    def check(self):
        right_answ = self.result[self.count][2]
        self.rightLabel.setText(right_answ)
       # self.decisionLabel.wordWrap()
        if str(right_answ) == self.answerEdit.text():
            self.answerEdit.setStyleSheet(
                """background-color: rgba(255, 255, 255);
                    color: rgb(0, 0, 0);
                    border-color: rgb(255, 255, 255);
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(110, 175, 13, 100);;
                    border-radius: 3px;
                    """)
        else:
            self.answerEdit.setStyleSheet(
                """background-color: rgba(255, 255, 255);
                    color: rgb(0, 0, 0);
                    border-color: rgb(255, 255, 255);
                    font: 63 14pt "Sitka Text Semibold";
                    background-color: rgba(181, 0, 0, 100);
                    border-radius: 3px;
                    """)
        if self.num == 22 or self.num == 26:
            self.decisionLabell.setText("Решение")
            self.decisionLabell.setStyleSheet(
                """background-color: rgba(255, 255, 255);
                color: rgb(0, 0, 0);
                font: 63 14pt "Sitka Text Semibold";
                border-radius: 20px;

                border-width:3px;
                border-style: solid;
                border-color:rgb(222, 177, 14);
                    """)
            image_path = f"images/practise/mech/decision/{self.result[self.count][5]}"
            if os.path.exists(image_path) and self.result[self.count][5] != "0":
                self.pixmap_decision = QPixmap(image_path)
                if not self.pixmap_formulas.isNull():
                    self.decisionLabel.setPixmap(self.pixmap_decision)
                    self.decisionLabel.setScaledContents(True)










