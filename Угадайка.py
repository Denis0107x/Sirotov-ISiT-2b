import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
import random
class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Попробуй угадть число")
        self.label = QLabel("Попробуй угадать число от 1 до 100")
        self.button = QPushButton("Попробовать угадать")
        self.button.clicked.connect(self.check_number)
        self.number_to_guess = None
        self.max_attempts = 10
        self.attempts = 0
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.new_game()
    def check_number(self):
        guess = int(self.line_edit.text())
        self.attempts += 1
        if guess == self.number_to_guess:
            self.label.setText(f"Ура! Вы отгадали число {self.number_to_guess} за {self.attempts} попыток.")
            self.button.setEnabled(False)
            self.line_edit.setEnabled(False)
            self.show_game_over_message()
        elif guess < self.number_to_guess:
            self.label.setText("Число больше!")
        else:
            self.label.setText("Число меньше!")
        if self.attempts >= self.max_attempts:
            self.label.setText(
                f"Все {self.max_attempts} попыток использовано. Загаданное число было {self.number_to_guess}.")
            self.button.setEnabled(False)
            self.line_edit.setEnabled(False)
            self.show_game_over_message()
    def new_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.button.setEnabled(True)
        self.line_edit.setEnabled(True)
        self.label.setText("Попробуй угадть число от 1 до 100")
        self.line_edit.clear()
    def show_game_over_message(self):
        msg_box = QMessageBox()
        msg_box.setText("Конец!")
        msg_box.setInformativeText("Хотите начать новую игру?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.new_game()
        else:
            QApplication.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec())