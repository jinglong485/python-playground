from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton
import sys
from random import randint
import time

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "LCD"
        self.left = 200
        self.top = 100
        self.width = 200
        self.height = 80
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton("Random Number!")
        self.button.clicked.connect(self.onClicked)
        self.lcd = QLCDNumber()
        self.lcd.display(8888)
        self.lcd.setStyleSheet("background:rgb(162,199,63)")
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()
        
    def onClicked(self):
        self.lcd.display(randint(1000,9999))
        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())