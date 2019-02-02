import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtWebEngineWidgets
from ui import mainWindow, jupyterView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()

    view = jupyterView()
    view.show()

    sys.exit(app.exec_())
        
