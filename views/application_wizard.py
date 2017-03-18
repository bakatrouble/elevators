from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWizard

from models.application_internals import DataTableModel, DataTableDelegate
from models.items.application import Application
from models.items.client import Client
from models import Models

from controllers.client import ClientController
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
        self.ui.cmbApplicationType.setModel(Models.get().application_types)
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
        if not self._client:
            self._client = Client()
            self._client.short_name = '<без названия>'
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
