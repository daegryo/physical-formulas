import sys
import sqlite3
import os
import threading
import queue
import numpy as np

try:
    from venSpeakerPy import lib_speak
    import sounddevice as sd
    TTS_AVAILABLE = True
    print("TTS инициализирован успешно")
except ImportError:
    TTS_AVAILABLE = False
    print("Установите: pip install venSpeakerPy sounddevice")

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton



try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping






def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Mech(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mech.ui', self)
        print("UI загружен успешно")

        self.setWindowIcon(QIcon("images/logo_small.png"))
        self.setWindowTitle("СмартЕгэ")

        self.con = sqlite3.connect('data.sqlite')
        self.cur = self.con.cursor()

        self.is_playing = False
        self.stop_playback_flag = False

        self.speed = 1.0


        self.setGeometry(0, 0, 3000, 1000)
        self.pixmap = QPixmap("images/logo_small.jpg")
        self.logoLabel.setPixmap(self.pixmap)
        self.text = self.comboBox.currentText()
       # self.theoryButton.clicked.connect(self.theory)
        self.backButton.clicked.connect(self.back)
        self.nextButton.clicked.connect(self.next)
        self.showButton.clicked.connect(self.sh)
        self.returnButton.clicked.connect(self.returnn)
        self.speakButton.clicked.connect(self.speak_current_text_streaming)
        self.speed05Button.clicked.connect(self.speed05)
        self.speed1Button.clicked.connect(self.speed1)
        self.speed2Button.clicked.connect(self.speed2)

        self.stopButton.clicked.connect(self.stop_speaking)
        self.stopButton.setEnabled(False)

        if TTS_AVAILABLE:
            try:
                self.speaker = lib_speak.Speaker(
                    model_id="ru_v3",
                    language="ru",
                    speaker="baya",
                    device="cpu"
                )
                print("TTS инициализирован успешно")
            except Exception as e:
                print(f"Ошибка инициализации TTS: {e}")
                self.speaker = None

        with open(f"theory/5.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            self.textLabel.setText(text)
            self.textLabel.setStyleSheet(
                """font: 13pt "Palatino Linotype";""")
            self.textLabel.setTextFormat(Qt.RichText)
        self.pixmap_formulas = QPixmap(f"images/theory/1/0.png")
        self.photoLabel.setPixmap(self.pixmap_formulas)
        self.photoLabel.setScaledContents(True)


        self.flag = False
        self.count = 0
        self.counter = 0

    def speed05(self):
        self.speed = 0.5
        self.speed05Button.setStyleSheet(
            """font: 63 14pt "Sitka Text Semibold";
            border-radius: 7px;
            border-radius: 17px;

            border-width:3px;
        border-style: solid;
        border-color: rgb(24, 97, 27);
                """)

        self.speed1Button.setStyleSheet("""
        font: 63 14pt "Sitka Text Semibold";
border-radius: 7px;
border-radius: 17px;

border-width:3px;
border-style: solid;
border-color:rgb(135, 0, 0);
        """
        )
        self.speed2Button.setStyleSheet("""
                font: 63 14pt "Sitka Text Semibold";
        border-radius: 7px;
        border-radius: 17px;

        border-width:3px;
        border-style: solid;
        border-color:rgb(135, 0, 0);
                """
                                        )

    def speed1(self):
        self.speed = 1.0
        self.speed1Button.setStyleSheet(
            """font: 63 14pt "Sitka Text Semibold";
            border-radius: 7px;
            border-radius: 17px;

            border-width:3px;
        border-style: solid;
        border-color: rgb(24, 97, 27);
                """)

        self.speed05Button.setStyleSheet("""
                font: 63 14pt "Sitka Text Semibold";
        border-radius: 7px;
        border-radius: 17px;

        border-width:3px;
        border-style: solid;
        border-color:rgb(135, 0, 0);
                """
                                        )
        self.speed2Button.setStyleSheet("""
                        font: 63 14pt "Sitka Text Semibold";
                border-radius: 7px;
                border-radius: 17px;

                border-width:3px;
                border-style: solid;
                border-color:rgb(135, 0, 0);
                        """
                                        )

    def speed2(self):
        self.speed = 1.5
        self.speed2Button.setStyleSheet(
            """font: 63 14pt "Sitka Text Semibold";
            border-radius: 7px;
            border-radius: 17px;

            border-width:3px;
        border-style: solid;
        border-color: rgb(24, 97, 27);
                """)

        self.speed05Button.setStyleSheet("""
                        font: 63 14pt "Sitka Text Semibold";
                border-radius: 7px;
                border-radius: 17px;

                border-width:3px;
                border-style: solid;
                border-color:rgb(135, 0, 0);
                        """
                                         )
        self.speed1Button.setStyleSheet("""
                                font: 63 14pt "Sitka Text Semibold";
                        border-radius: 7px;
                        border-radius: 17px;

                        border-width:3px;
                        border-style: solid;
                        border-color:rgb(135, 0, 0);
                                """
                                        )

    def speak_current_text_streaming(self):
        if not TTS_AVAILABLE or self.speaker is None:
            QMessageBox.warning(self, "Ошибка", "TTS не доступен")
            return

        with open(f"theory/speak/mech/{self.result[0]}.txt", 'r', encoding='utf-8') as file:
            text = file.read()

        if not text or text.isspace():
            QMessageBox.warning(self, "Предупреждение", "Нет текста для озвучивания!")
            return

        # Если уже играет, останавливаем
        if self.is_playing:
            self.stop_speaking()

        self.is_playing = True
        self.stop_playback_flag = False
        self.speakButton.setEnabled(False)
        self.stopButton.setEnabled(True)

        # Запускаем в отдельном потоке
        self.tts_thread = threading.Thread(target=self._synthesize_and_play, args=(text,), daemon=True)
        self.tts_thread.start()

    def _synthesize_and_play(self, text):
        audio_queue = queue.Queue()
        self.player_thread = None

        def audio_player():
            try:
                with sd.OutputStream(samplerate=48000, channels=1, dtype='float32') as stream:
                    while not self.stop_playback_flag:
                        try:
                            speech_chunk = audio_queue.get(timeout=0.05)
                            if speech_chunk is None:
                                break
                            if self.stop_playback_flag:
                                break
                            audio_array = np.frombuffer(speech_chunk, dtype=np.float32)
                            stream.write(audio_array)
                        except queue.Empty:
                            continue
            except Exception as e:
                print(f"Ошибка в audio_player: {e}")

        self.player_thread = threading.Thread(target=audio_player, daemon=True)
        self.player_thread.start()

        try:
            for chunk, _ in self.speaker.speak(
                    text=text,
                    sample_rate=48000,
                    speed=self.speed,
                    volume=0.7
            ):
                if self.stop_playback_flag:
                    while not audio_queue.empty():
                        try:
                            audio_queue.get_nowait()
                        except queue.Empty:
                            break
                    break
                audio_queue.put(chunk)

            if not self.stop_playback_flag:
                audio_queue.put(None)
            else:
                audio_queue.put(None)

        except Exception as e:
            print(f"Ошибка синтеза: {e}")
            audio_queue.put(None)
        finally:
            if self.player_thread and self.player_thread.is_alive():
                self.player_thread.join(timeout=1.0)


#            QTimer.singleShot(0, self._on_playback_finished)

    def stop_speaking(self):
        self.stop_playback_flag = True
        self.is_playing = False
        if hasattr(self, 'speaker') and self.speaker:
            try:
                if hasattr(self.speaker, 'cancel'):
                    self.speaker.cancel()
            except:
                pass

        self.speakButton.setEnabled(True)
        self.stopButton.setEnabled(False)



    def back(self):
        from theory import Theory
        self.close()

        self.theory_form = Theory()
        self.theory_form.show()

    def sh(self):
        self.count = 0
        self.flag = True
        self.parameter = self.comboBox.currentText()
        self.result = self.cur.execute(f"""SELECT * FROM mech
                                        WHERE name = '{self.parameter}'""").fetchone()
        if self.parameter == "Кинематика":
            self.counter = 6
        elif self.parameter == "Динамика":
            self.counter = 5
        elif self.parameter == "Движение по окружности":
            self.counter = 5
        elif self.parameter == "Статика":
            self.counter = 3 
        elif self.parameter == "Законы сохранения":
            self.counter = 5
        elif self.parameter == "Механические колебания и волны":
            self.counter = 6





        with open(f"theory/{self.result[0]}.txt", 'r', encoding='utf-8') as file:
            text = file.read()
            self.textLabel.setText(text)
            self.textLabel.setStyleSheet(
                """font: 13pt "Palatino Linotype";""")
        self.pixmap_formulas = QPixmap(f"images/theory/{self.result[2]}/{self.count}.png")
        self.photoLabel.setPixmap(self.pixmap_formulas)
        self.photoLabel.setScaledContents(True)

    def next(self):
        if self.count < self.counter and self.flag:
            self.count += 1
            self.pixmap_formulas = QPixmap(f"images/theory/{self.result[2]}/{self.count}.png")
            self.photoLabel.setPixmap(self.pixmap_formulas)
            self.photoLabel.setScaledContents(True)

    def returnn(self):
        if self.count>=1 and self.flag:
            self.count -= 1
            self.pixmap_formulas = QPixmap(f"images/theory/{self.result[2]}/{self.count}.png")
            self.photoLabel.setPixmap(self.pixmap_formulas)
            self.photoLabel.setScaledContents(True)







