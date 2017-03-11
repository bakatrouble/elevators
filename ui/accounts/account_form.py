# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_form.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountForm(object):
    def setupUi(self, AccountForm):
        AccountForm.setObjectName("AccountForm")
        AccountForm.resize(400, 170)
        self.verticalLayout = QtWidgets.QVBoxLayout(AccountForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AccountForm)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtNumber = QtWidgets.QLineEdit(AccountForm)
        self.edtNumber.setObjectName("edtNumber")
        self.verticalLayout.addWidget(self.edtNumber)
        self.label_2 = QtWidgets.QLabel(AccountForm)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.edtDate = QtWidgets.QDateEdit(AccountForm)
        self.edtDate.setCalendarPopup(True)
        self.edtDate.setObjectName("edtDate")
        self.verticalLayout.addWidget(self.edtDate)
        self.buttonBox = QtWidgets.QDialogButtonBox(AccountForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AccountForm)
        self.buttonBox.accepted.connect(AccountForm.accept)
        self.buttonBox.rejected.connect(AccountForm.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountForm)

    def retranslateUi(self, AccountForm):
        _translate = QtCore.QCoreApplication.translate
        AccountForm.setWindowTitle(_translate("AccountForm", "Dialog"))
        self.label.setText(_translate("AccountForm", "Номер счета"))
        self.label_2.setText(_translate("AccountForm", "Дата счета"))

