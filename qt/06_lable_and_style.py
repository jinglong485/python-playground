from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Label and style"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 200
        self.iconName = "icon.png"
        self.initWindow()
        
    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        label = QLabel("This is a label.")
        vbox.addWidget(label)
        label2 = QLabel("I am still learning typing without watching the keyboard.")
        label2.setFont(QtGui.QFont("arial", 20))
        label2.setStyleSheet("color:red")
        label3 = QLabel("cat.JPG")
        vbox.addWidget(label3)
        vbox.addWidget(label2)
        self.setLayout(vbox)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
