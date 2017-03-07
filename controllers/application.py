from models.application import ApplicationModel


class ApplicationController:
    model = ApplicationModel()

    # @classmethod
    # def choose(cls, parent=None):
    #     from views.application_wizard import ApplicationWizard
    #     dlg = ApplicationWizard(parent)
    #     result = dlg.exec()
    #     item = dlg.getResult()
    #     return result, item

    @classmethod
    def create(cls, parent=None):
        from views.application_wizard import ApplicationWizard
        dlg = ApplicationWizard(parent)
        result = dlg.exec()
        if result == ApplicationWizard.Accepted:
            cls.model.addItem(dlg.getApplication())
            return True
        return False

    @staticmethod
    def edit(application, parent=None):
        from views.application_wizard import ApplicationWizard
        dlg = ApplicationWizard(parent)
        dlg.setApplication(application)
        result = dlg.exec()
        if result == ApplicationWizard.Accepted:
            dlg.getApplication()
            return True
        return False
