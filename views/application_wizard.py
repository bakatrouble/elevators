from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWizard

from models.application import Application, DataTableModel, DataTableDelegate

from controllers.client import ClientController
from models.application_type import ApplicationTypeModel
from ui.applications.application_wizard import Ui_ApplicationWizard


class ApplicationWizard(QWizard):
    def __init__(self, parent=None):
        super(ApplicationWizard, self).__init__(parent)
        self.ui = Ui_ApplicationWizard()
        self.ui.setupUi(self)

        self.setupSignals()
        self.setupUi()

        self._client = None
        self._application = Application()

    def setupSignals(self):
        self.ui.btnSelectClient.clicked.connect(self.selectClient)
        self.ui.btnTableAdd.clicked.connect(self.addTableItem)
        self.ui.btnTableRemove.clicked.connect(self.removeTableItem)

    def setupUi(self):
        self.ui.tblElevatorsData.horizontalHeader().setVisible(True)
        self.ui.cmbApplicationType.setModel(ApplicationTypeModel())
        self.ui.tblElevatorsData.setModel(DataTableModel())
        self.ui.tblElevatorsData.setItemDelegate(DataTableDelegate())

    def addTableItem(self):
        self.ui.tblElevatorsData.model().addItem()

    def removeTableItem(self):
        rows = {index.row() for index in self.ui.tblElevatorsData.selectedIndexes()}
        self.ui.tblElevatorsData.model().removeItems(rows)

    def selectClient(self):
        result, client = ClientController.choose(self)
        if result == QDialog.Accepted and client:
            self._client = client
            self.ui.lblClient.setText(client.short_name)

    def getApplication(self):
        self._application.date = self.ui.edtDate.date()
        self._application.client = self._client
        typeIndex = self.ui.cmbApplicationType.currentIndex()
        self._application.type = self.ui.cmbApplicationType.model().item(typeIndex)
        self._application.entries = self.ui.tblElevatorsData.model().getApplicationEntries()
        return self._application

    def setApplication(self, application: Application):
        self._application = application
        self.ui.edtDate.setDate(application.date)
        self._client = application.client
        self.ui.lblClient.setText(application.client.short_name)
        self.ui.cmbApplicationType.setCurrentIndex(self.ui.cmbApplicationType.model().getIndexById(application.type.id))
        self.ui.tblElevatorsData.model().setApplicationEntries(application.entries)
