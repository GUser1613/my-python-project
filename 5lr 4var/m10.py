from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])

window = QWidget()
window.setWindowTitle("Простейший GUI на PyQt5")

label = QLabel("Hello, world!", window)

window.show()
app.exec()

