from collections import OrderedDict
from datetime import date

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QDate
from PyQt5.QtWidgets import QDateEdit, QLineEdit, QSpinBox, QStyledItemDelegate, QWidget

from shared.address import Address, AddressDialog


class BaseElevatorsDataTableItem:
    def __init__(self):
        self.address = Address()
        self.purpose = ''
        self.number = ''
        self.maker = ''
        self.load = ''
        self.stops = 0
        self.speed = ''

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

    def createEditor(self, parent, option, index, delegate):
        column = index.column()
        editor = None
        if column not in (1, 6):
            editor = QLineEdit(parent)
        elif column == 1:
            editor = QWidget(parent)
            editor.dialog = AddressDialog(editor)
            editor.dialog.accepted.connect(lambda: delegate.closeEditor.emit(editor, QStyledItemDelegate.NoHint))
            editor.dialog.rejected.connect(lambda: delegate.closeEditor.emit(editor, QStyledItemDelegate.NoHint))
        elif column == 6:
            return QSpinBox(parent)
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


class BaseElevatorsDataTableDelegate(QStyledItemDelegate):
    def __init__(self):
        super(BaseElevatorsDataTableDelegate, self).__init__()

    def createEditor(self, parent, option, index):
        return index.internalPointer().createEditor(parent, option, index, self)

    def setEditorData(self, editor, index):
        index.internalPointer().setEditorData(editor, index, self)

    def setModelData(self, editor, model, index):
        index.internalPointer().setModelData(editor, model, index, self)


class BaseElevatorsDataTableModel(QAbstractTableModel):
    item_class = BaseElevatorsDataTableItem

    def __init__(self, parent=None):
        super(BaseElevatorsDataTableModel, self).__init__(parent)
        self._items = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def columnCount(self, parent=None, *args, **kwargs):
        return 8

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
                'Скорость, м/с'
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
        base = super(BaseElevatorsDataTableModel, self).flags(index)
        if index.column() == 0:
            return base
        else:
            return base | Qt.ItemIsEditable


class ElevatorsInspectionItem(BaseElevatorsDataTableItem):
    def __init__(self):
        super(ElevatorsInspectionItem, self).__init__()
        self.date = date.today()

    def data(self, row, column):
        if column == 8:
            return QDate(self.date).toString(Qt.DefaultLocaleShortDate)
        return super(ElevatorsInspectionItem, self).data(row, column)

    def createEditor(self, parent, option, index, delegate):
        if index.column() == 8:
            editor = QDateEdit(parent)
            editor.setCalendarPopup(True)
            return editor
        return super(ElevatorsInspectionItem, self).createEditor(parent, option, index, delegate)

    def setEditorData(self, editor, index, delegate):
        if index.column() == 8:
            editor.setDate(self.date)
            return
        super(ElevatorsInspectionItem, self).setEditorData(editor, index, delegate)

    def setModelData(self, editor, model, index, delegate):
        if index.column() == 8:
            self.date = editor.date().toPyDate()
        super(ElevatorsInspectionItem, self).setModelData(editor, model, index, delegate)


class ElevatorsInspectionModel(BaseElevatorsDataTableModel):
    item_class = ElevatorsInspectionItem

    def columnCount(self, parent=None, *args, **kwargs):
        return 9

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal and column == 8:
            return 'Дата ввода в эксплуатацию'
        return super(ElevatorsInspectionModel, self).headerData(column, orientation, role)


class ElevatorsPeriodicInspectionModel(ElevatorsInspectionModel):
    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal and column == 8:
            return 'Дата проведения последнего технического освидетельствования'
        return super(ElevatorsInspectionModel, self).headerData(column, orientation, role)


class ElevatorsPartialInspectionItem(ElevatorsInspectionItem):
    def __init__(self):
        super(ElevatorsPartialInspectionItem, self).__init__()
        self.replacements = ''

    def data(self, row, column):
        if column == 9:
            return self.replacements
        return super(ElevatorsPartialInspectionItem, self).data(row, column)

    # def createEditor(self, parent, option, index):
    #     if index.column() == 8:
    #         editor = QDateEdit(parent)
    #         editor.setCalendarPopup(True)
    #         return editor
    #     return super(ElevatorsPartialInspectionItem, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index, delegate):
        if index.column() == 9:
            editor.setText(self.replacements)
            return
        super(ElevatorsPartialInspectionItem, self).setEditorData(editor, index, delegate)

    def setModelData(self, editor, model, index, delegate):
        if index.column() == 9:
            self.replacements = editor.text()
        super(ElevatorsPartialInspectionItem, self).setModelData(editor, model, index, delegate)


class ElevatorsPartialInspectionModel(ElevatorsPeriodicInspectionModel):
    item_class = ElevatorsPartialInspectionItem

    def columnCount(self, parent=None, *args, **kwargs):
        return 10

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal and column == 9:
            return 'Перечень замененных узлов, механизмов, устройств безопасности'
        return super(ElevatorsPeriodicInspectionModel, self).headerData(column, orientation, role)


class ElevatorsDocsItem(BaseElevatorsDataTableItem):
    def __init__(self):
        super(ElevatorsDocsItem, self).__init__()
        self.deadline = ''

    def data(self, row, column):
        if column == 8:
            return self.deadline
        return super(ElevatorsDocsItem, self).data(row, column)


class ElevatorsDocsModel(BaseElevatorsDataTableModel):
    item_class = ElevatorsDocsItem

    def columnCount(self, parent=None, *args, **kwargs):
        return 9

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal and column == 8:
            return 'Срок проведения проверки'
        return super(ElevatorsDocsModel, self).headerData(column, orientation, role)


class PlatformsDocsItem:
    def __init__(self, index=0):
        self.index = index
        self.address = Address()
        self.number = ''
        self.deadline = ''

    def data(self, column):
        if column == 0:
            return str(self.index)
        elif column == 1:
            return str(self.address)
        elif column == 2:
            return self.number
        elif column == 3:
            return self.deadline

    def createEditor(self, parent, option, index):
        column = index.column()
        editor = None
        if column != 1:
            editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        column = index.column()
        if column == 2:
            editor.setText(self.number)
        elif column == 3:
            editor.setText(self.deadline)

    def setModelData(self, editor, model, index):
        column = index.column()

        if column == 2:
            self.number = editor.text()
        elif column == 3:
            self.deadline = editor.text()


class PlatformsDocsModel(BaseElevatorsDataTableModel):
    item_class = PlatformsDocsItem

    def columnCount(self, parent=None, *args, **kwargs):
        return 4

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                '№ п/п',
                'Адрес',
                '№ проекта',
                'Срок проведения экспертизы'
            ][column]
        return None


class MetalInspectModel(BaseElevatorsDataTableModel):
    item_class = BaseElevatorsDataTableItem

    def columnCount(self, parent=None, *args, **kwargs):
        return 2

    def headerData(self, column, orientation, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                '№ п/п',
                'Адрес'
            ][column]
        return None


APPLICATION_TYPES = OrderedDict([
    ('inspect', {
        'title': 'Заявка на обследование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': ElevatorsInspectionModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('periodic_inspect', {
        'title': 'Заявка на периодическое техническое освидетельствование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': ElevatorsPeriodicInspectionModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('full_inspect', {
        'title': 'Заявка на полное техническое освидетельствование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': BaseElevatorsDataTableModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('partial_inspect', {
        'title': 'Заявка на частичное техническое освидетельствование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': ElevatorsPartialInspectionModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('docs_elevator', {
        'title': 'Заявка на проектную документацию (ПД) лифтов',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': ElevatorsDocsModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('docs_platform', {
        'title': 'Заявка на проектную документацию (ПД) платформ и эскалаторы',
        'table_title': 'Адресный список и технические характеристики',
        'model': PlatformsDocsModel,
        'delegate': BaseElevatorsDataTableDelegate,
    }),
    ('metal_inspect', {
        'title': 'Заявка на обследование металлоконструкций',
        'table_title': 'Адресный список',
        'model': MetalInspectModel,
        'delegate': BaseElevatorsDataTableDelegate,
    })
])
