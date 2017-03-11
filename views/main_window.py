from PyQt5.QtWidgets import QMainWindow, QWidget

from controllers.application import ApplicationController
from controllers.contract import ContractController
from ui.shared.main_window import Ui_MainWindow
from models.application import ApplicationModel, Application


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

    def setupUi(self):
        self.ui.tblApplications.setModel(ApplicationModel())

    def setupSignals(self):
        self.ui.tblApplications.selectionModel().selectionChanged.connect(self.tblApplicationsSelectionChanged)
        self.ui.btnCreateApplication.clicked.connect(self.createApplication)
        self.ui.btnEditApplication.clicked.connect(self.editApplication)

        self.ui.btnCreateContract.clicked.connect(self.createContract)
        self.ui.btnEditContract.clicked.connect(self.editContract)

    def tblApplicationsSelectionChanged(self, selected, deselected):
        if len(self.ui.tblApplications.selectedIndexes()):
            self.ui.btnEditApplication.setEnabled(True)
            self.ui.pnlDocuments.setEnabled(True)
            # self.ui.btnPrintApplication.setEnabled(True)
            self.setupContract()
            self.setupAccount()
            self.setupOrder()
            self.setupProtocols()
        else:
            self.ui.btnEditApplication.setEnabled(False)
            self.ui.pnlDocuments.setEnabled(False)
            # self.ui.btnPrintApplication.setEnabled(False)

    def currentApplication(self) -> Application:
        return self.ui.tblApplications.currentIndex().internalPointer()

    def setupContract(self):
        if self.currentApplication().contract is not None:
            self.ui.btnEditContract.setEnabled(True)
            self.ui.btnCreateContract.setEnabled(False)
            # self.ui.btnPrintContract.setEnabled(True)
            self.ui.lblContractNumber.setText('№%s' % self.currentApplication().contract.number)
        else:
            self.ui.btnEditContract.setEnabled(False)
            self.ui.btnCreateContract.setEnabled(True)
            # self.ui.btnPrintContract.setEnabled(False)
            self.ui.lblContractNumber.setText('№')

    def setupAccount(self):
        pass

    def setupOrder(self):
        pass

    def setupProtocols(self):
        pass

    def createApplication(self):
        ApplicationController.create(self)
        self.ui.tblApplications.model().modelReset.emit()

    def editApplication(self):
        ApplicationController.edit(self.currentApplication(), self)
        self.ui.tblApplications.model().modelReset.emit()

    def createContract(self):
        ContractController.create(self.currentApplication(), self)
        self.setupContract()

    def editContract(self):
        ContractController.edit(self.currentApplication().contract)
        self.setupContract()
