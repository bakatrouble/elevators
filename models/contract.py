from PyQt5.QtCore import QAbstractTableModel, QDate, Qt

from models.base_model import BaseModel
from models.client import ClientModel


class Contract:
    def __init__(self):
        self.id = None
        self.application_id = None
        self.number = ''
        self.date = QDate().currentDate()
        self.finish_date = QDate().currentDate()
        self.price = 0.
        self.terms = ''
        self.client = None
        self.poa = False
        self.poa_number = ''
        self.poa_date = QDate().currentDate()

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.application_id = data['application']
        obj.number = data['number']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        obj.finish_date = QDate().fromString(data['finish_date'], 'yyyy-MM-dd')
        obj.price = data['price']
        obj.terms = data['terms']
        obj.client = ClientModel.getItemById(data['client'])
        obj.poa = data['poa']
        obj.poa_number = data['poa_number']
        obj.poa_date = QDate().fromString(data['poa_date'], 'yyyy-MM-dd')
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'application': self.application_id,
            'number': self.number,
            'date': self.date.toString('yyyy-MM-dd'),
            'finish_date': self.finish_date.toString('yyyy-MM-dd'),
            'price': self.price,
            'terms': self.terms,
            'poa': self.poa,
            'poa_number': self.poa_number,
            'poa_date': self.poa_date.toString('yyyy-MM-dd'),
        }


class ContractModel(QAbstractTableModel, BaseModel):
    _items = []
    url = 'api/contracts/'
    item_class = Contract

    @classmethod
    def data(cls, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return cls._items[row].number
            elif column == 1:
                return QDate(cls._items[row].date).toString(Qt.DefaultLocaleShortDate)
            elif column == 2:
                return cls._items[row].client.short_name if cls._items[row].client else ''
            elif column == 3:
                return cls._items[row].price
        return None

    def columnCount(self, *args, **kwargs):
        return 4

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole:
            if column == 0:
                return 'Номер'
            elif column == 1:
                return 'Дата'
            elif column == 2:
                return 'Заказчик'
            elif column == 3:
                return 'Сумма'
        return None
