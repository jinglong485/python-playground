from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "Hello World!"
        self.top = 500
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("face.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)#set the window position and size
        self.show()
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
