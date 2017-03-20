from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from models.items.order import Order
from models.items.application import Application
from models.specialist import SpecialistListModel, SpecialistItemDelegate, SpecialistModel

from ui.orders.order_form import Ui_OrderForm


class OrderForm(QDialog):
    def __init__(self, parent=None):
        super(OrderForm, self).__init__(parent)
        self.ui = Ui_OrderForm()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

        self._order = Order()

    def setupSignals(self):
        self.ui.btnAddSpecialist.clicked.connect(self.addSpecialist)
        self.ui.btnDeleteSpecialist.clicked.connect(self.deleteSpecialist)
        self.ui.lstSpecialists.selectionModel().selectionChanged.connect(self.specialistSelectionChanged)

    def setupUi(self):
        self.ui.edtDate.setDate(QDate().currentDate())
        self.ui.edtTODate.setDate(QDate().currentDate())
        self.ui.edtActDate.setDate(QDate().currentDate())

        self.ui.lstSpecialists.setModel(SpecialistListModel())
        self.ui.lstSpecialists.setItemDelegate(SpecialistItemDelegate())

    def specialistSelectionChanged(self):
        if len(self.ui.lstSpecialists.selectedIndexes()):
            self.ui.btnDeleteSpecialist.setEnabled(True)
        else:
            self.ui.btnDeleteSpecialist.setEnabled(False)

    def addSpecialist(self):
        self.ui.lstSpecialists.model().addItem()

    def deleteSpecialist(self):
        self.ui.lstSpecialists.model().removeItem(self.ui.lstSpecialists.currentIndex().row())

    def setApplication(self, application: Application):
        self._order.application_id = application.id

    def getOrder(self):
        self._order.number = self.ui.edtNumber.text()
        self._order.date = self.ui.edtDate.date()
        self._order.to_date = self.ui.edtTODate.date()
        self._order.act_date = self.ui.edtActDate.date()
        self._order.controller = self.ui.edtController.text()
        self._order.expert = self.ui.edtExpert.text()
        self._order.manager = self.ui.edtManager.text()
        self._order.head_specialist = self.ui.cmbHeadSpecialist.currentData(Qt.UserRole)
        self._order.specialists = self.ui.lstSpecialists.model().getSpecialists()
        return self._order

    def setOrder(self, order: Order):
        self._order = order
        self.ui.edtNumber.setText(order.number)
        self.ui.edtDate.setDate(order.date)
        self.ui.edtTODate.setDate(order.to_date)
        self.ui.edtActDate.setDate(order.act_date)
        self.ui.edtController.setText(order.controller)
        self.ui.edtManager.setText(order.manager)
        self.ui.edtExpert.setText(order.expert)
        if order.head_specialist is not None:
            self.ui.cmbHeadSpecialist.setCurrentIndex(SpecialistModel.getIndexById(order.head_specialist.id))
        self.ui.lstSpecialists.model().setSpecialists(order.specialists)
