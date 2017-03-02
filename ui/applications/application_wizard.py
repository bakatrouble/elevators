# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplicationWizard(object):
    def setupUi(self, ApplicationWizard):
        ApplicationWizard.setObjectName("ApplicationWizard")
        ApplicationWizard.resize(400, 300)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cmbApplicationType = QtWidgets.QComboBox(self.wizardPage1)
        self.cmbApplicationType.setObjectName("cmbApplicationType")
        self.verticalLayout.addWidget(self.cmbApplicationType)
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblCustomer = QtWidgets.QLabel(self.wizardPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCustomer.sizePolicy().hasHeightForWidth())
        self.lblCustomer.setSizePolicy(sizePolicy)
        self.lblCustomer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lblCustomer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblCustomer.setObjectName("lblCustomer")
        self.horizontalLayout_2.addWidget(self.lblCustomer)
        self.btnSelectCustomer = QtWidgets.QToolButton(self.wizardPage1)
        self.btnSelectCustomer.setObjectName("btnSelectCustomer")
        self.horizontalLayout_2.addWidget(self.btnSelectCustomer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        ApplicationWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTableTitle = QtWidgets.QLabel(self.wizardPage2)
        self.lblTableTitle.setObjectName("lblTableTitle")
        self.verticalLayout_2.addWidget(self.lblTableTitle)
        self.tblElevatorsData = QtWidgets.QTableView(self.wizardPage2)
        self.tblElevatorsData.setObjectName("tblElevatorsData")
        self.verticalLayout_2.addWidget(self.tblElevatorsData)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.wizardPage2)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.wizardPage2)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        ApplicationWizard.addPage(self.wizardPage2)

        self.retranslateUi(ApplicationWizard)
        QtCore.QMetaObject.connectSlotsByName(ApplicationWizard)

    def retranslateUi(self, ApplicationWizard):
        _translate = QtCore.QCoreApplication.translate
        ApplicationWizard.setWindowTitle(_translate("ApplicationWizard", "Wizard"))
        self.label.setText(_translate("ApplicationWizard", "Тип заявки"))
        self.label_2.setText(_translate("ApplicationWizard", "Заказчик"))
        self.lblCustomer.setText(_translate("ApplicationWizard", "<не выбрано>"))
        self.btnSelectCustomer.setText(_translate("ApplicationWizard", "..."))
        self.lblTableTitle.setText(_translate("ApplicationWizard", "Адресный список и технические характеристики лифтов"))
        self.pushButton.setText(_translate("ApplicationWizard", "Добавить"))
        self.pushButton_2.setText(_translate("ApplicationWizard", "Удалить"))

