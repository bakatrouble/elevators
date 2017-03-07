from models.client import ClientModel


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
            cls.model.addItem(dlg.getClient())
            return True
        return False

    @staticmethod
    def edit(client, parent=None):
        from views.client_form import ClientForm
        dlg = ClientForm(parent)
        dlg.setClient(client)
        result = dlg.exec()
        if result == ClientForm.Accepted:
            dlg.getClient()
            return True
        return False
