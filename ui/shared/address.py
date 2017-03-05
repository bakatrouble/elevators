# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'address.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddressDialog(object):
    def setupUi(self, AddressDialog):
        AddressDialog.setObjectName("AddressDialog")
        AddressDialog.resize(400, 302)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AddressDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtOblast = QtWidgets.QLineEdit(AddressDialog)
        self.edtOblast.setObjectName("edtOblast")
        self.verticalLayout.addWidget(self.edtOblast)
        self.label_2 = QtWidgets.QLabel(AddressDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.edtRaion = QtWidgets.QLineEdit(AddressDialog)
        self.edtRaion.setObjectName("edtRaion")
        self.verticalLayout.addWidget(self.edtRaion)
        self.label_3 = QtWidgets.QLabel(AddressDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.edtCity = QtWidgets.QLineEdit(AddressDialog)
        self.edtCity.setObjectName("edtCity")
        self.verticalLayout.addWidget(self.edtCity)
        self.label_7 = QtWidgets.QLabel(AddressDialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.edtStreet = QtWidgets.QLineEdit(AddressDialog)
        self.edtStreet.setObjectName("edtStreet")
        self.verticalLayout.addWidget(self.edtStreet)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(AddressDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.edtHouse = QtWidgets.QLineEdit(AddressDialog)
        self.edtHouse.setObjectName("edtHouse")
        self.horizontalLayout.addWidget(self.edtHouse)
        self.label_5 = QtWidgets.QLabel(AddressDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.edtBuilding = QtWidgets.QLineEdit(AddressDialog)
        self.edtBuilding.setObjectName("edtBuilding")
        self.horizontalLayout.addWidget(self.edtBuilding)
        self.label_6 = QtWidgets.QLabel(AddressDialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.edtLetter = QtWidgets.QLineEdit(AddressDialog)
        self.edtLetter.setObjectName("edtLetter")
        self.horizontalLayout.addWidget(self.edtLetter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddressDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddressDialog)
        self.buttonBox.accepted.connect(AddressDialog.accept)
        self.buttonBox.rejected.connect(AddressDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddressDialog)

    def retranslateUi(self, AddressDialog):
        _translate = QtCore.QCoreApplication.translate
        AddressDialog.setWindowTitle(_translate("AddressDialog", "Dialog"))
        self.label.setText(_translate("AddressDialog", "Область"))
        self.label_2.setText(_translate("AddressDialog", "Район"))
        self.label_3.setText(_translate("AddressDialog", "Населенный пункт"))
        self.label_7.setText(_translate("AddressDialog", "Улица"))
        self.label_4.setText(_translate("AddressDialog", "Дом"))
        self.label_5.setText(_translate("AddressDialog", "Корпус"))
        self.label_6.setText(_translate("AddressDialog", "Литера"))

