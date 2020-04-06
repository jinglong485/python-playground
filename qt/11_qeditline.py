from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
import sys


class Window(QWidget):
	
	def __init__(self):
		super().__init__()
		self.title = "Line Edit"
		self.left = 200
		self.top = 300
		self.width = 300
		self.height = 60
		self.iconName = "face.png"
		self.initWindow()
		
	def initWindow(self):
		self.setWindowIcon(QtGui.QIcon(self.iconName))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		vbox = QVBoxLayout()
		self.label = QLabel("Please input some thing")
		self.label.setFont(QtGui.QFont("arial", 20))
		self.label.setStyleSheet("color:blue")
		self.label.setFixedWidth(300)
		self.lineedit = QLineEdit()
		self.lineedit.setFont(QtGui.QFont("arial", 20))
		self.lineedit.setFixedWidth(300)
		self.lineedit.returnPressed.connect(self.onPressed)
		vbox.addWidget(self.label)
		vbox.addWidget(self.lineedit)
		self.setLayout(vbox)
		self.show()
	
	def onPressed(self):
		self.label.setText(self.lineedit.text())
		self.lineedit.clear()
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())