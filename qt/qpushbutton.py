from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init_(self):
        super().__init__()
        
        title = 'push button'
        left = 500
        top = 200
        width = 300
        height  = 250
        iconName = 'face.png'
        
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.show()
        
        
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
