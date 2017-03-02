from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWizard

from shared.customer_dialog import CustomerDialog
from ui.applications.application_wizard import Ui_ApplicationWizard
from .models import APPLICATION_TYPES


class ApplicationWizard(QWizard):
    def __init__(self, parent=None):
        super(ApplicationWizard, self).__init__(parent)
        self.ui = Ui_ApplicationWizard()
        self.ui.setupUi(self)

        self.setupSignals()
        self.setupUi()
        self.fillApplicationTypes()

    def setupSignals(self):
        self.currentIdChanged.connect(self.pageChanged)
        self.ui.btnSelectCustomer.clicked.connect(self.selectCustomer)

    def setupUi(self):
        self.ui.tblElevatorsData.horizontalHeader().setVisible(True)

    def pageChanged(self, pageId):
        if pageId == 1:
            applicationType = APPLICATION_TYPES[self.ui.cmbApplicationType.currentData(Qt.UserRole)]
            self.ui.lblTableTitle.setText(applicationType['table_title'])
            self.ui.tblElevatorsData.setModel(applicationType['model'](self))

    def selectCustomer(self):
        dlg = CustomerDialog(self)
        if dlg.exec() == CustomerDialog.Accepted:
            pass

    def fillApplicationTypes(self):
        for code, info in APPLICATION_TYPES.items():
            self.ui.cmbApplicationType.addItem(info['title'], code)
