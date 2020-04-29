from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()
        
        self.title = 'layout'
        self.left = 500
        self.top = 200
        self.width = 300
        self.height  = 300
        self.iconName = 'face.png'
        
        self.initWindow()
        
        
    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.groupBox)
        hbox.addWidget(self.groupBox2)
        self.setLayout(hbox)
        self.show()
        
        
    def createLayout(self):
        self.groupBox = QGroupBox("What is the music of life?")
        self.groupBox2 = QGroupBox("What is the meaning of life?")
        vboxlayout = QVBoxLayout()
        hboxlayout = QHBoxLayout()
        
        button1 = QPushButton("This is first button")
        button1.setIcon(QtGui.QIcon(self.iconName))
        button1.setIconSize(QtCore.QSize(30,30))
        button1.setMinimumHeight(40)
        button1.setToolTip("Close Application")
        vboxlayout.addWidget(button1)
        
        button2 = QPushButton("This is second button")
        button2.setIcon(QtGui.QIcon(self.iconName))
        button2.setIconSize(QtCore.QSize(30,30))
        button2.setMinimumHeight(40)
        button2.setToolTip("Close Application this is real")
        vboxlayout.addWidget(button2)
        
        button3 = QPushButton("This is third button")
        button3.setIcon(QtGui.QIcon(self.iconName))
        button3.setIconSize(QtCore.QSize(30,30))
        button3.setMinimumHeight(40)
        button3.setToolTip("Close Application! this will work FOR SURE!")
        vboxlayout.addWidget(button3)
        
        button4 = QPushButton("This is fourth button")
        button4.setIcon(QtGui.QIcon(self.iconName))
        button4.setIconSize(QtCore.QSize(30,30))
        button4.setMinimumHeight(40)
        button4.setToolTip("This is fourth button")
        hboxlayout.addWidget(button4)
        
        button5 = QPushButton("This is fifth button")
        button5.setIcon(QtGui.QIcon(self.iconName))
        button5.setIconSize(QtCore.QSize(30,30))
        button5.setMinimumHeight(40)
        button5.setToolTip("LULALALALLAAA")
        hboxlayout.addWidget(button5)
        
        button6 = QPushButton("This is sixth button")
        button6.setIcon(QtGui.QIcon(self.iconName))
        button6.setIconSize(QtCore.QSize(30,30))
        button6.setMinimumHeight(40)
        button6.setToolTip("dadidadidadada")
        hboxlayout.addWidget(button6)
        
        self.groupBox.setLayout(vboxlayout)
        self.groupBox2.setLayout(hboxlayout)
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
