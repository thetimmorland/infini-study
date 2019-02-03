import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

from ui import mainWindow
from db import problemDb
from jupyter import jupyterServer

if __name__ == '__main__':
    app = QApplication(sys.argv)

    db = problemDb()
    server = jupyterServer()
    win = mainWindow(db, server)
    win.show()

    sys.exit(app.exec_())

