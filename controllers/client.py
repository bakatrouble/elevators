from models.client import ClientModel
from utils import Options


class ClientController:
    model = ClientModel()

    @classmethod
    def choose(cls, parent=None):
        from views.client_dialog import ClientDialog
        dlg = ClientDialog(parent)
        result = dlg.exec()
        item_id = dlg.getResult()
        item = cls.model.getItemById(item_id)
        return result, item

    @classmethod
    def create(cls, parent=None):
        from views.client_form import ClientForm
        dlg = ClientForm(parent)
        result = dlg.exec()
        if result == ClientForm.Accepted:
            client = dlg.getClient()
            if not Options.get().autonomy_mode:
                while not cls.model.saveItem(client):
                    p = QMessageBox().warning(parent, 'Ошибка',
                                              'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                              'закрыта, а несохраненные изменения потеряны.',
                                              QMessageBox.Retry | QMessageBox.Cancel)
                    if p != QMessageBox.Retry:
                        die()
            cls.model.addItem(client)
            return True
        return False

    @classmethod
    def edit(cls, client, parent=None):
        from views.client_form import ClientForm
        dlg = ClientForm(parent)
        dlg.setClient(client)
        result = dlg.exec()
        if result == ClientForm.Accepted:
            client = dlg.getClient()
            if not Options.get().autonomy_mode:
                while not cls.model.saveItem(client):
                    p = QMessageBox().warning(parent, 'Ошибка',
                                              'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                              'закрыта, а несохраненные изменения потеряны.',
                                              QMessageBox.Retry | QMessageBox.Cancel)
                    if p != QMessageBox.Retry:
                        die()
            return True
        return False
