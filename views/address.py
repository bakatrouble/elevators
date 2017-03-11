from PyQt5.QtWidgets import QDialog

from models.address import Address
from ui.shared.address import Ui_AddressDialog


class AddressDialog(QDialog):
    def __init__(self, parent=None):
        super(AddressDialog, self).__init__(parent)

        self._address = Address()

        self.ui = Ui_AddressDialog()
        self.ui.setupUi(self)

        self.accepted.connect(self.saveAddress)

    def setAddress(self, address):
        self._address = address

    def showEvent(self, evt):
        self.ui.edtOblast.setText(self._address.oblast)
        self.ui.edtRaion.setText(self._address.raion)
        self.ui.edtCity.setText(self._address.city)
        self.ui.edtStreet.setText(self._address.street)
        self.ui.edtHouse.setText(self._address.house)
        self.ui.edtBuilding.setText(self._address.building)
        self.ui.edtLetter.setText(self._address.letter)
        super(AddressDialog, self).showEvent(evt)

    def saveAddress(self):
        self._address.oblast = self.ui.edtOblast.text()
        self._address.raion = self.ui.edtRaion.text()
        self._address.city = self.ui.edtCity.text()
        self._address.street = self.ui.edtStreet.text()
        self._address.house = self.ui.edtHouse.text()
        self._address.building = self.ui.edtBuilding.text()
        self._address.letter = self.ui.edtLetter.text()