from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        loadUi("userinterface.ui", self)    


app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())