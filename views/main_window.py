from PyQt5.QtWidgets import QMainWindow, QWidget

from ui.shared.main_window import Ui_MainWindow
from views.applications_tab import ApplicationsTab
from views.contracts_tab import ContractsTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.applicationsTab = ApplicationsTab(self)
        self.contractsTab = ContractsTab(self)
        self.ui.tabWidget.addTab(self.applicationsTab, 'Заявки')
        self.ui.tabWidget.addTab(self.contractsTab, 'Договоры')

        # dummy
        self.ui.tabWidget.addTab(QWidget(self), 'Приказы')
        self.ui.tabWidget.setTabEnabled(2, False)
