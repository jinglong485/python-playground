from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QButtonGroup
import sys
from PyQt5 import QtCore

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "button group"
        self.left = 200
        self.top = 300
        self.width = 300
        self.height = 60
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.title))
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        self.label = QLabel()
        self.label.setFont(QtGui.QFont("arial", 20))
        self.label.setStyleSheet("color:blue")
        self.label.setFixedWidth(300)
        hbox.addWidget(self.label)
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.buttonClicked['int'].connect(self.onButtonClicked)
        button = Button("first", self.iconName, 20,'arial', 'blue' )
        self.buttonGroup.addButton(button,1)
        hbox.addWidget(button)
        button = Button("second", self.iconName, 20,'arial', 'yellow' )
        self.buttonGroup.addButton(button,2)
        hbox.addWidget(button)
        button = Button("third", self.iconName, 20,'arial', 'green' )
        self.buttonGroup.addButton(button,3)
        hbox.addWidget(button)
        self.setLayout(hbox)
        self.show()
    
    def onButtonClicked(self,id):
        for buttons in self.buttonGroup.buttons():
            if buttons is self.buttonGroup.button(id):
                self.label.setText(buttons.text()+' was clicked.')
    
    
class Button(QPushButton):
    
    def __init__(self, name, icon, size, font, color):
        super().__init__()
        self.setText(name)
        self.setIcon(QtGui.QIcon(icon))
        self.setFont(QtGui.QFont(font,15))
        self.setIconSize(QtCore.QSize(size,size))
        self.setStyleSheet("color:{}".format(color))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())