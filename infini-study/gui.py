from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)
window.show()
app.exec_()

