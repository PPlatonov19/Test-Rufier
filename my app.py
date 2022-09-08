from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox
def final():
    result = QMessageBox()
    result.setText('')
    result.exec_()
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Тест Руфье')
main_text = QLabel('Тест Руфье')
main_line = QVBoxLayout()
main_line.addWidget(main_text, alignment = Qt.AlignLeft)
my_win.setLayout(main_line)
my_win.show()
app.exec_()