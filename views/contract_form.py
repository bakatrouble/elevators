from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog

from models.items.contract import Contract
from models.items.application import Application

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
        self.ui.edtContractDate.setDate(QDate().currentDate())
        self.ui.edtContractFinishDate.setDate(QDate().currentDate())
        self.ui.edtPOAClientDate.setDate(QDate().currentDate())
        self.ui.edtPOAContractorDate.setDate(QDate().currentDate())

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
        self._contract.poa_client = self.ui.chkPOAClient.isChecked()
        if self.ui.chkPOAClient.isChecked():
            self._contract.poa_client_number = self.ui.edtPOAClientNumber.text()
            self._contract.poa_client_date = self.ui.edtPOAClientDate.date()
        self._contract.poa_contractor = self.ui.chkPOAContractor.isChecked()
        if self.ui.chkPOAContractor.isChecked():
            self._contract.poa_contractor_number = self.ui.edtPOAContractorNumber.text()
            self._contract.poa_contractor_date = self.ui.edtPOAContractorDate.date()
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
        self.ui.chkPOAClient.setChecked(contract.poa_client)
        if contract.poa_client:
            self.ui.edtPOAClientNumber.setText(contract.poa_client_number)
            self.ui.edtPOAClientDate.setDate(contract.poa_client_date)
        self.ui.chkPOAContractor.setChecked(contract.poa_contractor)
        if contract.poa_contractor:
            self.ui.edtPOAContractorNumber.setText(contract.poa_contractor_number)
            self.ui.edtPOAContractorDate.setDate(contract.poa_contractor_date)
