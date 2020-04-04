from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):

	def __init__(self):
		super().__init__()
		self.title = "check box"
		self.left = 200
		self.top = 300
		self.width = 200
		self.height = 70
		self.iconName = "face.png"
		self.initWindow()

	def initWindow(self):
		self.setWindowTitle(self.title)
		self.setWindowIcon(QtGui.QIcon(self.iconName))
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.createGroupBox()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupBox)
		vbox.addWidget(self.groupBox2)
		self.label = QLabel("What is the problem?")
		self.label.setFont(QtGui.QFont("arial", 15))
		self.label.setStyleSheet("color:green")
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		self.show()

	def createGroupBox(self):
		self.groupBox = QGroupBox("This is a check box demo")
		self.groupBox.setFont(QtGui.QFont("arial",15))
		hboxlayout = QHBoxLayout()
		self.checkBox1 = QCheckBox("This is the first check box")
		self.checkBox1.setWhatsThis("WOW")
		self.checkBox1.setIcon(QtGui.QIcon(self.iconName))
		self.checkBox1.setIconSize(QtCore.QSize(30,30))
		self.checkBox1.toggled.connect(self.onCheckBox_toggled)
		hboxlayout.addWidget(self.checkBox1)
		self.checkBox2 = QCheckBox("This is the second check box")
		self.checkBox2.setWhatsThis("HAHA")
		self.checkBox2.setIcon(QtGui.QIcon("face.png"))
		self.checkBox2.setIconSize(QtCore.QSize(30,30))
		self.checkBox2.toggled.connect(self.onCheckBox_toggled)
		hboxlayout.addWidget(self.checkBox2)
		self.groupBox.setLayout(hboxlayout)
		
		self.button =  QPushButton("Just for What is This")
		self.groupBox2 = QGroupBox("This is for button")
		self.button.setWhatsThis("Info!")
		boxlayout = QHBoxLayout()
		boxlayout.addWidget(self.button)
		self.groupBox2.setLayout(boxlayout)

	def onCheckBox_toggled(self):
		if self.checkBox1.isChecked() and not self.checkBox2.isChecked():
			self.label.setFont(QtGui.QFont("arial",15))
			self.label.setStyleSheet("color:green")
			self.label.setText("This is the first box(checked) "+ self.checkBox1.text())
		if self.checkBox2.isChecked() and not self.checkBox1.isChecked():
			self.label.setFont(QtGui.QFont("arial",15))
			self.label.setStyleSheet("color:green")
			self.label.setText("This is the seciond box (checked) "+ self.checkBox2.text())
		if self.checkBox1.isChecked() and self.checkBox2.isChecked():
			self.label.setFont(QtGui.QFont("arial",20))
			self.label.setStyleSheet("color:red")
			self.label.setText("You cannot check all!")
		if not self.checkBox1.isChecked() and not self.checkBox2.isChecked():
			self.label.setText("What?")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())

