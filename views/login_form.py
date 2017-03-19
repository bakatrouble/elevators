import sys

from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
import requests
import requests.exceptions

from ui.shared.login_form import Ui_LoginForm
from utils import Options
from models import Models


class Worker(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(bool)
    progress = pyqtSignal(str)

    def __init__(self, username, password):
        super(Worker, self).__init__()
        self.username = username
        self.password = password

    def checkAuth(self):
        data = requests.post('http://' + Options.get().server_url + '/api/auth/', json={
            'username': self.username, 'password': self.password
        }).json()
        if data['status'] != 'success':
            return False
        Options.get().token = data['token']
        Options.get().group = data['user']['group']
        return True

    def process(self):
        try:
            self.progress.emit('Проверка имени пользователя и пароля')
            if not self.checkAuth():
                self.progress.emit('<font color=red>Неверное имя пользователя и/или пароль</font>')
                self.finished.emit()
                return

            self.progress.emit('Синхронизация локального хранилища с сервером...')
            for client in Options.get().local_clients:
                Models.get().clients.saveItem(client)
            for application in Options.get().local_applications:
                Models.get().applications.saveItem(application)
            Options.get().local_clients = []
            Options.get().local_applications = []

            self.progress.emit('Загрузка типов заявок')
            Models.get().application_types.loadData()
            self.progress.emit('Загрузка заказчиков')
            Models.get().clients.loadData()
            self.progress.emit('Загрузка специалистов')
            Models.get().specialists.loadData()
            self.progress.emit('')
            self.result.emit(True)
        except requests.exceptions.ConnectionError:
            self.result.emit(False)
        self.finished.emit()


class LoginForm(QDialog):
    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

        self.thread = None
        self.worker = None

    def setupUi(self):
        self.ui.edtServerAddress.setText(Options.get().server_url)
        self.ui.edtUsername.setText(Options.get().username)
        if not Options.get().autonomy_available:
            self.ui.btnAutonomyMode.setEnabled(False)

    def setupSignals(self):
        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnAutonomyMode.clicked.connect(self.autonomy_mode)

    def login(self):
        Options.get().username = self.ui.edtUsername.text()
        Options.get().server_url = self.ui.edtServerAddress.text()

        self.ui.btnAutonomyMode.setEnabled(False)
        self.ui.btnLogin.setEnabled(False)

        self.loadModels()

    def loadModels(self):
        self.thread = QThread()
        self.worker = Worker(self.ui.edtUsername.text(), self.ui.edtPassword.text())
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.process)
        self.worker.result.connect(self.loadModelsFinished)
        self.worker.progress.connect(self.loadModelsProgress)
        self.worker.finished.connect(self.reset)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def loadModelsProgress(self, message):
        self.ui.lblStatus.setText(message)

    def loadModelsFinished(self, success):
        if not success:
            if Options.get().autonomy_available:
                ans = QMessageBox().warning(None, 'Ошибка',
                                            'Произошла ошибка при соединении с сервером. Перейти в автономный режим?',
                                            QMessageBox.Yes | QMessageBox.No)
                if ans == QMessageBox.Yes:
                    self.autonomy_mode()
                    return
            else:
                QMessageBox().warning(None, 'Ошибка', 'Произошла ошибка при соединении с сервером.', QMessageBox.Ok)
            self.reset()
        else:
            self.accept()

    def reset(self):
        self.ui.btnAutonomyMode.setEnabled(True)
        self.ui.btnLogin.setEnabled(True)

    def autonomy_mode(self):
        Options.get().autonomy_mode = True
        Models.get().application_types.setItems(Options.get().cache_application_types)
        Models.get().clients.setItems(Options.get().cache_clients)
        Models.get().specialists.setItems(Options.get().cache_specialists)
        self.accept()
