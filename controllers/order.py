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
            cls.model.saveItem(order)
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
            cls.model.saveItem(order)
            return True
        return False
