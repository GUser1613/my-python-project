from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

app = QApplication([])

window = QWidget()
window.setWindowTitle("Таблица")
window.resize(300, 200)

table = QTableWidget(3, 2, window)

table.setItem(0, 0, QTableWidgetItem("A"))
table.setItem(0, 1, QTableWidgetItem("B"))

window.show()
app.exec()