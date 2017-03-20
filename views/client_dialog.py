from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox

from controllers.client import ClientController
from models.client import ClientModel
from ui.shared.client_dialog import Ui_ClientDialog
from utils import Options


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
        self.ui.btnAdd.clicked.connect(self.addClient)
        self.ui.btnEdit.clicked.connect(self.editClient)
        self.ui.lstClients.doubleClicked.connect(self.accept)
        self.ui.lstClients.clicked.connect(self.selectionChanged)

    def selectionChanged(self, index):
        self._result = index.internalPointer().id
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        self.ui.btnEdit.setEnabled(not Options.get().autonomy_mode)

    def getResult(self):
        return self._result

    def getCurrent(self):
        return self.ui.lstClients.currentIndex().internalPointer()

    def addClient(self):
        ClientController.create(self) and self.ui.lstClients.reset()

    def editClient(self):
        ClientController.edit(self.getCurrent(), self) and self.ui.lstClients.reset()

