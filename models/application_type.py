from PyQt5.QtCore import Qt, QStringListModel

from models.base_model import BaseModel


class ApplicationType:
    def __init__(self):
        self.id = None
        self.name = ''
        self.hints = ''
        self.application_template = ''
        self.contract_template = ''
        self.account_template = ''
        self.order_template = ''

        self._changed = False

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.name = data['name']
        obj.hints = data['hints']
        obj.application_template = data['application_template']
        obj.contract_template = data['contract_template']
        obj.account_template = data['account_template']
        obj.order_template = data['order_template']
        return obj
    
    # def toDict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'hints': self.hints,
    #         'application_template': self.application_template,
    #         'contract_template': self.contract_template,
    #         'order_template': self.order_template,
    #     }


class ApplicationTypeModel(QStringListModel, BaseModel):
    _items = []
    url = 'api/application_types/'
    item_class = ApplicationType

    @classmethod
    def data(cls, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            return cls._items[row].name
        return None

    def columnCount(self, *args, **kwargs):
        return 1
