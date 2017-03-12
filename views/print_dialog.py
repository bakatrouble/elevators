from PyQt5.QtWidgets import QDialog
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

from ui.shared.print_dialog import Ui_PrintDialog


class PrintDialog(QDialog):
    def __init__(self, parent=None):
        super(PrintDialog, self).__init__(parent)
        self.ui = Ui_PrintDialog()
        self.ui.setupUi(self)

        self.setupUi()
        self.setupSignals()

        self._html = ''

    def setupUi(self):
        pass

    def setupSignals(self):
        self.ui.btnPrint.clicked.connect(self.doPrint)

    def showDialog(self, html):
        print(html)
        self._html = html
        self.ui.textBrowser.setHtml(html)
        self.exec()

    def doPrint(self):
        printer = QPrinter()
        dlg = QPrintDialog(printer, self)
        dlg.setWindowTitle('Печать документа')
        if dlg.exec() == QPrintDialog.Accepted:
            self.ui.textBrowser.print(printer)
            self.close()
