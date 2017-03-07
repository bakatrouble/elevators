from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWizard

from applications.models.application_type import ApplicationTypeModel
from shared.client_dialog import ClientDialog
from shared.models.client_model import ClientModel
from ui.applications.application_wizard import Ui_ApplicationWizard


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

    def addTableItem(self):
        self.ui.tblElevatorsData.model().addItem()

    def removeTableItem(self):
        rows = {index.row() for index in self.ui.tblElevatorsData.selectedIndexes()}
        self.ui.tblElevatorsData.model().removeItems(rows)

    def selectClient(self):
        dlg = ClientDialog(self)
        if dlg.exec() == ClientDialog.Accepted:
            self._client = ClientModel.getItemById(dlg.getResult())
            if self._client:
                self.ui.lblCustomer.setText(self._client.short_name)
