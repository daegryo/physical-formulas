import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import random

spravka2 = '''<p><b>Хотите потренировать навык решения задач? Это именно для вас.</p></b>

<p>Для того, чтобы начать решать задачи нажмите на кнопку <i>«Начать».</i>
<br>Далее появится текст задачи. В <i>окне для ввода</i> введите ответ.</br>
<br>Далее нажмите на кнопку <i>«Проверить»</i>, чтобы узнать правильный ответ и проверить свой.</p></br>
<br><i>По всем вопросам писать: yegorova082@yandex.ru</i></br>
'''

class Zadachi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('zadachides.ui', self)
        self.con = sqlite3.connect('data.sqlite')
        # Создание курсора
        self.cur = self.con.cursor()
        self.task = ''

        self.checkButton.clicked.connect(self.check)
        self.startButton.clicked.connect(self.start)
        self.startButton.setEnabled(True)
        self.checkButton.setEnabled(False)
        self.answerEdit.setEnabled(False)

    def start(self):
        self.answerEdit.setEnabled(True)
        self.startButton.setEnabled(False)
        self.checkButton.setEnabled(True)
        self.answerEdit.setStyleSheet(
            """
            border-width: 0px;
            font: 75 italic 12pt "Times New Roman";
background-color:rgb(255, 255, 255);
            """)
        self.startButton.setText('Следующая задача')
        num = random.randint(1, 10)
        self.task = self.cur.execute(f"""SELECT * FROM tasks
                                WHERE id = {num}""").fetchone()
        count = 0
        st = '<br>'
        note = []
        for i in range(len(self.task[1])):
            st += self.task[1][i]
            count += 1
            if count == 33:
                st += '</br>'
                note.append(st)
                count = 0
                st = '<br>'
            if len(self.task[1]) - i < 33:
                if i == len(self.task[1]) - 1:
                    st += '</br>'
                    note.append(st)
                    count = 0
                    st = '<br>'
        self.textLabel.setText(f'{"".join(note)}')

    def check(self):
        self.startButton.setEnabled(True)
        self.checkButton.setEnabled(False)
        self.answerEdit.setEnabled(False)
        right_answ = self.task[2]
        if str(right_answ) == self.answerEdit.text():
            self.rightLabel.setText('Верно!')
            self.answerEdit.setStyleSheet(
                    """border-style: outset;
                    border-width: 1px;
                    border-color: green;
                    font: 75 italic 12pt "Times New Roman";
background-color:rgb(255, 255, 255);""")
        else:
            self.rightLabel.setText(f'Неверно! Правильный ответ: {right_answ}')
            self.answerEdit.setStyleSheet(
                    """border-style: outset;
                    border-width: 1px;
                    border-color: red;
                    font: 75 italic 12pt "Times New Roman";
background-color:rgb(255, 255, 255);""")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F3:
            reply = QMessageBox.information(self, 'Информация о игре', spravka2, QMessageBox.Yes,
                                            QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Информация',
            'Вы уверены, что хотите закрыть решебник?',
            QMessageBox.Yes,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


