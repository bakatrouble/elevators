# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrintDialog(object):
    def setupUi(self, PrintDialog):
        PrintDialog.setObjectName("PrintDialog")
        PrintDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PrintDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(PrintDialog)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalWidget = QtWidgets.QWidget(PrintDialog)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnPrint = QtWidgets.QPushButton(self.horizontalWidget)
        icon = QtGui.QIcon.fromTheme("document-print")
        self.btnPrint.setIcon(icon)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout.addWidget(self.btnPrint)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(PrintDialog)
        QtCore.QMetaObject.connectSlotsByName(PrintDialog)

    def retranslateUi(self, PrintDialog):
        _translate = QtCore.QCoreApplication.translate
        PrintDialog.setWindowTitle(_translate("PrintDialog", "Dialog"))
        self.btnPrint.setText(_translate("PrintDialog", "Печать"))

