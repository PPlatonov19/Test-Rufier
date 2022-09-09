from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox
from instr import *
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
        
class SScreeen(QWidget):
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
        self.instruction1 = QLabel(text_instruction1)
        self.instruction2 = QLabel(text_instruction2)
        self.instruction3 = QLabel(text_instruction3)
        self.instruction4 = QLabel(text_instruction4)
        self.instruction5 = QLabel(text_instruction5)
        self.button = QPushButton(text_button)
        self.VLayout = QVBoxLayout()
        self.VLayout.addWidget(self.instruction1)
        self.VLayout.addWidget(self.instruction2)
        self.VLayout.addWidget(self.instruction3)
        self.VLayout.addWidget(self.instruction4)
        self.VLayout.addWidget(self.instruction5)
        self.VLayout.addWidget(self.button)
        self.setLayout(VLayout)

    def connects(self):
        self.button.clicked.connect(self.final_win)

    def next_win(self):
        self.hide()

app = QApplication([])
mw = FScreen()
app.exec_()