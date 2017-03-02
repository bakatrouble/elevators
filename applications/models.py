from collections import OrderedDict

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import Qt


class BaseElevatorsDataTableModel(QAbstractTableModel):
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

APPLICATION_TYPES = OrderedDict([
    ('inspect', {
        'title': 'Заявка на обследование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': BaseElevatorsDataTableModel,
    }),
    ('periodic_inspect', {
        'title': 'Заявка на периодическое техническое освидетельствование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': BaseElevatorsDataTableModel,
    }),
    ('full_inspect', {
        'title': 'Заявка на полное техническое освидетельствование',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': BaseElevatorsDataTableModel,
    }),
    ('docs_elevator', {
        'title': 'Заявка на проектную документацию (ПД) лифтов',
        'table_title': 'Адресный список и технические характеристики лифтов',
        'model': BaseElevatorsDataTableModel,
    }),
    ('docs_platform', {
        'title': 'Заявка на проектную документацию (ПД) платформ и эскалаторы',
        'table_title': 'Адресный список и технические характеристики',
        'model': BaseElevatorsDataTableModel,
    })
])
