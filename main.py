#!/usr/bin/env python3
import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication

from utils import excepthook, Options, die
from views.main_window import MainWindow
from views.login_form import LoginForm
import resources

if __name__ == '__main__':
    # setting exception hook for pycharm
    sys.excepthook = excepthook

    app = QApplication(sys.argv)
    QLocale().setDefault(QLocale(QLocale.Russian, QLocale.RussianFederation))
    qt_translator = QTranslator()
    qt_translator.load(':/qtbase_ru.qm')
    app.installTranslator(qt_translator)

    login_form = LoginForm()
    if login_form.exec() != LoginForm.Accepted:
        die()

    window = MainWindow()
    window.show()
    app.exec()

    Options.dump()
    die()
