from PyQt5.QtWidgets import QApplication, QPushButton, QDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super.__init__()
        self.title = 'layout'
        self.left = 500
        self.top = 200
        self.width = 300
        self.height  = 300
        self.iconName = 'face.png'
        
        self.InitWindow()
        
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
        
        
        
        
        
        
if __name__ == "__mian__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
