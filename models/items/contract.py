from PyQt5.QtCore import QDate

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