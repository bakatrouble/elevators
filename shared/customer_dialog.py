from PyQt5.QtWidgets import QDialog

from ui.shared.customer_dialog import Ui_CustomerDialog
from shared.customer_form import CustomerForm


class CustomerDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomerDialog, self).__init__(parent)
        self.ui = Ui_CustomerDialog()
        self.ui.setupUi(self)

        self.setupSignals()

    def setupSignals(self):
        self.ui.btnAdd.clicked.connect(self.addCustomer)

    def addCustomer(self):
        dlg = CustomerForm(self)
        if dlg.exec() == CustomerForm.Accepted:
            pass
