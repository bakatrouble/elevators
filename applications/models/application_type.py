from PyQt5.QtCore import Qt, QStringListModel

from shared.models.rest_model import RestApiModel


class ApplicationType:
    def __init__(self):
        self.id = None
        self.name = ''
        self.hints = ''
        self.application_template = ''
        self.contract_template = ''
        self.order_template = ''

    @classmethod
    def from_dict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.name = data['name']
        obj.hints = data['hints']
        obj.application_template = data['application_template']
        obj.contract_template = data['contract_template']
        obj.order_template = data['order_template']
        return obj


class ApplicationTypeModel(QStringListModel, RestApiModel):
    _items = []
    url = 'api/application_types/'
    item_class = ApplicationType

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            return self._items[row].name
        return None

    def columnCount(self, *args, **kwargs):
        return 1
