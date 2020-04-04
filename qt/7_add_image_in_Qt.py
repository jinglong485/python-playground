from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel

class Window(QDialog):
	def __init__(self):
		super().__init__()
		self.title = "Whai is this software for?"
		self.left = 200
		self.top = 400
		self.width = 200
		self.height = 600
		self.iconName = "icon.png"
		self.initWindow()
		
	def initWindow(self):
		self.setWindowTitle(self.title)
		self.setWindowIcon(QtGui.QIcon(self.iconName))
		self.setGeometry(self.left, self.top, self.width, self.height)
		vbox = QVBoxLayout()
		labelImage = QLabel("What is this for?")
		pixmap = QPixmap("cat.JPG")
		labelImage.setPixmap(pixmap)
		labelImage.setMargin(0)
		vbox.addWidget(labelImage)
		self.setLayout(vbox)
		self.show()
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())
		