from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpinBox
import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "spinbox"
        self.left = 200
        self.top = 400
        self.width = 300
        self.height = 80
        self.iconName = 'face.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel("70")
        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.onValueChanged)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(55)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.spinBox)
        self.setLayout(vbox)
        self.show()
        
    def onValueChanged(self):
        value = self.spinBox.value()
        self.label.setText(str(value))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
