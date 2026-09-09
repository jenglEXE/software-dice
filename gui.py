import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt, QTimer

from roll_the_dice import load_dice, roll_all
from animation import build_die

ANIMATION_DELAYS = [50, 50, 60, 80, 100, 150, 200, 300]  # milliseconds

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roller")
        self.resize(900, 550)

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setFocusPolicy(Qt.NoFocus)
        self.output.setStyleSheet("background-color: black; color: #33ff33;")
        self.setCentralWidget(self.output)

        font = QFont("Consolas", 12)
        font.setStyleHint(QFont.Monospace)
        self.output.setFont(font)

        self.dice = load_dice()
        self.rolling = False

        self.output.appendPlainText("Press space to roll.")

    def combine_dice_faces(self, faces, gap=4):
        spacer = " " * gap
        combined_lines = []
        for line_group in zip(*faces):
            combined_lines.append(spacer.join(line_group))
        return "\n".join(combined_lines)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space and not self.rolling:
            self.start_animation()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def start_animation(self):
        self.rolling = True
        self.frame_index = 0
        self.play_next_frame()

    def play_next_frame(self):
        if self.frame_index >= len(ANIMATION_DELAYS):
            self.finish_roll()
            return

        self.output.clear()
        faces = [build_die(random.randint(1, 6)) for _ in range(3)]
        self.output.appendPlainText(self.combine_dice_faces(faces))

        delay = ANIMATION_DELAYS[self.frame_index]
        self.frame_index += 1
        QTimer.singleShot(delay, self.play_next_frame)

    def finish_roll(self):
        self.output.clear()
        die1_choice, die2_choice, die3_choice = roll_all(self.dice)
        self.output.appendPlainText(f"""Rolls:
---------------
Interface/Runtime paradigm: {die1_choice}
---------------
Object/Category: {die2_choice}
---------------
Modifier (friendly/creative flavor): {die3_choice}

Press space to roll again.
Press esc to exit.""")
        self.rolling = False

def run():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()