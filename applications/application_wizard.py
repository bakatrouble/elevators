from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWizard

from shared.customer_dialog import CustomerDialog
from ui.applications.application_wizard import Ui_ApplicationWizard
from .models import APPLICATION_TYPES


class ApplicationWizard(QWizard):
    def __init__(self, parent=None):
        super(ApplicationWizard, self).__init__(parent)
        self.ui = Ui_ApplicationWizard()
        self.ui.setupUi(self)

        self._currentApplicationTypeIndex = -1

        self.setupSignals()
        self.setupUi()
        self.fillApplicationTypes()

    def setupSignals(self):
        self.ui.cmbApplicationType.currentIndexChanged[int].connect(self.applicationTypeChanged)
        self.ui.btnSelectCustomer.clicked.connect(self.selectCustomer)
        self.ui.btnTableAdd.clicked.connect(self.addTableItem)
        self.ui.btnTableRemove.clicked.connect(self.removeTableItem)

    def setupUi(self):
        self.ui.tblElevatorsData.horizontalHeader().setVisible(True)

    def applicationTypeChanged(self, index):
        if index == self._currentApplicationTypeIndex:
            return
        if self.ui.tblElevatorsData.model() and self.ui.tblElevatorsData.model().rowCount():
            prompt = QMessageBox().question(self, 'Сменить тип?', 'В таблице есть заполненные данные. При смене типа заявки они будут сброшены. Вы уверены?')
            if prompt == QMessageBox.No:
                self.ui.cmbApplicationType.setCurrentIndex(self._currentApplicationTypeIndex)
                return
        self._currentApplicationTypeIndex = index
        applicationType = APPLICATION_TYPES[self.ui.cmbApplicationType.currentData(Qt.UserRole)]
        self.ui.lblTableTitle.setText(applicationType['table_title'])
        self.ui.tblElevatorsData.setModel(applicationType['model'](self))
        self.ui.tblElevatorsData.setItemDelegate(applicationType['delegate']())

    def addTableItem(self):
        self.ui.tblElevatorsData.model().addItem()

    def removeTableItem(self):
        rows = {index.row() for index in self.ui.tblElevatorsData.selectedIndexes()}
        self.ui.tblElevatorsData.model().removeItems(rows)

    def selectCustomer(self):
        dlg = CustomerDialog(self)
        if dlg.exec() == CustomerDialog.Accepted:
            pass

    def fillApplicationTypes(self):
        for code, info in APPLICATION_TYPES.items():
            self.ui.cmbApplicationType.addItem(info['title'], code)
