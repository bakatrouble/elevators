from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox

from shared.models.client_model import ClientModel
from ui.shared.client_dialog import Ui_ClientDialog
from shared.client_form import ClientForm


class ClientDialog(QDialog):
    def __init__(self, parent=None):
        super(ClientDialog, self).__init__(parent)
        self.ui = Ui_ClientDialog()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

        self._result = None

    def setupUi(self):
        self.ui.lstClients.setModel(ClientModel())
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.btnEdit.setEnabled(False)

    def setupSignals(self):
        self.ui.btnAdd.clicked.connect(self.addCustomer)
        self.ui.lstClients.doubleClicked.connect(self.accept)
        self.ui.lstClients.clicked.connect(self.selectionChanged)

    def selectionChanged(self, index):
        self._result = index.internalPointer().id
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self.ui.btnEdit.setEnabled(True)

    def getResult(self):
        return self._result

    def addCustomer(self):
        dlg = ClientForm(self)
        if dlg.exec() == ClientForm.Accepted:
            pass
