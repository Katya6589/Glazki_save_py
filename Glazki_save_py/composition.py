# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'composition.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_composition(object):
    def setupUi(self, composition):
        composition.setObjectName("composition")
        composition.resize(633, 499)
        self.tableWidget = QtWidgets.QTableWidget(composition)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 611, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(composition)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 70, 121, 134))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.layoutWidget1 = QtWidgets.QWidget(composition)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 209, 159))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_9 = QtWidgets.QLabel(composition)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 541, 31))
        self.label_9.setMinimumSize(QtCore.QSize(0, 31))
        self.label_9.setObjectName("label_9")
        self.layoutWidget_2 = QtWidgets.QWidget(composition)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 70, 121, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.retranslateUi(composition)
        QtCore.QMetaObject.connectSlotsByName(composition)

    def retranslateUi(self, composition):
        _translate = QtCore.QCoreApplication.translate
        composition.setWindowTitle(_translate("composition", "Form"))
        self.pushButton.setText(_translate("composition", "Открыть"))
        self.pushButton_2.setText(_translate("composition", "Добавить"))
        self.pushButton_3.setText(_translate("composition", "Удалить"))
        self.label.setText(_translate("composition", "Артикул"))
        self.label_2.setText(_translate("composition", "Дата поступления"))
        self.label_3.setText(_translate("composition", "Дата изготовления"))
        self.label_4.setText(_translate("composition", "ID_агента"))
        self.label_9.setText(_translate("composition", "<html><head/><body><p><span style=\" font-size:24pt;\">Композиция</span></p></body></html>"))
        self.pushButton_10.setText(_translate("composition", "Найти"))
