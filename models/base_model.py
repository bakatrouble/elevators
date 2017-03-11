import json

import requests
from PyQt5.QtCore import QAbstractItemModel, QModelIndex


class BaseModel(QAbstractItemModel):
    item_class = None
    url = ''
    _items = []

    def __init__(self):
        super(BaseModel, self).__init__()
        if not self._items:
            self.loadData()

    @classmethod
    def loadData(cls):
        data = requests.get('http://127.0.0.1:8000/' + cls.url).json()
        cls._items = []
        for item in data:
            cls._items.append(cls.item_class.fromDict(item))

    @classmethod
    def saveItem(cls, item):
        print(json.dumps(item.toDict()))
        if item.id is None:
            data = requests.post('http://127.0.0.1:8000/' + cls.url, json=item.toDict()).json()
            item.id = data['id']
        else:
            requests.put('http://127.0.0.1:8000/' + cls.url + str(item.id) + '/', json=item.toDict())

    @classmethod
    def data(cls, index, role=None):
        raise NotImplementedError

    def index(self, row, column=0, parent=None, *args, **kwargs):
        if 0 <= row < len(self._items):
            return self.createIndex(row, column, self._items[row])
        return QModelIndex()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def getItemById(cls, item_id):
        try:
            return next(x for x in cls._items if x.id == item_id)
        except StopIteration:
            return None

    @classmethod
    def getIndexById(cls, item_id):
        try:
            return cls._items.index(cls.getItemById(item_id))
        except IndexError:
            return 0

    @classmethod
    def addItem(cls, item):
        cls._items.append(item)

    @classmethod
    def item(cls, index):
        return cls._items[index]
