from models.contract import ContractModel


class ContractController:
    model = ContractModel()

    # @classmethod
    # def choose(cls, parent=None):
    #     from views.application_wizard import ApplicationWizard
    #     dlg = ApplicationWizard(parent)
    #     result = dlg.exec()
    #     item = dlg.getResult()
    #     return result, item

    @classmethod
    def create(cls, application, parent=None):
        from views.contract_form import ContractForm
        dlg = ContractForm(parent)
        dlg.setApplication(application)
        result = dlg.exec()
        if result == ContractForm.Accepted:
            contract = dlg.getContract()
            while not cls.model.saveItem(contract):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            application.contract = contract
            return True
        return False

    @classmethod
    def edit(cls, contract, parent=None):
        from views.contract_form import ContractForm
        dlg = ContractForm(parent)
        dlg.setContract(contract)
        result = dlg.exec()
        if result == ContractForm.Accepted:
            contract = dlg.getContract()
            while not cls.model.saveItem(contract):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            return True
        return False
