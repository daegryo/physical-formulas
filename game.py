import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox

# отредактировать, чтобы красиво было
LET = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmρ'
spravka1 = '''<p><b>Хочешь выучить формулы по физике, но не знаешь как? Эта игра для запоминания тебе поможет!</b>
<br>В ней ты сможешь подучить все формулы как для сдачи ОГЭ по физике, так и просто для себя.</br><p>
<p>Интерфейс игры прост и понятен. Для старта нажимаешь кнопку <i>«Начать».</i>
<br>На экране высвечивается название формулы, формулы с пропуском в виде <i>«?»</i> и три варианта ответа, из которых правильный только один.</br>
<br>Чтобы проверить верную ли ты букву выбрал, нужно нажать на кнопку <i>«Проверить»</i>.</br>
<br>При нажатии каждый из вариантов ответов поменяет цвет.</br>
<br>Если правильный, то зеленый, если неправильный, то красный.</br> 
<br>Для продолжения игры нажмите на кнопку <i>«Следующая формула».</i></br> 
<br>Так же имеется счетчик. С помощью него вы сможете отследить сколько формул вы знаете на данный момент.</br></p>
<br><i>По всем вопросам писать: yegorova082@yandex.ru</i></br>
'''


class GameForRemember(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gamedes.ui', self)

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()
        self.formulaEdit.setEnabled(False)
        self.index = ''
        self.radiobuttons = [self.v1Button, self.v2Button, self.v3Button]
        self.checkButton.setEnabled(False)

        self.nextButton.clicked.connect(self.next)
        self.checkButton.clicked.connect(self.check)

    def next(self):
        for i in range(3):
            self.radiobuttons[i].setStyleSheet(
                """border-width: 0px;font: italic 14pt "Times New Roman";""")
        if self.nextButton.text() == 'Начать':
            self.countLabel.setText('очки: 0')
        self.nextButton.setEnabled(False)
        self.checkButton.setEnabled(True)
        self.nextButton.setText('Следующая формула')
        # все формулы что есть
        self.znachen = self.cur.execute("SELECT znach FROM physic").fetchall()
        # выбираем одну
        formula = random.choice(self.znachen)
        form = list(formula)
        search = ''.join(form)
        self.title = self.cur.execute(f"""SELECT title FROM physic
                                               WHERE znach = '{search}'""").fetchone()[0]
        count = 0
        st = '<br>'
        note = []
        for i in range(len(self.title)):
            st += self.title[i]
            count += 1
            if count == 21:
                st += '</br>'
                note.append(st)
                count = 0
                st = '<br>'
            if len(self.title) - i < 21:
                if i == len(self.title) - 1:
                    st += '</br>'
                    note.append(st)
                    count = 0
                    st = '<br>'
        self.titleLabel.setText(f'{"".join(note)}')
        # промежуточный список
        prom = []
        # выбираем все буквы
        for el in form[0]:
            if el in LET:
                prom.append(el)
        # выбираем одну букву из списка букв
        right_var = random.choice(prom)
        newform = ''
        # замена этой буквы на ?
        for i in range(len(form[0])):
            if form[0][i] == right_var:
                newform += '?'
            else:
                newform += form[0][i]
        # меняем текст в formulaEdit
        self.formulaEdit.setText(newform)
        newrand = random.choices(LET, k=2)
        # составляем значения кнопок
        # добавляем правильный вариант
        newrand.append(right_var)
        newrandomlst = newrand
        # перемешиваем ответы
        random.shuffle(newrandomlst)
        for i in range(3):
            if right_var == newrandomlst[i]:
                self.index = i
            if newrandomlst[i] == '0':
                random_let = random.choice(LET)
                newrandomlst[i] = random_let
        # меняем текст кнопок
        self.v1Button.setText(newrandomlst[0])
        self.v2Button.setText(newrandomlst[1])
        self.v3Button.setText(newrandomlst[2])

    def check(self):
        self.nextButton.setEnabled(True)
        self.checkButton.setEnabled(False)
        if self.radiobuttons[self.index].isChecked():
            text_int = int(self.countLabel.text().split()[-1]) + 1
            self.countLabel.setText(f'очки: {text_int}')
        for i in range(3):
            if i != self.index:
                self.radiobuttons[i].setStyleSheet(
                    """border-style: outset;
                    border-width: 1px;
                    border-color: red;
                    font: italic 14pt "Times New Roman";""")
            else:
                self.radiobuttons[i].setStyleSheet(
                    """border-style: outset;
                    border-width: 1px;
                    border-color: green;
                    font: italic 14pt "Times New Roman";""")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F2:
            reply = QMessageBox.information(self, 'Информация о игре', spravka1, QMessageBox.Yes,
                                            QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Информация',
            'Вы уверены, что хотите закрыть игру для запоминания?',
            QMessageBox.Yes,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
