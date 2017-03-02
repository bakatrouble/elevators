from PyQt5.QtWidgets import QDialog

from ui.shared.customer_form import Ui_CustomerForm


class CustomerForm(QDialog):
    def __init__(self, parent=None):
        super(CustomerForm, self).__init__(parent)
        self.ui = Ui_CustomerForm()
        self.ui.setupUi(self)
