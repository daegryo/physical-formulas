import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIcon, QFontMetrics
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy
from main import Physic
from practise import Practise
from prob import Prob
from theory import Theory
from openai import OpenAI


class Ask(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ask.ui', self)
        print("UI загружен успешно")

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")


        self.textLabel.setWordWrap(True)
        self.textLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.textLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.textLabel.setMinimumHeight(100)

        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)


        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )
        self.model_name = "openrouter/free"

        self.sendButton.clicked.connect(self.send)
        self.backButton.clicked.connect(self.back)

        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.adapt_text_size)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_timer.start(100)

    def adapt_text_size(self):
        if not self.textLabel.text():
            return

        font = self.textLabel.font()
        original_size = font.pointSize()

        for size in range(original_size, 7, -1):
            font.setPointSize(size)
            self.textLabel.setFont(font)

            self.textLabel.updateGeometry()
            QApplication.processEvents()

            metrics = QFontMetrics(font)
            text_rect = metrics.boundingRect(
                self.textLabel.rect(),
                Qt.TextWordWrap,
                self.textLabel.text()
            )

            if text_rect.height() <= self.textLabel.height():
                break

    def send(self):
        user_question = self.answerEdit.text()

        if not user_question.strip():
            QMessageBox.warning(self, "Внимание", "Пожалуйста, введите вопрос")
            return

        try:
            self.textLabel.setText("Думаю над ответом...")
            QApplication.processEvents()

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system",
                     "content": "Ты — эксперт по физике. Отвечай ТОЛЬКО на русском языке. Используй формулы где нужно."},
                    {"role": "user", "content": user_question}
                ],
                extra_body={
                    "transforms": ["middle-out"]
                }
            )

            answer = response.choices[0].message.content
            self.textLabel.setText(answer)

            self.adapt_text_size()

        except Exception as e:
            print(f"Ошибка: {e}")
            self.textLabel.setText(f"Ошибка: {e}")

    def back(self):
        from chose import Choose
        self.close()
        self.welcome_form = Choose()
        self.welcome_form.show()