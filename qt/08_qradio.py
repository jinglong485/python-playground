from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
	
	def __init__(self):
		super().__init__()
		self.title = "QRadio"
		self.left = 200
		self.top = 200
		self.width = 200
		self.height = 80
		self.iconName = "face.png"
		self.initWindow()
		
	def initWindow(self):
		self.setWindowIcon(QtGui.QIcon(self.iconName))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.CreateLayout()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupBox)
		self.label = QLabel(self)
		self.label.setFont(QtGui.QFont("arial", 15))
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		self.show()
		
	def CreateLayout(self):
		self.groupBox = QGroupBox("What is that sound?")
		self.groupBox.setFont(QtGui.QFont("arial",13))
		hboxlayout = QHBoxLayout()
		self.radiobtn1 = QRadioButton("WOW")
		self.radiobtn1.setChecked(True)
		self.radiobtn1.setIcon(QtGui.QIcon(self.iconName))
		self.radiobtn1.setIconSize(QtCore.QSize(40,40))
		self.radiobtn1.setFont(QtGui.QFont("arial",13))
		hboxlayout.addWidget(self.radiobtn1)
		self.radiobtn1.toggled.connect(self.onRadioBtn)
		self.radiobtn2 = QRadioButton("HOHO")
		self.radiobtn2.setIcon(QtGui.QIcon(self.iconName))
		self.radiobtn2.setIconSize(QtCore.QSize(40,40))
		self.radiobtn2.setFont(QtGui.QFont("arial",13))
		hboxlayout.addWidget(self.radiobtn2)
		self.radiobtn2.toggled.connect(self.onRadioBtn)
		self.radiobtn3 = QRadioButton("HAHA")
		self.radiobtn3.setIcon(QtGui.QIcon(self.iconName))
		self.radiobtn3.setIconSize(QtCore.QSize(40,40))
		self.radiobtn3.setFont(QtGui.QFont("arial",13))
		hboxlayout.addWidget(self.radiobtn3)
		self.radiobtn3.toggled.connect(self.onRadioBtn)
		self.radiobtn4 = QRadioButton("Whahahah")
		self.radiobtn4.setIcon(QtGui.QIcon(self.iconName))
		self.radiobtn4.setIconSize(QtCore.QSize(40,40))
		self.radiobtn4.setFont(QtGui.QFont("arial",13))
		hboxlayout.addWidget(self.radiobtn4)
		self.radiobtn4.toggled.connect(self.onRadioBtn)
		self.groupBox.setLayout(hboxlayout)
		
	def onRadioBtn(self):
		radioBtn = self.sender()
		if radioBtn.isChecked():
			self.label.setText("You say it is {}?".format(radioBtn.text()))
			
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())
			