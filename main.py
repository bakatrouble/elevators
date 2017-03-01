import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

import utils

if __name__ == '__main__':
    # setting exception hook for pycharm
    sys.excepthook = utils.excepthook

    app = QApplication(sys.argv)
    window = QMainWindow()
    button = QPushButton("Hello, PyQt!")
    window.setCentralWidget(button)
    window.show()
    sys.exit(app.exec())
