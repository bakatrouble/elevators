from PyQt5.QtCore import Qt, QStringListModel

from models.base_model import BaseModel


class Client:
    def __init__(self):
        self.id = None
        self.full_name = ''
        self.short_name = ''
        self.registration_address = ''
        self.location_address = ''
        self.phone = ''
        self.inn = ''
        self.kpp = ''
        self.account_number = ''
        self.bank = ''
        self.bik = ''
        self.ogrn = ''

        self._changed = False

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.full_name = data['full_name']
        obj.short_name = data['short_name']
        obj.registration_address = data['registration_address']
        obj.location_address = data['location_address']
        obj.phone = data['phone']
        obj.inn = data['inn']
        obj.kpp = data['kpp']
        obj.account_number = data['account_number']
        obj.bank = data['bank']
        obj.bik = data['bik']
        obj.ogrn = data['ogrn']
        return obj
    
    def toDict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'short_name': self.short_name,
            'registration_address': self.registration_address,
            'location_address': self.location_address,
            'phone': self.phone,
            'inn': self.inn,
            'kpp': self.kpp,
            'account_number': self.account_number,
            'bank': self.bank,
            'bik': self.bik,
            'ogrn': self.ogrn,
        }


class ClientModel(QStringListModel, BaseModel):
    _items = []
    url = 'api/clients/'
    item_class = Client

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            return self._items[row].short_name
        return None

    def columnCount(self, *args, **kwargs):
        return 1
