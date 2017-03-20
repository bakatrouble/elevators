from PyQt5.QtCore import QDate

from models.client import ClientModel


class Contract:
    def __init__(self):
        self.id = None
        self.application_id = None
        self.number = ''
        self.date = QDate().currentDate()
        self.price = 0.
        self.terms = ''
        self.client = None
        self.poa_client = False
        self.poa_client_number = ''
        self.poa_client_date = QDate().currentDate()
        self.poa_contractor = False
        self.poa_contractor_number = ''
        self.poa_contractor_date = QDate().currentDate()

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.application_id = data['application']
        obj.number = data['number']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        obj.price = data['price']
        obj.terms = data['terms']
        obj.client = ClientModel.getItemById(data['client'])
        obj.poa = data['poa_client']
        obj.poa_number = data['poa_client_number']
        obj.poa_date = QDate().fromString(data['poa_client_date'], 'yyyy-MM-dd')
        obj.poa = data['poa_contractor']
        obj.poa_number = data['poa_contractor_number']
        obj.poa_date = QDate().fromString(data['poa_contractor_date'], 'yyyy-MM-dd')
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'application': self.application_id,
            'number': self.number,
            'date': self.date.toString('yyyy-MM-dd'),
            'price': self.price,
            'terms': self.terms,
            'poa_client': self.poa_client,
            'poa_client_number': self.poa_client_number,
            'poa_client_date': self.poa_client_date.toString('yyyy-MM-dd'),
            'poa_contractor': self.poa_contractor,
            'poa_contractor_number': self.poa_contractor_number,
            'poa_contractor_date': self.poa_contractor_date.toString('yyyy-MM-dd'),
        }