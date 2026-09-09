import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

app = QApplication(sys.argv)
app.setStyle("Fusion")

window = QMainWindow()
window.setWindowTitle("Style Test")
window.resize(400, 300)

output = QPlainTextEdit()
output.setReadOnly(True)
output.setStyleSheet("background-color: black; color: #33ff33;")
output.appendPlainText("If this is black with green text, styling works.")
window.setCentralWidget(output)

window.show()
sys.exit(app.exec())