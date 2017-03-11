from PyQt5.QtWidgets import QDialog

from models.contract import Contract
from models.application import Application

from controllers.client import ClientController
from ui.contracts.contract_form import Ui_ContractForm


class ContractForm(QDialog):
    def __init__(self, parent=None):
        super(ContractForm, self).__init__(parent)
        self.ui = Ui_ContractForm()
        self.ui.setupUi(self)

        self.setupSignals()
        self.setupUi()

        self._client = None
        self._contract = Contract()

    def setupSignals(self):
        # self.ui.btnSelectClient.clicked.connect(self.selectClient)
        pass

    def setupUi(self):
        self.ui.wdgPOA.setVisible(False)

    def selectClient(self):
        result, client = ClientController.choose(self)
        if result == QDialog.Accepted and client:
            self._contract.client = client
            self.ui.lblClient.setText(client.short_name)

    def setApplication(self, application: Application):
        self._contract.application_id = application.id
        self._client = application.client
        self.ui.lblClient.setText(application.client.short_name)

    def getContract(self):
        self._contract.number = self.ui.edtContractNumber.text()
        self._contract.date = self.ui.edtContractDate.date()
        self._contract.finish_date = self.ui.edtContractFinishDate.date()
        self._contract.price = self.ui.edtPrice.value()
        self._contract.terms = self.ui.edtPaymentTerms.toHtml()
        self._contract.client = self._client
        self._contract.poa = self.ui.chkPOA.isChecked()
        if self.ui.chkPOA.isChecked():
            self._contract.poa_number = self.ui.edtPOANumber.text()
            self._contract.poa_date = self.ui.edtPOADate.date()
        return self._contract

    def setContract(self, contract: Contract):
        self._contract = contract
        self._client = contract.client
        self.ui.edtContractNumber.setText(contract.number)
        self.ui.edtContractDate.setDate(contract.date)
        self.ui.edtContractFinishDate.setDate(contract.finish_date)
        self.ui.edtPrice.setValue(contract.price)
        self.ui.edtPaymentTerms.setHtml(contract.terms)
        self.ui.lblClient.setText(contract.client.short_name)
        self.ui.chkPOA.setChecked(contract.poa)
        if contract.poa:
            self.ui.edtPOANumber.setText(contract.poa_number)
            self.ui.edtPOADate.setDate(contract.poa_date)
