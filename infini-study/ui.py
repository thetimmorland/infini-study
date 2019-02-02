from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUiType

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        (self.form, self.base) = loadUiType('ui/mainWindow.ui')
        self.ui = self.form()
        self.ui.setupUi(self)

