from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QVBoxLayout, QLabel
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "QDial"
        self.left = 200
        self.top = 100
        self.width = 300
        self.height = 100
        self.iconName  = 'face.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.dial = QDial()
        self.dial.setMinimum(20)
        self.dial.setMaximum(100)
        self.dial.setValue(60)
        self.dial.valueChanged.connect(self.onChangedValue)
        self.label = QLabel("60")
        vbox = QVBoxLayout()
        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()
        
    def onChangedValue(self):
        dialValue = self.dial.value()
        self.label.setText(str(dialValue))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
        
        
