from PyQt5.QtCore import QDate


class Account:
    def __init__(self):
        self.id = None
        self.application_id = None
        self.number = ''
        self.date = QDate().currentDate()

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.application_id = data['application']
        obj.number = data['number']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'application': self.application_id,
            'number': self.number,
            'date': self.date.toString('yyyy-MM-dd')
        }