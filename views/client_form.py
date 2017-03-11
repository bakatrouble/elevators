from PyQt5.QtWidgets import QDialog

from models.client import Client
from ui.shared.client_form import Ui_CustomerForm


class ClientForm(QDialog):
    def __init__(self, parent=None):
        super(ClientForm, self).__init__(parent)
        self.ui = Ui_CustomerForm()
        self.ui.setupUi(self)

        self._client = Client()

    def setClient(self, client):
        self._client = client
        self.ui.edtFullName.setText(self._client.full_name)
        self.ui.edtShortName.setText(self._client.short_name)
        self.ui.edtRegistrationAddress.setText(self._client.registration_address)
        self.ui.edtLocationAddress.setText(self._client.location_address)
        self.ui.edtPhone.setText(self._client.phone)
        self.ui.edtINN.setText(self._client.inn)
        self.ui.edtKPP.setText(self._client.kpp)
        self.ui.edtAccount.setText(self._client.account_number)
        self.ui.edtBank.setText(self._client.bank)
        self.ui.edtBIK.setText(self._client.bik)
        self.ui.edtOGRN.setText(self._client.ogrn)
        self.ui.edtPersonName.setText(self._client.person_name)
        self.ui.edtPersonPost.setText(self._client.person_post)

    def getClient(self):
        self._client.full_name = self.ui.edtFullName.text()
        self._client.short_name = self.ui.edtShortName.text()
        self._client.registration_address = self.ui.edtRegistrationAddress.text()
        self._client.location_address = self.ui.edtLocationAddress.text()
        self._client.phone = self.ui.edtPhone.text()
        self._client.inn = self.ui.edtINN.text()
        self._client.kpp = self.ui.edtKPP.text()
        self._client.account_number = self.ui.edtAccount.text()
        self._client.bank = self.ui.edtBank.text()
        self._client.bik = self.ui.edtBIK.text()
        self._client.ogrn = self.ui.edtOGRN.text()
        self._client.person_name = self.ui.edtPersonName.text()
        self._client.person_post = self.ui.edtPersonName.text()
        self._client._changed = True
        return self._client
