from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Size Grip"
        self.left = 200
        self.top = 100
        self.width = 200
        self.height = 70
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        vbox = QVBoxLayout()
        sizeGrip = QSizeGrip(self)
        vbox.addWidget(sizeGrip)
        self.setLayout(vbox)
        self.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())