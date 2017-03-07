# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientDialog(object):
    def setupUi(self, ClientDialog):
        ClientDialog.setObjectName("ClientDialog")
        ClientDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ClientDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstClients = QtWidgets.QListView(ClientDialog)
        self.lstClients.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstClients.setObjectName("lstClients")
        self.verticalLayout.addWidget(self.lstClients)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAdd = QtWidgets.QPushButton(ClientDialog)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(ClientDialog)
        icon = QtGui.QIcon.fromTheme("document-edit")
        self.btnEdit.setIcon(icon)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout.addWidget(self.btnEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClientDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ClientDialog)
        self.buttonBox.accepted.connect(ClientDialog.accept)
        self.buttonBox.rejected.connect(ClientDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClientDialog)

    def retranslateUi(self, ClientDialog):
        _translate = QtCore.QCoreApplication.translate
        ClientDialog.setWindowTitle(_translate("ClientDialog", "Выбор заказчика"))
        self.btnAdd.setText(_translate("ClientDialog", "Добавить"))
        self.btnEdit.setText(_translate("ClientDialog", "Изменить"))

