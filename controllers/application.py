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
            application = dlg.getApplication()
            cls.model.saveItem(application)
            cls.model.addItem(application)
            return True
        return False

    @classmethod
    def edit(cls, application, parent=None):
        from views.application_wizard import ApplicationWizard
        dlg = ApplicationWizard(parent)
        dlg.setApplication(application)
        result = dlg.exec()
        if result == ApplicationWizard.Accepted:
            application = dlg.getApplication()
            cls.model.saveItem(application)
            return True
        return False
