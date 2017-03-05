# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomerDialog(object):
    def setupUi(self, CustomerDialog):
        CustomerDialog.setObjectName("CustomerDialog")
        CustomerDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(CustomerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(CustomerDialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAdd = QtWidgets.QPushButton(CustomerDialog)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.pushButton_3 = QtWidgets.QPushButton(CustomerDialog)
        icon = QtGui.QIcon.fromTheme("document-edit")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CustomerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CustomerDialog)
        self.buttonBox.accepted.connect(CustomerDialog.accept)
        self.buttonBox.rejected.connect(CustomerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CustomerDialog)

    def retranslateUi(self, CustomerDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomerDialog.setWindowTitle(_translate("CustomerDialog", "Выбор заказчика"))
        self.btnAdd.setText(_translate("CustomerDialog", "Добавить"))
        self.pushButton_3.setText(_translate("CustomerDialog", "Изменить"))

