from PyQt5.QtCore import QUrl
import PyQt5.QtWebEngineWidgets

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUiType

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        (self.form, self.base) = loadUiType('ui/mainWindow.ui')
        self.ui = self.form()
        self.ui.setupUi(self)

class jupyterView(QWidget):
    def __init__(self):
        super(jupyterView, self).__init__()
        (self.form, self.base) = loadUiType('ui/jupyterView.ui')
        self.ui = self.form()
        self.ui.setupUi(self)

        
        self.ui.webView.load(QUrl('https://www.google.com'))

