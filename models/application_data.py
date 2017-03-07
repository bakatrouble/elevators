from datetime import date

from PyQt5.QtCore import QAbstractTableModel, QAbstractItemModel, QModelIndex, Qt, QDate
from PyQt5.QtWidgets import QDateEdit, QLineEdit, QSpinBox, QStyledItemDelegate, QWidget

from shared.address import Address, AddressDialog


class DataTableItem:
    def __init__(self):
        self.address = Address()
        self.purpose = ''
        self.number = ''
        self.maker = ''
        self.load = ''
        self.stops = 0
        self.speed = ''
        self.date = date.today()
        self.deadline = ''
        self.replacements = ''

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
            return QDate(self.date).toString(Qt.DefaultLocaleShortDate)
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
            self.date = editor.date().toPyDate()
        elif column == 9:
            self.deadline = editor.text()
        elif column == 10:
            self.replacements = editor.text()


class DataTableDelegate(QStyledItemDelegate):
    def __init__(self):
        super(DataTableDelegate, self).__init__()

    def createEditor(self, parent, option, index):
        return index.internalPointer().createEditor(parent, option, index, self)

    def setEditorData(self, editor, index):
        index.internalPointer().setEditorData(editor, index, self)

    def setModelData(self, editor, model, index):
        index.internalPointer().setModelData(editor, model, index, self)


class DataTableModel(QAbstractTableModel):
    item_class = DataTableItem

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
