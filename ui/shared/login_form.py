# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(377, 274)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtUsername = QtWidgets.QLineEdit(LoginForm)
        self.edtUsername.setObjectName("edtUsername")
        self.verticalLayout.addWidget(self.edtUsername)
        self.label_2 = QtWidgets.QLabel(LoginForm)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.edtPassword = QtWidgets.QLineEdit(LoginForm)
        self.edtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPassword.setObjectName("edtPassword")
        self.verticalLayout.addWidget(self.edtPassword)
        self.label_3 = QtWidgets.QLabel(LoginForm)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.edtServerAddress = QtWidgets.QLineEdit(LoginForm)
        self.edtServerAddress.setObjectName("edtServerAddress")
        self.verticalLayout.addWidget(self.edtServerAddress)
        self.lblStatus = QtWidgets.QLabel(LoginForm)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout.addWidget(self.lblStatus)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalWidget = QtWidgets.QWidget(LoginForm)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAutonomyMode = QtWidgets.QPushButton(self.horizontalWidget)
        self.btnAutonomyMode.setObjectName("btnAutonomyMode")
        self.horizontalLayout.addWidget(self.btnAutonomyMode)
        self.btnLogin = QtWidgets.QPushButton(self.horizontalWidget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Вход"))
        self.label.setText(_translate("LoginForm", "Имя пользователя"))
        self.label_2.setText(_translate("LoginForm", "Пароль"))
        self.label_3.setText(_translate("LoginForm", "Адрес сервера"))
        self.edtServerAddress.setText(_translate("LoginForm", "127.0.0.1:8000"))
        self.btnAutonomyMode.setText(_translate("LoginForm", "Автономный режим"))
        self.btnLogin.setText(_translate("LoginForm", "Войти"))

