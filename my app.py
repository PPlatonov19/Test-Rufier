from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox
class FScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(text_title)
        self.reisze(win_width, win_height)
    
    def initUI(self):
        self.text = QLabel(text)
        self.instruction = QLabel(text_instruction)
        self.button = QPushButton(text_button)
        self.VLayout = QVBoxLayout()
        self.VLayout.addWidget(self.text)
        self.VLayout.addWidget(self.instruction)
        self.VLayout.addWidget(self.button)
        self.setLayout(VLayout)

    def connects(self):
        self.button.clicked.connect(self.next_win)

    def next_win(self):
        self.hide()
        #создать класс следующего экрана

#class SScreeen(QWidget):

app = QApplication([])
mw = FScreen()
app.exec_()