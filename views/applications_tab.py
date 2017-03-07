from PyQt5.QtWidgets import QWidget

from ui.applications.applications_tab import Ui_ApplicationsTab
from views.application_wizard import ApplicationWizard


class ApplicationsTab(QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__(parent)
        self.ui = Ui_ApplicationsTab()
        self.ui.setupUi(self)

        self.setupSignals()

    def setupSignals(self):
        self.ui.buttonWizard.clicked.connect(self.createApplication)

    def createApplication(self):
        wizard = ApplicationWizard(self)
        result = wizard.exec()
        pass
