from PyQt5.QtCore import QStringListModel, Qt, QModelIndex
from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate

from models.items.specialist import Specialist
from .base_model import BaseModel


class SpecialistModel(QStringListModel, BaseModel):
    _items = []
    url = 'api/specialists/'
    item_class = Specialist

    @classmethod
    def data(cls, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            return cls._items[row].fullName()
        elif role == Qt.UserRole:
            row = index.row()
            return cls._items[row]
        return None

    def columnCount(self, *args, **kwargs):
        return 1


class SpecialistComboBox(QComboBox):
    def __init__(self, parent=None):
        super(SpecialistComboBox, self).__init__(parent)
        self.setModel(SpecialistModel())


class SpecialistItemDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return SpecialistComboBox(parent)

    def setEditorData(self, editor: SpecialistComboBox, index):
        specialist = index.internalPointer()
        if specialist is not None:
            editor.setCurrentIndex(SpecialistModel.getIndexById(specialist.id))

    def setModelData(self, editor, model, index):
        model.setItem(index.row(), editor.currentData(Qt.UserRole))


class SpecialistListModel(QStringListModel):
    def __init__(self):
        super(SpecialistListModel, self).__init__()
        self._items = []

    def data(self, index, role=None):
        if role == Qt.DisplayRole:
            row = index.row()
            if self._items[row] is None:
                return '<не выбран>'
            else:
                return self._items[row].fullName()
        elif role == Qt.UserRole:
            row = index.row()
            return self._items[row]
        return None

    def addItem(self):
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items))
        self._items.append(None)
        self.endInsertRows()

    def setItem(self, row, value):
        self._items[row] = value

    def removeItem(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._items[row]
        self.endRemoveRows()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, *args, **kwargs):
        return 1

    def index(self, row, column=0, parent=None, *args, **kwargs):
        return self.createIndex(row, column, self._items[row])

    def getSpecialists(self):
        return [x for x in self._items if x is not None]

    def setSpecialists(self, specialists):
        self.beginResetModel()
        self._items = []
        for spec in specialists:
            self._items.append(spec)
        self.endResetModel()
