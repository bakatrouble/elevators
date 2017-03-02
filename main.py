import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

import utils
from shared.main_window import MainWindow

if __name__ == '__main__':
    # setting exception hook for pycharm
    sys.excepthook = utils.excepthook

    app = QApplication(sys.argv)
    QLocale().setDefault(QLocale(QLocale.Russian, QLocale.RussianFederation))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
