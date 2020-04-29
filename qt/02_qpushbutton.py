from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = 'push button'
        left = 500
        top = 200
        width = 300
        height  = 300
        iconName = 'face.png'
        
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        
        self.UiComponents()
        
        self.show()
        
    def UiComponents(self):
        button = QPushButton("Don't Click Me!",self)
        #button.move(50,50)
        button.setGeometry(QRect(50,100,150,50))#left,top,width,height
        button.setIcon(QtGui.QIcon('face.png'))
        button.setIconSize(QtCore.QSize(30,30))
        button.setToolTip("You will click it anyway.")
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
