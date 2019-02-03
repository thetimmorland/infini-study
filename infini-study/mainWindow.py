import PyQt5

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from db import db, schedule

# Load UI from QtCreator File
formClass, _ = loadUiType('infini-study/mainWindow.ui')

class mainWindow(QMainWindow, formClass):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

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

        # Initialize View
        self.stackView.setCurrentIndex(0)


    def openClicked(self):
        self.fileDialog = QFileDialog(self)
        url, _ = self.fileDialog.getOpenFileUrl(self)
        
        if url.isValid:

            self.db = db()
            self.db.open(url.toLocalFile())

            self.schedule = schedule(self.db, 5)

    def newClicked(self):
        self.fileDialog = QFileDialog(self)
        url, _ = self.fileDialog.getSaveFileUrl(self)

        if url.isValid:

            self.db = db()
            self.db.new(url.toLocalFile())
            
            self.addClicked()

    def addClicked(self):
        self.stackView.setCurrentIndex(1)

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

