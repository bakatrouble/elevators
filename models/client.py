from PyQt5.QtCore import Qt, QStringListModel

from models.base_model import BaseModel
from models.items.client import Client


class ClientModel(QStringListModel, BaseModel):
    _items = []
    url = 'api/clients/'
    item_class = Client

    # def __init__(self):
        # self._items = Options.get().

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            item = self._items[row]
            if item.id:
                return '№%d %s' % (item.id, item.short_name)
            else:
                return '[Локальный] %s' % item.short_name
        return None

    def columnCount(self, *args, **kwargs):
        return 1
