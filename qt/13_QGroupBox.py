from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QRadioButton, QGroupBox, QLabel
import sys
from PyQt5 import QtGui

class Window(QWidget):
     
    def __init__(self):
        super().__init__()
        self.title = 'group box'
        self.left = 200
        self.top = 100
        self.width = 300
        self.height = 60
        self.iconName = 'face.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        self.button = QPushButton('haha')
        self.button.clicked.connect(self.onClicked)
        hbox.addWidget(self.button)
        self.checkBox = QCheckBox("what")
        self.checkBox.setChecked(True)
        self.checkBox.setIcon(QtGui.QIcon(self.iconName))
        self.checkBox.setFont(QtGui.QFont("arial", 15))
        self.checkBox.toggled.connect(self.onChecked)
        hbox.addWidget(self.checkBox)
        self.groupBox1 = QGroupBox("buttons")
        self.groupBox1.setLayout(hbox)
        vbox = QVBoxLayout()
        self.label = QLabel()
        vbox.addWidget(self.label)
        vbox.addWidget(self.groupBox1)
        self.setLayout(vbox)
        self.show()
        
    def onClicked(self):
        print("Clicked!")
        self.label.setText('What?')
        if self.checkBox.isChecked():
            self.checkBox.setChecked(False)
            
    def onChecked(self):
        if self.checkBox.isChecked():
            self.label.setText("WOW")
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
        