#!/usr/bin/env python3
import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication

import utils
from models.application import ApplicationModel
from models.application_type import ApplicationTypeModel
from models.client import ClientModel
from models.contract import ContractModel
from views.main_window import MainWindow


def loadModels():
    ApplicationTypeModel.loadData()
    ClientModel.loadData()
    ApplicationModel.loadData()
    ContractModel.loadData()

if __name__ == '__main__':
    # setting exception hook for pycharm
    sys.excepthook = utils.excepthook

    app = QApplication(sys.argv)
    loadModels()
    QLocale().setDefault(QLocale(QLocale.Russian, QLocale.RussianFederation))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
