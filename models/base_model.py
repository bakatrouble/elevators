import requests


class BaseModel:
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
        try:
            return next(x for x in cls._items if x.id == item_id)
        except StopIteration:
            return None

    @classmethod
    def addItem(cls, item):
        cls._items.append(item)
