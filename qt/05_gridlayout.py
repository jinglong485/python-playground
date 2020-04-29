from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "grid layout"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 200
        self.iconName = "icon.png"
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("What is the music of life?")
        gridLayout = QGridLayout()
        self.button = QPushButton("WOW", self)
#        self.button.setSize()
        self.button.setIcon(QtGui.QIcon("face.png"))
        self.button.setIconSize(QtCore.QSize(40,40))
        self.button.setMinimumHeight(40)
        gridLayout.addWidget(self.button,0,0)
        self.button2 = QPushButton("HoHo", self)
        self.button2.setIcon(QtGui.QIcon("face.png"))
        self.button2.setIconSize(QtCore.QSize(40,40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2,1,0)
        self.button3 = QPushButton("kaka", self)
        self.button3.setIcon(QtGui.QIcon("face.png"))
        self.button3.setIconSize(QtCore.QSize(40,40))
        self.button3.setMinimumHeight(40)
        gridLayout.addWidget(self.button3,0,1)
        self.button4 = QPushButton("lulala", self)
        self.button4.setIcon(QtGui.QIcon("face.png"))
        self.button4.setIconSize(QtCore.QSize(40,40))
        self.button4.setMinimumHeight(40)
        gridLayout.addWidget(self.button4,1,1)
        self.button5 = QPushButton("WOW", self)
        self.button5.setIcon(QtGui.QIcon("face.png"))
        self.button5.setIconSize(QtCore.QSize(40,40))
        self.button5.setMinimumHeight(40)
        gridLayout.addWidget(self.button5,20,1)
        self.groupBox.setLayout(gridLayout)
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())