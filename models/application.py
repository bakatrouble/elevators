from PyQt5.QtCore import QAbstractTableModel, QModelIndex
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QLineEdit, QWidget, QSpinBox, QDateEdit

from models.application_type import ApplicationTypeModel
from models.base_model import BaseModel
from models.client import ClientModel
from models.contract import Contract
from shared.address import Address, AddressDialog


class ApplicationEntry:
    def __init__(self):
        self.id = None
        self.address = Address()
        self.purpose = ''
        self.number = ''
        self.maker = ''
        self.load = ''
        self.stops = 0
        self.speed = ''
        self.date = QDate().currentDate()
        self.deadline = ''
        self.replacements = ''

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.address.oblast = data['address_oblast']
        obj.address.raion = data['address_raion']
        obj.address.city = data['address_city']
        obj.address.street = data['address_street']
        obj.address.house = data['address_house']
        obj.address.building = data['address_building']
        obj.address.letter = data['address_letter']
        obj.purpose = data['purpose']
        obj.number = data['number']
        obj.maker = data['maker']
        obj.load = data['load']
        obj.stops = data['stops']
        obj.speed = data['speed']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        obj.replacements = data['replacements']
        obj.deadline = data['deadline']
        return obj
    
    def toDict(self):
        return {
            'id': self.id,
            'address_oblast': self.address.oblast,
            'address_raion': self.address.raion,
            'address_city': self.address.city,
            'address_street': self.address.street,
            'address_house': self.address.house,
            'address_building': self.address.building,
            'address_letter': self.address.letter,
            'purpose': self.purpose,
            'number': self.number,
            'maker': self.maker,
            'load': self.load,
            'stops': self.stops,
            'speed': self.speed,
            'date': self.date.toString('yyyy-MM-dd'),
            'replacements': self.replacements,
            'deadline': self.deadline,
        }

    def data(self, row, column):
        if column == 0:
            return str(row+1)
        elif column == 1:
            return str(self.address)
        elif column == 2:
            return self.purpose
        elif column == 3:
            return self.number
        elif column == 4:
            return self.maker
        elif column == 5:
            return self.load
        elif column == 6:
            return str(self.stops)
        elif column == 7:
            return self.speed
        elif column == 8:
            return self.date.toString(Qt.DefaultLocaleShortDate)
        elif column == 9:
            return self.deadline
        elif column == 10:
            return self.replacements

    def createEditor(self, parent, option, index, delegate):
        column = index.column()
        editor = None
        if column not in (1, 6, 8):
            editor = QLineEdit(parent)
        elif column == 1:
            editor = QWidget(parent)
            editor.dialog = AddressDialog(editor)
            editor.dialog.accepted.connect(lambda: delegate.closeEditor.emit(editor, QStyledItemDelegate.NoHint))
            editor.dialog.rejected.connect(lambda: delegate.closeEditor.emit(editor, QStyledItemDelegate.NoHint))
        elif column == 6:
            editor = QSpinBox(parent)
        elif column == 8:
            editor = QDateEdit(parent)
            editor.setCalendarPopup(True)
        return editor

    def setEditorData(self, editor, index, delegate):
        column = index.column()
        if column == 1:
            editor.dialog.setAddress(self.address)
            editor.dialog.show()
        elif column == 2:
            editor.setText(self.purpose)
        elif column == 3:
            editor.setText(self.number)
        elif column == 4:
            editor.setText(self.maker)
        elif column == 5:
            editor.setText(self.load)
        elif column == 6:
            editor.setValue(self.stops)
        elif column == 7:
            editor.setText(self.speed)
        elif column == 8:
            editor.setDate(self.date)
        elif column == 9:
            editor.setText(self.deadline)
        elif column == 10:
            editor.setText(self.replacements)

    def setModelData(self, editor, model, index, delegate):
        column = index.column()

        if column == 2:
            self.purpose = editor.text()
        elif column == 3:
            self.number = editor.text()
        elif column == 4:
            self.maker = editor.text()
        elif column == 5:
            self.load = editor.text()
        elif column == 6:
            self.stops = editor.value()
        elif column == 7:
            self.speed = editor.text()
        elif column == 8:
            self.date = editor.date()
        elif column == 9:
            self.deadline = editor.text()
        elif column == 10:
            self.replacements = editor.text()


class Application:
    def __init__(self):
        self.id = None
        self.date = QDate().currentDate()
        self.type = None
        self.client = None
        self.entries = []

        self.contract = None
        self.account = None
        self.order = None
        self.protocols = []

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.date = QDate().fromString(data['date'], 'yyyy-MM-dd')
        obj.type = ApplicationTypeModel.getItemById(data['type'])
        obj.client = ClientModel.getItemById(data['client'])
        for item in data['entries']:
            obj.entries.append(ApplicationEntry.fromDict(item))
        if data['contract']:
            obj.contract = Contract.fromDict(data['contract'])
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'date': self.date.toString('yyyy-MM-dd'),
            'type': self.type.id,
            'client': self.client.id,
            'entries': [entry.toDict() for entry in self.entries]
        }


class ApplicationModel(QAbstractTableModel, BaseModel):
    _items = []
    url = 'api/applications/'
    item_class = Application

    @classmethod
    def data(cls, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            return '№%s от %s, %s, %s' % (cls._items[row].id, cls._items[row].date.toString(Qt.DefaultLocaleShortDate),
                                          cls._items[row].client.short_name, cls._items[row].type.name)
        return None

    def columnCount(self, *args, **kwargs):
        return 1


class DataTableModel(QAbstractTableModel):
    item_class = ApplicationEntry

    def __init__(self, parent=None):
        super(DataTableModel, self).__init__(parent)
        self._items = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, parent=None, *args, **kwargs):
        return 11

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                '№ п/п',
                'Адрес',
                'Назначение',
                'зав. №/рег. №',
                'Изготовитель',
                'г/п, кг',
                'Число остановок',
                'Скорость, м/с',
                'Дата',
                'Срок проведения проверки',
                'Замененные узлы',
            ][column]
        return None

    def addItem(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(self.item_class())
        self.endInsertRows()

    def removeItems(self, rows):
        rows = sorted(rows, reverse=True)
        for row in rows:
            self.beginRemoveRows(QModelIndex(), row, row)
            del self._items[row]
            self.endRemoveRows()

    def data(self, index, role=None):
        if role in (Qt.DisplayRole, Qt.ToolTipRole):
            return index.internalPointer().data(index.row(), index.column())
        return None

    def index(self, row, column, parent=None, *args, **kwargs):
        return self.createIndex(row, column, self._items[row])

    def flags(self, index):
        base = super(DataTableModel, self).flags(index)
        if index.column() == 0:
            return base
        else:
            return base | Qt.ItemIsEditable

    def getApplicationEntries(self):
        entries = []
        for item in self._items:
            entries.append(item)
        return entries

    def setApplicationEntries(self, entries):
        self._items = entries
        self.modelReset.emit()


class DataTableDelegate(QStyledItemDelegate):
    def __init__(self):
        super(DataTableDelegate, self).__init__()

    def createEditor(self, parent, option, index):
        return index.internalPointer().createEditor(parent, option, index, self)

    def setEditorData(self, editor, index):
        index.internalPointer().setEditorData(editor, index, self)

    def setModelData(self, editor, model, index):
        index.internalPointer().setModelData(editor, model, index, self)
