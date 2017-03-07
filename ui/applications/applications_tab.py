# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applications_tab.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplicationsTab(object):
    def setupUi(self, ApplicationsTab):
        ApplicationsTab.setObjectName("ApplicationsTab")
        ApplicationsTab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ApplicationsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(ApplicationsTab)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonPrint = QtWidgets.QPushButton(ApplicationsTab)
        self.buttonPrint.setEnabled(False)
        self.buttonPrint.setObjectName("buttonPrint")
        self.horizontalLayout.addWidget(self.buttonPrint)
        self.buttonContract = QtWidgets.QPushButton(ApplicationsTab)
        self.buttonContract.setEnabled(False)
        self.buttonContract.setObjectName("buttonContract")
        self.horizontalLayout.addWidget(self.buttonContract)
        self.buttonWizard = QtWidgets.QPushButton(ApplicationsTab)
        self.buttonWizard.setObjectName("buttonWizard")
        self.horizontalLayout.addWidget(self.buttonWizard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ApplicationsTab)
        QtCore.QMetaObject.connectSlotsByName(ApplicationsTab)

    def retranslateUi(self, ApplicationsTab):
        _translate = QtCore.QCoreApplication.translate
        ApplicationsTab.setWindowTitle(_translate("ApplicationsTab", "Form"))
        self.buttonPrint.setText(_translate("ApplicationsTab", "Печать"))
        self.buttonContract.setText(_translate("ApplicationsTab", "Создать договор"))
        self.buttonWizard.setText(_translate("ApplicationsTab", "Добавить"))

