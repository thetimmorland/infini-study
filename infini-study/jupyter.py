from subprocess import Popen
from PyQt5.QtCore import QUrl

class jupyterServer():
    def __init__(self):
        self.url = QUrl('http://localhost:8888')
        self.server = Popen(
                ['jupyter-notebook', '-y', '--no-browser',
                "--NotebookApp.token=''"])
        
