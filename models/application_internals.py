from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtWidgets import QStyledItemDelegate

from models.items.application import ApplicationEntry


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