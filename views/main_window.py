from PyQt5.QtWidgets import QMainWindow, QMessageBox
from jinja2 import Template, exceptions
import sys

from controllers.account import AccountController
from controllers.contract import ContractController
from controllers.order import OrderController
from ui.shared.main_window import Ui_MainWindow
from models import Models
from utils import Options, die
from views.print_dialog import PrintDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

    def setupUi(self):
        self.ui.tblApplications.setModel(Models.get().applications)

    def setupSignals(self):
        self.ui.tblApplications.selectionModel().selectionChanged.connect(self.tblApplicationsSelectionChanged)
        self.ui.btnCreateApplication.clicked.connect(self.createApplication)
        self.ui.btnEditApplication.clicked.connect(self.editApplication)
        self.ui.btnPrintApplication.clicked.connect(self.printApplication)

        self.ui.btnCreateContract.clicked.connect(self.createContract)
        self.ui.btnEditContract.clicked.connect(self.editContract)
        self.ui.btnPrintContract.clicked.connect(self.printContract)

        self.ui.btnCreateAccount.clicked.connect(self.createAccount)
        self.ui.btnEditAccount.clicked.connect(self.editAccount)
        self.ui.btnPrintAccount.clicked.connect(self.printAccount)

        self.ui.btnCreateOrder.clicked.connect(self.createOrder)
        self.ui.btnEditOrder.clicked.connect(self.editOrder)
        self.ui.btnPrintOrder.clicked.connect(self.printOrder)

        self.ui.actExit.triggered.connect(die)

    def tblApplicationsSelectionChanged(self, selected, deselected):
        if len(self.ui.tblApplications.selectedIndexes()):
            self.ui.btnEditApplication.setEnabled(not Options.get().autonomy_mode)
            self.ui.pnlDocuments.setEnabled(bool(self.currentApplication().id))
            self.ui.btnPrintApplication.setEnabled(True)
            self.setupContract()
            self.setupAccount()
            self.setupOrder()
            self.setupProtocols()
        else:
            self.ui.btnEditApplication.setEnabled(False)
            self.ui.pnlDocuments.setEnabled(False)
            self.ui.btnPrintApplication.setEnabled(False)

    def currentApplication(self):
        return self.ui.tblApplications.currentIndex().internalPointer()

    def setupContract(self):
        has_perms = Options.get().group in ('supervisor', 'accounting')
        if self.currentApplication().contract is not None:
            self.ui.btnEditContract.setEnabled(has_perms)
            self.ui.btnCreateContract.setEnabled(False)
            self.ui.btnPrintContract.setEnabled(True)
            self.ui.lblContractNumber.setText('№%s' % self.currentApplication().contract.number)
        else:
            self.ui.btnEditContract.setEnabled(False)
            self.ui.btnCreateContract.setEnabled(has_perms)
            self.ui.btnPrintContract.setEnabled(False)
            self.ui.lblContractNumber.setText('не создан')

    def setupAccount(self):
        has_perms = self.currentApplication().contract is not None and \
                    Options.get().group in ('supervisor', 'accounting')
        if self.currentApplication().account is not None:
            self.ui.btnEditAccount.setEnabled(has_perms)
            self.ui.btnCreateAccount.setEnabled(False)
            self.ui.btnPrintAccount.setEnabled(True)
            self.ui.lblAccountNumber.setText('№%s' % self.currentApplication().account.number)
        else:
            self.ui.btnEditAccount.setEnabled(False)
            self.ui.btnCreateAccount.setEnabled(has_perms)
            self.ui.btnPrintAccount.setEnabled(False)
            self.ui.lblAccountNumber.setText('не создан')

    def setupOrder(self):
        has_perms = self.currentApplication().contract is not None and \
                    self.currentApplication().account is not None and \
                    Options.get().group in ('supervisor', 'secretary', 'testing')
        if self.currentApplication().order is not None:
            self.ui.btnEditOrder.setEnabled(has_perms)
            self.ui.btnCreateOrder.setEnabled(False)
            self.ui.btnPrintOrder.setEnabled(True)
            self.ui.lblOrderNumber.setText('№%s' % self.currentApplication().order.number)
        else:
            self.ui.btnEditOrder.setEnabled(False)
            self.ui.btnCreateOrder.setEnabled(has_perms)
            self.ui.btnPrintOrder.setEnabled(False)
            self.ui.lblOrderNumber.setText('не создан')

    def setupProtocols(self):
        pass

    def createApplication(self):
        Models.get().applications.createApplication(self)

    def editApplication(self):
        Models.get().applications.editApplication(self.ui.tblApplications.currentIndex(), self)

    def printApplication(self):
        try:
            template = Template(self.currentApplication().type.application_template)
            dlg = PrintDialog(self)
            dlg.showDialog(template.render(application=self.currentApplication()))
        except exceptions.TemplateSyntaxError as e:
            QMessageBox().warning(self, 'Ошибка',
                                  'Произошла ошибка при печати шаблона:\n%s\n(Строка %s)' % (e.message, e.lineno))
            return
        except exceptions.TemplateError as e:
            QMessageBox().warning(self, 'Ошибка', 'Произошла ошибка при печати шаблона:\n%s' % e.message)
            return

    def createContract(self):
        ContractController.create(self.currentApplication(), self)
        self.setupContract()

    def editContract(self):
        ContractController.edit(self.currentApplication().contract, self)
        self.setupContract()

    def printContract(self):
        try:
            template = Template(self.currentApplication().type.contract_template)
            dlg = PrintDialog(self)
            dlg.showDialog(template.render(
                application=self.currentApplication(),
                contract=self.currentApplication().contract
            ))
        except exceptions.TemplateSyntaxError as e:
            QMessageBox().warning(self, 'Ошибка',
                                  'Произошла ошибка при печати шаблона:\n%s\n(Строка %s)' % (e.message, e.lineno))
            return
        except exceptions.TemplateError as e:
            QMessageBox().warning(self, 'Ошибка', 'Произошла ошибка при печати шаблона:\n%s' % e.message)
            return

    def createAccount(self):
        AccountController.create(self.currentApplication(), self)
        self.setupAccount()

    def editAccount(self):
        AccountController.edit(self.currentApplication().account, self)
        self.setupAccount()

    def printAccount(self):
        try:
            template = Template(self.currentApplication().type.account_template)
            dlg = PrintDialog(self)
            dlg.showDialog(template.render(
                application=self.currentApplication(),
                contract=self.currentApplication().contract,
                account=self.currentApplication().account
            ))
        except exceptions.TemplateSyntaxError as e:
            QMessageBox().warning(self, 'Ошибка',
                                  'Произошла ошибка при печати шаблона:\n%s\n(Строка %s)' % (e.message, e.lineno))
            return
        except exceptions.TemplateError as e:
            QMessageBox().warning(self, 'Ошибка', 'Произошла ошибка при печати шаблона:\n%s' % e.message)
            return

    def createOrder(self):
        OrderController.create(self.currentApplication(), self)
        self.setupOrder()

    def editOrder(self):
        OrderController.edit(self.currentApplication().order, self)
        self.setupOrder()

    def printOrder(self):
        try:
            template = Template(self.currentApplication().type.order_template)
            dlg = PrintDialog(self)
            dlg.showDialog(template.render(
                application=self.currentApplication(),
                contract=self.currentApplication().contract,
                account=self.currentApplication().account,
                order=self.currentApplication().order
            ))
        except exceptions.TemplateSyntaxError as e:
            QMessageBox().warning(self, 'Ошибка',
                                  'Произошла ошибка при печати шаблона:\n%s\n(Строка %s)' % (e.message, e.lineno))
            return
        except exceptions.TemplateError as e:
            QMessageBox().warning(self, 'Ошибка', 'Произошла ошибка при печати шаблона:\n%s' % e.message)
            return
