from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "event and signal"
        self.top = 500
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("face.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)#set the window position and size
        
        self.CreatButton()
        self.show()
        
    def CreatButton(self):
        button = QPushButton("Don't Click Me!",self)
        #button.move(50,50)
        button.setGeometry(QRect(50,100,150,50))#left,top,width,height
        button.setIcon(QtGui.QIcon('face.png'))
        button.setIconSize(QtCore.QSize(30,30))
        button.setToolTip("You will click it anyway.")
        button.clicked.connect(self.ClickMe)
        
    def ClickMe(self):
        print("Hello World!")
        sys.exit()
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
