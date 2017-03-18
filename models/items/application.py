from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QStyledItemDelegate, QSpinBox, QDateEdit

from models.items.contract import Contract
from models.items.account import Account
from models.items.address import Address
from models.items.order import Order
from views.address import AddressDialog
from models import Models


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
        obj.type = Models.get().application_types.getItemById(data['type'])
        obj.client = Models.get().clients.getItemById(data['client'])
        for item in data['entries']:
            obj.entries.append(ApplicationEntry.fromDict(item))
        if data['contract']:
            obj.contract = Contract.fromDict(data['contract'])
        if data['account']:
            obj.account = Account.fromDict(data['account'])
        if data['order']:
            obj.order = Order.fromDict(data['order'])
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'date': self.date.toString('yyyy-MM-dd'),
            'type': self.type.id,
            'client': self.client.id if self.client else None,
            'entries': [entry.toDict() for entry in self.entries]
        }


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
