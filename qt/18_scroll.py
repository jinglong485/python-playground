from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys

class Window(QWidget):
    
    def __init__(self, val):
        super().__init__()
        self.title = "scroll bar"
        self.left = 200
        self.top = 200
        self.width = 1000
        self.height = 900
        self.iconName = "face.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout = QFormLayout()
        groupBox = QGroupBox("This is a group box")
        labelList = []
        comboList = []
        for i in range(val):
            labelList.append(QLabel("label"))
            comboList.append(QPushButton("What?"))
            formLayout.addRow(labelList[i],comboList[i])
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(30)
    sys.exit(app.exec())