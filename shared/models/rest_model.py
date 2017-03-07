import requests


class RestApiModel:
    item_class = None
    url = ''
    _items = []

    def __init__(self):
        super(RestApiModel, self).__init__()
        if not self._items:
            self.loadData()

    @classmethod
    def loadData(cls):
        data = requests.get('http://127.0.0.1:8000/' + cls.url).json()
        cls._items = []
        for item in data:
            cls._items.append(cls.item_class.from_dict(item))

    def data(self, index, role):
        raise NotImplementedError

    def index(self, row, column=0, parent=None, *args, **kwargs):
        return self.createIndex(row, column, self._items[row])

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def getItemById(cls, item_id):
        item = list(filter(lambda x: x.id == item_id, cls._items))
        return item[0] if item else None
