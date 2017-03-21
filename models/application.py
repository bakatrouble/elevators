import requests
import requests.exceptions
import sys
from PyQt5.QtCore import QModelIndex, Qt, QStringListModel
from PyQt5.QtWidgets import QMessageBox

from models.items.application import Application
from utils import Options, die
from views.application_wizard import ApplicationWizard


class ApplicationModel(QStringListModel):
    def __init__(self):
        super(ApplicationModel, self).__init__()
        self._items = Options.get().local_applications.copy()
        self._next = None
        self._has_next_page = True

    def resetInternalData(self):
        self._items = Options.get().local_applications.copy()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._items)

    def canFetchMore(self, index):
        return self._has_next_page and not Options.get().autonomy_mode

    def index(self, row, column=0, parent=None, *args, **kwargs):
        if 0 <= row < len(self._items):
            return self.createIndex(row, column, self._items[row])
        return QModelIndex()

    def fetchMore(self, index):
        headers = {'Authorization': 'Token ' + Options.get().token}
        try:
            if not self._next:
                data = requests.get('http://' + Options.get().server_url + '/api/applications/',
                                    headers=headers).json()
            else:
                data = requests.get(self._next).json()
        except requests.exceptions.ConnectionError:
            QMessageBox().warning(None, 'Ошибка', 'Соединение с сервером потеряно. Программа будет закрыта.')
            die()
            return
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items) + len(data['results']))
        for item in data['results']:
            self._items.append(Application.fromDict(item))
        self.endInsertRows()
        self._next = data['next']
        self._has_next_page = bool(data['next'])

    def data(self, index, role=None):
        row = index.row()
        item = self._items[row]
        if role == Qt.DisplayRole:
            if item.id:
                return '№%s от %s, %s, %s' % (item.id, item.date.toString(Qt.DefaultLocaleShortDate),
                                              item.client.short_name, item.type.name)
            else:
                return '[Локальная] %s, %s, %s' % (item.date.toString(Qt.DefaultLocaleShortDate),
                                                   item.client.short_name, item.type.name)
        return None

    def columnCount(self, *args, **kwargs):
        return 1

    def saveItem(self, item):
        headers = {'Authorization': 'Token ' + Options.get().token}
        try:
            if item.id is None:
                data = requests.post('http://' + Options.get().server_url + '/api/applications/',
                                     json=item.toDict(),
                                     headers=headers).json()
                item.id = data['id']
            else:
                requests.put('http://' + Options.get().server_url + '/api/applications/' + str(item.id) + '/',
                             json=item.toDict(),
                             headers=headers)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def addItem(self, item):
        local = len(Options.get().local_applications)
        self.beginInsertRows(QModelIndex(), local, local + 1)
        self._items.insert(local, item)
        self.endInsertRows()

    def createApplication(self, parent=None):
        dlg = ApplicationWizard(parent)
        result = dlg.exec()
        if result == ApplicationWizard.Accepted:
            application = dlg.getApplication()
            if not Options.get().autonomy_mode:
                while not self.saveItem(application):
                    p = QMessageBox().warning(None, 'Ошибка',
                                              'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                              'закрыта, а несохраненные изменения потеряны.',
                                              QMessageBox.Retry | QMessageBox.Cancel)
                    if p != QMessageBox.Retry:
                        self.addItem(application)
                        die()
            self.addItem(application)
            return True
        return False

    def editApplication(self, index, parent=None):
        dlg = ApplicationWizard(parent)
        dlg.setApplication(index.internalPointer())
        result = dlg.exec()
        if result == ApplicationWizard.Accepted:
            application = dlg.getApplication()
            while not self.saveItem(application):
                p = QMessageBox().warning(None, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            self.dataChanged.emit(index, index)
            return True
        return False

    def items(self):
        return self._items

    def flags(self, index):
        return super(ApplicationModel, self).flags(index) & ~Qt.ItemIsEditable
