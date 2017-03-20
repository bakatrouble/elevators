from PyQt5.QtCore import QDate

from models.specialist import SpecialistModel


class Order:
    def __init__(self):
        self.id = None
        self.application_id = None
        self.number = ''
        self.date = QDate().currentDate()
        self.to_date = QDate().currentDate()
        self.act_date = QDate().currentDate()
        self.controller = ''
        self.manager = ''
        self.expert = ''
        self.head_specialist = None
        self.specialists = []

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.application_id = data['application']
        obj.number = data['number']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        obj.to_date = QDate().fromString(data['to_date'], 'yyyy-MM-dd')
        obj.act_date = QDate().fromString(data['act_date'], 'yyyy-MM-dd')
        obj.controller = data['controller']
        obj.manager = data['manager']
        obj.expert = data['expert']
        obj.head_specialist = SpecialistModel.getItemById(data['head_specialist'])
        obj.specialists = [SpecialistModel.getItemById(spec_id) for spec_id in data['specialists']]
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'application': self.application_id,
            'number': self.number,
            'date': self.date.toString('yyyy-MM-dd'),
            'to_date': self.to_date.toString('yyyy-MM-dd'),
            'act_date': self.act_date.toString('yyyy-MM-dd'),
            'controller': self.controller,
            'manager': self.manager,
            'expert': self.expert,
            'head_specialist': self.head_specialist.id if self.head_specialist else None,
            'specialists': [spec.id for spec in self.specialists]
        }