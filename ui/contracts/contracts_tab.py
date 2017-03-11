# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contracts_tab.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContractsTab(object):
    def setupUi(self, ContractsTab):
        ContractsTab.setObjectName("ContractsTab")
        ContractsTab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ContractsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(ContractsTab)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrint = QtWidgets.QPushButton(ContractsTab)
        self.btnPrint.setEnabled(False)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout.addWidget(self.btnPrint)
        self.btnAccount = QtWidgets.QPushButton(ContractsTab)
        self.btnAccount.setEnabled(False)
        self.btnAccount.setObjectName("btnAccount")
        self.horizontalLayout.addWidget(self.btnAccount)
        self.btnCreateForm = QtWidgets.QPushButton(ContractsTab)
        self.btnCreateForm.setObjectName("btnCreateForm")
        self.horizontalLayout.addWidget(self.btnCreateForm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ContractsTab)
        QtCore.QMetaObject.connectSlotsByName(ContractsTab)

    def retranslateUi(self, ContractsTab):
        _translate = QtCore.QCoreApplication.translate
        ContractsTab.setWindowTitle(_translate("ContractsTab", "Form"))
        self.btnPrint.setText(_translate("ContractsTab", "Печать"))
        self.btnAccount.setText(_translate("ContractsTab", "Создать счет"))
        self.btnCreateForm.setText(_translate("ContractsTab", "Добавить"))

