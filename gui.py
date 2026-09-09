import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roller")
        self.resize(700, 500)

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.setCentralWidget(self.output)

        font = QFont("Consolas", 12)
        font.setStyleHint(QFont.Monospace)
        self.output.setFont(font)

        palette = self.output.palette()
        palette.setColor(QPalette.Base, QColor("black"))
        palette.setColor(QPalette.Text, QColor("#33ff33"))
        self.output.setPalette(palette)

        self.output.appendPlainText("Press space to roll.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.output.appendPlainText("You rolled!")
        elif event.key() == Qt.Key_Escape:
            self.close()

def run():
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()