from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QSlider, QHBoxLayout, QVBoxLayout, QWidget, QGroupBox
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "slider"
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.slider1 = QSlider()
        self.slider2 = QSlider()
        self.slider3 = QSlider()
        self.sliderConfig(self.slider1)
        self.sliderConfig(self.slider2)
        self.sliderConfig(self.slider3)
        self.slider1.valueChanged.connect(self.changeValue)
        self.slider2.valueChanged.connect(self.changeValue)
        self.slider3.valueChanged.connect(self.changeValue)
        vbox.addWidget(self.slider1)
        vbox.addWidget(self.slider2)
        vbox.addWidget(self.slider3)
        self.frameLeft = QFrame()
        self.frameLeft.setLayout(vbox)
        self.frameRight = QFrame()
        self.label = QLabel('(0, 0, 0)')
        self.label.setFixedWidth(100)
        box = QHBoxLayout()
        box.addWidget(self.label)
        self.frameRight.setLayout(box)
        hbox.addWidget(self.frameLeft)
        hbox.addWidget(self.frameRight)
        self.setLayout(hbox)
        self.show()
        
    def sliderConfig(self, slider):
        slider.setOrientation(Qt.Horizontal)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        slider.setMinimum(0)
        slider.setMaximum(255)
        
    def changeValue(self):
        value1 = self.slider1.value()
        value2 = self.slider2.value()
        value3 = self.slider3.value()
        self.label.setText('({}, {} ,{})'.format(value1, value2, value3))
        self.frameRight.setStyleSheet('background-color:rgb({}, {} ,{})'.format(value1, value2, value3))
        self.frameLeft.setStyleSheet('background-color:rgb({}, {} ,{})'.format(255-value1, 255-value2, 255-value3))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())