from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QLabel, QHBoxLayout
from PyQt5 import QtGui
import time
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "name"
        self.left = 200
        self.top = 300
        self.width = 200
        self.height = 200
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:yellow")
        self.btn1 = QPushButton("What is This?")
        self.btn1.setStyleSheet('color:white')
        self.btn1.setStyleSheet("background-color:green")
        self.btn1.clicked.connect(self.clickedBTN)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(10)
        hbox = QHBoxLayout()
        hbox.addWidget(self.frame)
        hbox.addWidget(self.btn1)
        self.setLayout(hbox)
        self.show()
        
    def clickedBTN(self):
        self.frame.setStyleSheet('background-color:blue')
        self.frame.setStyleSheet('background-color:red')
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())