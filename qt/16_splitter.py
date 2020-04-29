from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QSplitter, QButtonGroup, QGroupBox, QPushButton, QFrame, QLabel
import sys
from PyQt5.QtCore import Qt

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'splitter'
        self.left = 200
        self.top = 300
        self.width = 400
        self.height = 100
        self.iconName = 'face.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createButtonGroup()#self.buttonGroupBox
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.buttonGroupBox)
        self.frame  = QFrame()
        self.frame.setStyleSheet("background-color:brown")
        splitter1.addWidget(self.frame)
        splitter2 = QSplitter(Qt.Vertical)
        self.label = QLabel('Brown')
        self.label.setFont(QtGui.QFont('arial',20))
        self.label.setStyleSheet("color:brown")
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.label)
        hbox = QHBoxLayout()
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.show()
        
    def createButtonGroup(self):
        self.button = QButtonGroup()
        self.button.buttonClicked['int'].connect(self.myButtonClicked)
        btn1 = MyButton("first","blue")
        btn2 = MyButton("second","red")
        btn3 = MyButton("third","yellow")
        self.button.addButton(btn1, 1)
        self.button.addButton(btn2, 2)
        self.button.addButton(btn3, 3)
        self.buttonGroupBox = QGroupBox()
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.buttonGroupBox.setLayout(vbox)
        
    def myButtonClicked(self,id):
        if id == 1:
            self.label.setText('Blue')
            self.label.setStyleSheet("color:blue")
            self.frame.setStyleSheet("background-color:blue")
        if id == 2:
            self.label.setText("Red")
            self.label.setStyleSheet("color:red")
            self.frame.setStyleSheet("background-color:red")
        if id == 3:
            self.label.setText('yellow')
            self.label.setStyleSheet("color:yellow")
            self.frame.setStyleSheet("background-color:yellow")
            
            
class MyButton(QPushButton):
    
    def __init__(self, text, color):
        super().__init__()
        self.setText(text)
        self.setStyleSheet('color:{}'.format(color))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
                