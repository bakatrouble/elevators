# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.verticalWidget = QtWidgets.QWidget(self.splitter)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tblApplications = QtWidgets.QListView(self.verticalWidget)
        self.tblApplications.setObjectName("tblApplications")
        self.verticalLayout_2.addWidget(self.tblApplications)
        self.widget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnPrintApplication = QtWidgets.QPushButton(self.widget_2)
        self.btnPrintApplication.setEnabled(False)
        self.btnPrintApplication.setObjectName("btnPrintApplication")
        self.horizontalLayout_5.addWidget(self.btnPrintApplication)
        self.btnCreateApplication = QtWidgets.QPushButton(self.widget_2)
        self.btnCreateApplication.setObjectName("btnCreateApplication")
        self.horizontalLayout_5.addWidget(self.btnCreateApplication)
        self.btnEditApplication = QtWidgets.QPushButton(self.widget_2)
        self.btnEditApplication.setEnabled(False)
        self.btnEditApplication.setObjectName("btnEditApplication")
        self.horizontalLayout_5.addWidget(self.btnEditApplication)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.pnlDocuments = QtWidgets.QScrollArea(self.splitter)
        self.pnlDocuments.setEnabled(False)
        self.pnlDocuments.setMinimumSize(QtCore.QSize(500, 0))
        self.pnlDocuments.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pnlDocuments.setWidgetResizable(True)
        self.pnlDocuments.setObjectName("pnlDocuments")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 500, 522))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblContractNumber = QtWidgets.QLabel(self.horizontalWidget)
        self.lblContractNumber.setObjectName("lblContractNumber")
        self.horizontalLayout.addWidget(self.lblContractNumber)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnPrintContract = QtWidgets.QPushButton(self.horizontalWidget)
        self.btnPrintContract.setEnabled(False)
        self.btnPrintContract.setObjectName("btnPrintContract")
        self.horizontalLayout.addWidget(self.btnPrintContract)
        self.btnCreateContract = QtWidgets.QPushButton(self.horizontalWidget)
        self.btnCreateContract.setObjectName("btnCreateContract")
        self.horizontalLayout.addWidget(self.btnCreateContract)
        self.btnEditContract = QtWidgets.QPushButton(self.horizontalWidget)
        self.btnEditContract.setEnabled(False)
        self.btnEditContract.setObjectName("btnEditContract")
        self.horizontalLayout.addWidget(self.btnEditContract)
        self.verticalLayout_4.addWidget(self.horizontalWidget)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblAccountNumber = QtWidgets.QLabel(self.horizontalWidget_2)
        self.lblAccountNumber.setObjectName("lblAccountNumber")
        self.horizontalLayout_2.addWidget(self.lblAccountNumber)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnPrintAccount = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btnPrintAccount.setEnabled(False)
        self.btnPrintAccount.setObjectName("btnPrintAccount")
        self.horizontalLayout_2.addWidget(self.btnPrintAccount)
        self.btnCreateAccount = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btnCreateAccount.setObjectName("btnCreateAccount")
        self.horizontalLayout_2.addWidget(self.btnCreateAccount)
        self.btnEditAccount = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btnEditAccount.setEnabled(False)
        self.btnEditAccount.setObjectName("btnEditAccount")
        self.horizontalLayout_2.addWidget(self.btnEditAccount)
        self.verticalLayout_4.addWidget(self.horizontalWidget_2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblOrderNumber = QtWidgets.QLabel(self.horizontalWidget_3)
        self.lblOrderNumber.setObjectName("lblOrderNumber")
        self.horizontalLayout_3.addWidget(self.lblOrderNumber)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnPrintOrder = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.btnPrintOrder.setEnabled(False)
        self.btnPrintOrder.setObjectName("btnPrintOrder")
        self.horizontalLayout_3.addWidget(self.btnPrintOrder)
        self.btnCreateOrder = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.btnCreateOrder.setObjectName("btnCreateOrder")
        self.horizontalLayout_3.addWidget(self.btnCreateOrder)
        self.btnEditOrder = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.btnEditOrder.setEnabled(False)
        self.btnEditOrder.setObjectName("btnEditOrder")
        self.horizontalLayout_3.addWidget(self.btnEditOrder)
        self.verticalLayout_4.addWidget(self.horizontalWidget_3)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.tblProtocols = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.tblProtocols.setObjectName("tblProtocols")
        self.verticalLayout_4.addWidget(self.tblProtocols)
        self.horizontalWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.btnPrintProtocol = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.btnPrintProtocol.setEnabled(False)
        self.btnPrintProtocol.setObjectName("btnPrintProtocol")
        self.horizontalLayout_4.addWidget(self.btnPrintProtocol)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.btnCreateProtocol = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.btnCreateProtocol.setObjectName("btnCreateProtocol")
        self.horizontalLayout_4.addWidget(self.btnCreateProtocol)
        self.btnEditProtocol = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.btnEditProtocol.setEnabled(False)
        self.btnEditProtocol.setObjectName("btnEditProtocol")
        self.horizontalLayout_4.addWidget(self.btnEditProtocol)
        self.verticalLayout_4.addWidget(self.horizontalWidget_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.pnlDocuments.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Заявки"))
        self.btnPrintApplication.setText(_translate("MainWindow", "Печать"))
        self.btnCreateApplication.setText(_translate("MainWindow", "Создать"))
        self.btnEditApplication.setText(_translate("MainWindow", "Изменить"))
        self.label_2.setText(_translate("MainWindow", "Договор"))
        self.lblContractNumber.setText(_translate("MainWindow", "№"))
        self.btnPrintContract.setText(_translate("MainWindow", "Печать"))
        self.btnCreateContract.setText(_translate("MainWindow", "Создать"))
        self.btnEditContract.setText(_translate("MainWindow", "Изменить"))
        self.label_3.setText(_translate("MainWindow", "Счет"))
        self.lblAccountNumber.setText(_translate("MainWindow", "№"))
        self.btnPrintAccount.setText(_translate("MainWindow", "Печать"))
        self.btnCreateAccount.setText(_translate("MainWindow", "Создать"))
        self.btnEditAccount.setText(_translate("MainWindow", "Изменить"))
        self.label_4.setText(_translate("MainWindow", "Приказ"))
        self.lblOrderNumber.setText(_translate("MainWindow", "№"))
        self.btnPrintOrder.setText(_translate("MainWindow", "Печать"))
        self.btnCreateOrder.setText(_translate("MainWindow", "Создать"))
        self.btnEditOrder.setText(_translate("MainWindow", "Изменить"))
        self.label_5.setText(_translate("MainWindow", "Протоколы"))
        self.btnPrintProtocol.setText(_translate("MainWindow", "Печать"))
        self.pushButton_12.setText(_translate("MainWindow", "Удалить"))
        self.btnCreateProtocol.setText(_translate("MainWindow", "Создать"))
        self.btnEditProtocol.setText(_translate("MainWindow", "Изменить"))

