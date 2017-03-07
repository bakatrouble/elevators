from PyQt5.QtWidgets import QDialog

from ui.shared.client_form import Ui_CustomerForm


class ClientForm(QDialog):
    def __init__(self, parent=None):
        super(ClientForm, self).__init__(parent)
        self.ui = Ui_CustomerForm()
        self.ui.setupUi(self)
