from PyQt5.QtWidgets import QMainWindow, QWidget

from ui.shared.main_window import Ui_MainWindow
from views.applications_tab import ApplicationsTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.applicationsTab = ApplicationsTab(self)
        self.ui.tabWidget.addTab(self.applicationsTab, 'Заявки')

        # dummy
        self.ui.tabWidget.addTab(QWidget(self), 'Договоры')
        self.ui.tabWidget.addTab(QWidget(self), 'Приказы')
        self.ui.tabWidget.setTabEnabled(2, False)
