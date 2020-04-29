from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QSlider, QHBoxLayout, QVBoxLayout, QWidget, QGroupBox
import sys
import os
from PyQt5.QtCore import Qt


class Window(QWidget):
    
    def __init__(self,filePath = "./"):
        super().__init__()
        self.title = "slider"
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        #self.setGeometry(self.left, self.top, self.width, self.height)
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
        self.frameLeft.setStyleSheet('background-color:rgb(255,255,255)')
        self.frameLeft.setLayout(vbox)
        self.frameRight = QFrame()
        self.frameRight.setStyleSheet('background-color:rgb(0,0,0)')
        self.label = QLabel('(0, 0, 0)')
        #self.label.setFixedWidth(100)
        box = QHBoxLayout()
        box.addWidget(self.label)
        self.frameRight.setLayout(box)
        hbox.addWidget(self.frameLeft)
        hbox.addWidget(self.frameRight)
        groupBoxUpper = QGroupBox("Color Mixer")
        groupBoxUpper.setLayout(hbox)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(groupBoxUpper)
        self.slider4 = QSlider()
        self.slider4.setOrientation(Qt.Horizontal)
        self.slider4.setTickPosition(QSlider.TicksBelow)
        self.slider4.setTickInterval(1)
        self.slider4.setMinimum(50)
        self.slider4.setMaximum(150)
        self.slider4.valueChanged.connect(self.changeSize)
        self.labelPicture = QLabel()
        self.labelPicture.setScaledContents(True)
        self.pixmap = QPixmap(filePath+"\\cat.jpg")
        self.pixmapChanged = QPixmap()
        self.labelPicture.setPixmap(self.pixmap)
        groupBoxLower = QGroupBox("Cat")
        lowerLayout = QVBoxLayout()
        lowerLayout.addWidget(self.slider4)
        lowerLayout.addWidget(self.labelPicture)
        groupBoxLower.setLayout(lowerLayout)
        windowLayout.addWidget(groupBoxLower)
        self.setLayout(windowLayout)
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
        
    def changeSize(self):
        ratio = self.slider4.value()
        width = 378
        height = 672
        adjustedWidth = int(float(width)*float(ratio/100.0))
        adjustedHeight = int(float(height)*float(ratio/100.0))
        self.pixmapChanged= self.pixmap.scaled(adjustedWidth, adjustedHeight)
        self.labelPicture.setPixmap(self.pixmapChanged)
        self.labelPicture.update()
        
        
if __name__ == "__main__":
    try:
        wd = sys._MEIPASS
    except AttributeError:
        wd = os.getcwd()
    app = QApplication(sys.argv)
    window = Window(wd)
    sys.exit(app.exec())
