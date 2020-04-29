from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QPushButton, QVBoxLayout
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class MyThread(QThread):
    change_value = pyqtSignal(int)
    
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=1
            time.sleep(0.3)
            self.change_value.emit(int(cnt))
            
            
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Progress Bar"
        self.iconName = 'face.png'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        vbox = QVBoxLayout()
        self.progressBar = QProgressBar()
        self.progressBar.setMaximum(100)
        self.progressBar.setStyleSheet("QProgressBar::chunk {background:yellow}")
        vbox.addWidget(self.progressBar)
        self.button = QPushButton("START")
        self.button.clicked.connect(self.startProgressBar)
        self.button.setStyleSheet("color:green")
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()
        
    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressValue)
        self.thread.start()
        
    def setProgressValue(self, value):
        self.progressBar.setValue(value)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())