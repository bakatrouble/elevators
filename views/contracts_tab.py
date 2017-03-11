from PyQt5.QtWidgets import QWidget

from controllers.contract import ContractController
from models.contract import ContractModel
from ui.contracts.contracts_tab import Ui_ContractsTab


class ContractsTab(QWidget):
    def __init__(self, parent=None):
        super(ContractsTab, self).__init__(parent)
        self.ui = Ui_ContractsTab()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

    def setupUi(self):
        self.ui.tableView.setModel(ContractModel())
        self.ui.btnCreateForm.setEnabled(False)

    def setupSignals(self):
        self.ui.btnCreateForm.clicked.connect(self.createContract)
        self.ui.tableView.doubleClicked.connect(self.editContract)

    def createContract(self):
        ContractController.create(self) and self.ui.tableView.model().modelReset.emit()

    def editContract(self):
        application = self.ui.tableView.currentIndex().internalPointer()
        ContractController.edit(application, self) and self.ui.tableView.model().modelReset.emit()

    def showEvent(self, event):
        super(ContractsTab, self).showEvent(event)
        self.ui.tableView.model().modelReset.emit()
