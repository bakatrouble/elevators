from datetime import date

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

from models.application_type import ApplicationType, ApplicationTypeModel
from models.base_model import BaseModel
from models.client import ClientModel


class ApplicationEntry:
    def __init__(self):
        self.id = None
        self.address_oblast = ''
        self.address_raion = ''
        self.address_city = ''
        self.address_street = ''
        self.address_house = ''
        self.address_building = ''
        self.address_letter = ''
        self.purpose = ''
        self.number = ''
        self.maker = ''
        self.load = ''
        self.stops = ''
        self.speed = ''
        self.date = ''
        self.replacements = ''
        self.deadline = ''
        
    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.address_oblast = data['address_oblast']
        obj.address_raion = data['address_raion']
        obj.address_city = data['address_city']
        obj.address_street = data['address_street']
        obj.address_house = data['address_house']
        obj.address_building = data['address_building']
        obj.address_letter = data['address_letter']
        obj.purpose = data['purpose']
        obj.number = data['number']
        obj.maker = data['maker']
        obj.load = data['load']
        obj.stops = data['stops']
        obj.speed = data['speed']
        obj.date = data['date']
        obj.replacements = data['replacements']
        obj.deadline = data['deadline']
        return obj

    @classmethod
    def fromDataTableItem(cls, item):
        obj = cls()
        obj.id = None
        obj.address_oblast = item.address.oblast
        obj.address_raion = item.address.raion
        obj.address_city = item.address.city
        obj.address_street = item.address.street
        obj.address_house = item.address.house
        obj.address_building = item.address.building
        obj.address_letter = item.address.letter
        obj.purpose = item.purpose
        obj.number = item.number
        obj.maker = item.maker
        obj.load = item.load
        obj.stops = item.stops
        obj.speed = item.speed
        obj.date = item.date
        obj.replacements = item.replacements
        obj.deadline = item.deadline
        return obj


class Application:
    def __init__(self):
        self.id = None
        self.date = date.today()
        self.type = None
        self.client = None
        self.entries = []
        
    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.date = data['date']
        obj.type = ApplicationTypeModel.getItemById(data['type'])
        obj.client = ClientModel.getItemById(data['client'])
        for item in data['entries']:
            obj.entries.append(ApplicationEntry.fromDict(item))
        return obj


class ApplicationModel(QAbstractTableModel, BaseModel):
    _items = []
    url = 'api/applications/'
    item_class = Application

    @classmethod
    def data(cls, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return QDate(cls._items[row].date).toString(Qt.DefaultLocaleShortDate)
            elif column == 1:
                return cls._items[row].client.short_name if cls._items[row].client else ''
            elif column == 2:
                return cls._items[row].type.name
        return None

    def columnCount(self, *args, **kwargs):
        return 3

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole:
            if column == 0:
                return 'Дата создания'
            elif column == 1:
                return 'Заказчик'
            elif column == 2:
                return 'Тип заявки'
        return None
