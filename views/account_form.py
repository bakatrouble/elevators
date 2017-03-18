from PyQt5.QtWidgets import QDialog

from models.items.account import Account
from models.items.application import Application

from ui.accounts.account_form import Ui_AccountForm


class AccountForm(QDialog):
    def __init__(self, parent=None):
        super(AccountForm, self).__init__(parent)
        self.ui = Ui_AccountForm()
        self.ui.setupUi(self)

        self._account = Account()

    def setApplication(self, application: Application):
        self._account.application_id = application.id

    def getAccount(self):
        self._account.number = self.ui.edtNumber.text()
        self._account.date = self.ui.edtDate.date()
        return self._account

    def setAccount(self, account: Account):
        self._account = account
        self.ui.edtNumber.setText(account.number)
        self.ui.edtDate.setDate(account.date)
