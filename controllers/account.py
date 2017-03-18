from models.account import AccountModel


class AccountController:
    model = AccountModel()

    # @classmethod
    # def choose(cls, parent=None):
    #     from views.application_wizard import ApplicationWizard
    #     dlg = ApplicationWizard(parent)
    #     result = dlg.exec()
    #     item = dlg.getResult()
    #     return result, item

    @classmethod
    def create(cls, application, parent=None):
        from views.account_form import AccountForm
        dlg = AccountForm(parent)
        dlg.setApplication(application)
        result = dlg.exec()
        if result == AccountForm.Accepted:
            account = dlg.getAccount()
            while not cls.model.saveItem(account):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            application.account = account
            return True
        return False

    @classmethod
    def edit(cls, account, parent=None):
        from views.account_form import AccountForm
        dlg = AccountForm(parent)
        dlg.setAccount(account)
        result = dlg.exec()
        if result == AccountForm.Accepted:
            account = dlg.getAccount()
            while not cls.model.saveItem(account):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            return True
        return False
