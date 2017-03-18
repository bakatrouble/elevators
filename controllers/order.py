from models.order import OrderModel


class OrderController:
    model = OrderModel()

    @classmethod
    def create(cls, application, parent=None):
        from views.order_form import OrderForm
        dlg = OrderForm(parent)
        dlg.setApplication(application)
        result = dlg.exec()
        if result == OrderForm.Accepted:
            order = dlg.getOrder()
            while not cls.model.saveItem(order):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            application.contract = order
            return True
        return False

    @classmethod
    def edit(cls, order, parent=None):
        from views.order_form import OrderForm
        dlg = OrderForm(parent)
        dlg.setOrder(order)
        result = dlg.exec()
        if result == OrderForm.Accepted:
            order = dlg.getOrder()
            while not cls.model.saveItem(order):
                p = QMessageBox().warning(parent, 'Ошибка',
                                          'Потеряно соединение с сервером. Повторить?\nПри отмене программа будет '
                                          'закрыта, а несохраненные изменения потеряны.',
                                          QMessageBox.Retry | QMessageBox.Cancel)
                if p != QMessageBox.Retry:
                    die()
            return True
        return False
