import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from game import GameForRemember
from zadachi import Zadachi
try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

ERRORZN = '''!@#$%^&*()_+|[]{}:;",<.>/?№;:?*-='''
RUS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю'
LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmρ'
POST = {'g': 9.8, 'G': 6.67 * 10 ** -11}
spravka = f'''<p><u><b>Добро пожаловать в калькулятор физических формул!</b></u></p>
<p>
Он поможет тебе в решении <u><i>физических задач.</i></u>
Для того, чтобы правильно использовать данное приложение, нужно:</p>
<p>
<i>1.	Выбрать из выпадающего списка <u>переменную, которую нужно найти</u>, исходя из условия задачи
<p> 
2.	Нажать кнопку <u>«Показать»</u></p>
<p> 
3.	На экране отобразятся представление формулы, переменные из которых она состоит, окна, в которые нужно 
<u>вписать значение этих переменных</u>, значения в системе интернациональной тех же переменных</p> 
<p> 
4.	Далее нужно нажать на кнопку <u>«Получить результат»</u></p> 
<p> 
5.	На экране отобразится результат вида:
<u>переменная, которую нужно найти</u> = <u>результат</u>, <u>его значение по СИ</u> </i></p>
По вопросам писать: <u>yegorova082@yandex.ru</u>
'''

helpp = '''1.   Для общей информации о программе 
      нажмите F1 в главном окне;
2.  Для информации об игре 
     нажмите F2 в окне игры;
3.  Для информации о задаче
     нажмите F3 в окне задач;
Чтобы скрыть данный текст нажмите
 еще раз на кнопку "Помощь"
'''


class Physic(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('des.ui', self)
        self.con = sqlite3.connect('data.sqlite')

        # Создание курсора
        self.cur = self.con.cursor()
        self.zn1.setEnabled(False)
        self.zn2.setEnabled(False)
        self.zn3.setEnabled(False)
        self.zn4.setEnabled(False)
        self.zn5.setEnabled(False)
        self.zn6.setEnabled(False)

        self.lst = [self.zn1, self.zn2, self.zn3, self.zn4, self.zn5, self.zn6]
        self.note = [self.let1, self.let2, self.let3, self.let4, self.let5, self.let6]
        self.spisok = [self.si1, self.si2, self.si3, self.si4, self.si5, self.si6]
        self.result = ''
        self.parameter = ''
        self.pixmap = QPixmap('pictures/welcome.jpg')
        self.photoLabel.setPixmap(self.pixmap)
        self.count = 0
        self.chet = 0

        self.showButtton.clicked.connect(self.sh)
        self.resultButton.clicked.connect(self.res)
        self.gameButton.clicked.connect(self.game)
        self.zadachiButton.clicked.connect(self.zadachi)
        self.helpButton.clicked.connect(self.help)

    def sh(self):
        self.parameter = self.comboBox.currentText()
        self.result = self.cur.execute(f"""SELECT * FROM physic
                                WHERE title = '{self.parameter}'""").fetchone()
        self.count = 0
        for i in range(3, 8):
            if self.result[i] != '0':
                self.count += 1
        for i in range(self.count):
            if self.result[i + 3].split()[0] == '0':
                break
            self.note[i].setText(self.result[i + 3].split()[0])
            if self.note[i].text()[0] in POST.keys():
                self.lst[i].setEnabled(False)
                self.lst[i].setText(str(POST[self.note[i].text()]))
            else:
                self.lst[i].setEnabled(True)
            self.spisok[i].setText(self.result[i + 3].split()[1])
            self.pixmap = QPixmap(self.result[9])
            self.photoLabel.setPixmap(self.pixmap)

    def res(self):
        try:
            for i in range(self.count):
                self.lst[i].setStyleSheet(
                    """border-width: 0px;
                    font: 75 italic 12pt "Times New Roman";
background-color:rgb(255, 255, 255);""")
            try:
                print(self.result[2].split())
                vyraz = self.result[2].split()
                for i in range(len(vyraz)):
                    if vyraz[i] in LETTERS:
                        for j in range(len(self.note)):
                            if self.note[j].text() == vyraz[i]:
                                vyraz[i] = self.lst[j].text()
                try:
                    res = round(eval(' '.join(vyraz)), 2)
                    print(res)
                    self.resultLabel.setText(f'<b>{self.parameter} = {res} {self.result[10]}</b>')
                    file = open('histor.txt', mode='a')
                    file.write(f'\n Найти: {self.result[1]}\n По формуле {self.result[2]},\n {res} = {" ".join(vyraz)},'
                               f'\n {self.parameter} = {res} {self.result[10]}')
                except SyntaxError:
                    self.resultLabel.setText(
                        f'<b>Некоторые поля оказалисть пустыми <br>или введен неправильный тип данных</b></br>')
                    for i in range(self.count):
                        if self.lst[i].text() == '' or self.lst[i].text() in ERRORZN:
                            self.lst[i].setStyleSheet(
                                """border-style: outset;
                                border-width: 1px;
                                border-color: red;
                                font: 75 italic 12pt "Times New Roman";
                                background-color:rgb(255, 255, 255);""")
            except IndexError:
                self.resultLabel.setText(f'<b>Вы нажали кнопку <br>"Получить результат" до "Показать"</br></b>')

            except NameError:
                self.resultLabel.setText(f'<b>Введен неправильный тип данных</b>')
                for i in range(self.count):
                    if self.lst[i].text() in RUS or self.lst[i].text() in LETTERS:
                        self.lst[i].setStyleSheet(
                            """border-style: outset;
                            border-width: 1px;
                            border-color: red;
                            font: 75 italic 12pt "Times New Roman";
                            background-color:rgb(255, 255, 255);""")

        except AttributeError:
            self.resultLabel.setText(f'<b>Вы нажали кнопку <br>"Получить результат" до "Показать"</br></b>')

    def game(self):
        self.game_form = GameForRemember()
        self.game_form.show()

    def zadachi(self):
        self.zadachi_form = Zadachi()
        self.zadachi_form.show()

    def help(self):
        self.chet += 1
        if self.chet % 2 != 0:
            self.helpLabel.setText(helpp)
        else:
            self.helpLabel.setText('')

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Информация',
            'Вы уверены, что хотите закрыть калькулятор формул?',
            QMessageBox.Yes,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            reply = QMessageBox.information(self, 'Информация по использованию', spravka, QMessageBox.Yes,
                                            QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Physic()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
