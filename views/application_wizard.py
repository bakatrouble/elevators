from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWizard
from models.application_data import DataTableModel, DataTableDelegate

from controllers.client import ClientController
from models.application_type import ApplicationTypeModel
from models.client import ClientModel
from ui.applications.application_wizard import Ui_ApplicationWizard
from views.client_dialog import ClientDialog


class ApplicationWizard(QWizard):
    def __init__(self, parent=None):
        super(ApplicationWizard, self).__init__(parent)
        self.ui = Ui_ApplicationWizard()
        self.ui.setupUi(self)

        self.setupSignals()
        self.setupUi()

        self._client = None

    def setupSignals(self):
        self.ui.btnSelectCustomer.clicked.connect(self.selectClient)
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
            self.ui.lblCustomer.setText(client.short_name)
