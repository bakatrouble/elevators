from PyQt5.QtWidgets import QWidget

from controllers.application import ApplicationController
from models.application import ApplicationModel
from ui.applications.applications_tab import Ui_ApplicationsTab


class ApplicationsTab(QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__(parent)
        self.ui = Ui_ApplicationsTab()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

    def setupUi(self):
        self.ui.tableView.setModel(ApplicationModel())

    def setupSignals(self):
        self.ui.buttonWizard.clicked.connect(self.createApplication)
        self.ui.tableView.doubleClicked.connect(self.editApplication)

    def createApplication(self):
        ApplicationController.create(self) and self.ui.tableView.model().modelReset.emit()

    def editApplication(self):
        application = self.ui.tableView.currentIndex().internalPointer()
        ApplicationController.edit(application, self) and self.ui.tableView.model().modelReset.emit()
