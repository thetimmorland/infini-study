import PyQt5

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QFileDialog

# Load UI from QtCreator File
formClass, _ = loadUiType('infini-study/main.ui')

class mainWindow(QMainWindow, formClass):
    def __init__(self, db, server):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.db = db
        self.server = server

        # File Menu Triggers
        self.actionOpen.triggered.connect(self.openClicked)
        self.actionNew.triggered.connect(self.newClicked)

        # Tool Menu Triggers
        self.actionAddQ.triggered.connect(self.addClicked)
        self.actionEdit.triggered.connect(self.editClicked)

        # Help Menu Triggers
        self.actionAbout.triggered.connect(self.aboutClicked)

        # Button Triggers
        self.submitButton.clicked.connect(self.submitClicked)
        self.showSolButton.clicked.connect(self.showSolClicked)
        self.cancelEditButton.clicked.connect(self.cancelEditClicked)
        self.finishEditButton.clicked.connect(self.finishEditClicked)

        self.stackView.setCurrentIndex(0)


    def openClicked(self):
        self.fileDialog = QFileDialog(self)
        url, _ = self.fileDialog.getOpenFileUrl(self)
        
        if url.isValid():
            self.db.load(url.toLocalFile())

            self.stackView.setEnabled(True)
            self.menuTools.setEnabled(True)

    def newClicked(self):
        self.fileDialog = QFileDialog(self)
        url, _ = self.fileDialog.getSaveFileUrl(self)

        if url.isValid():
            self.db.create(url.toLocalFile())

            self.stackView.setEnabled(True)
            self.menuTools.setEnabled(True)

    def addClicked(self):
        self.stackView.setCurrentIndex(1)
        self.webPage.load(self.server.url)
        self.webPage.show()

    def editClicked(self):
        self.stackView.setCurrentIndex(1)

    def aboutClicked(self):
        print('about') 

    def submitClicked(self):
        print('submit')

    def showSolClicked(self):
        print('show')

    def cancelEditClicked(self):
        print('cancel')
        self.stackView.setCurrentIndex(0)

    def finishEditClicked(self):
        print('finish')
        self.stackView.setCurrentIndex(0)

