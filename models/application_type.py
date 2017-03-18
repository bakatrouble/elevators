from PyQt5.QtCore import Qt, QStringListModel

from models.base_model import BaseModel
from models.items.application_type import ApplicationType


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
