# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 570)
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(10, 330, 271, 51))
        self.search.setObjectName("search")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label.setObjectName("label")
        self.lon = QtWidgets.QLineEdit(Form)
        self.lon.setGeometry(QtCore.QRect(10, 40, 271, 20))
        self.lon.setObjectName("lon")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 271, 16))
        self.label_2.setObjectName("label_2")
        self.lat = QtWidgets.QLineEdit(Form)
        self.lat.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.lat.setObjectName("lat")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 271, 16))
        self.label_3.setObjectName("label_3")
        self.scale = QtWidgets.QLineEdit(Form)
        self.scale.setGeometry(QtCore.QRect(10, 270, 271, 20))
        self.scale.setObjectName("scale")
        self.map = QtWidgets.QLabel(Form)
        self.map.setGeometry(QtCore.QRect(291, 60, 450, 450))
        self.map.setText("")
        self.map.setObjectName("map")
        self.map_showing = QtWidgets.QRadioButton(Form)
        self.map_showing.setGeometry(QtCore.QRect(380, 10, 91, 19))
        self.map_showing.setObjectName("map_showing")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.map_showing)
        self.sattelite_showing = QtWidgets.QRadioButton(Form)
        self.sattelite_showing.setGeometry(QtCore.QRect(480, 10, 91, 19))
        self.sattelite_showing.setObjectName("sattelite_showing")
        self.buttonGroup.addButton(self.sattelite_showing)
        self.gibrid_showing = QtWidgets.QRadioButton(Form)
        self.gibrid_showing.setGeometry(QtCore.QRect(580, 10, 91, 19))
        self.gibrid_showing.setObjectName("gibrid_showing")
        self.buttonGroup.addButton(self.gibrid_showing)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(760, 10, 271, 16))
        self.label_4.setObjectName("label_4")
        self.requested = QtWidgets.QTextEdit(Form)
        self.requested.setGeometry(QtCore.QRect(760, 40, 271, 121))
        self.requested.setObjectName("requested")
        self.clear_dots = QtWidgets.QPushButton(Form)
        self.clear_dots.setGeometry(QtCore.QRect(760, 330, 281, 51))
        self.clear_dots.setObjectName("clear_dots")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(760, 240, 271, 16))
        self.label_5.setObjectName("label_5")
        self.other_scale = QtWidgets.QLineEdit(Form)
        self.other_scale.setGeometry(QtCore.QRect(760, 270, 271, 20))
        self.other_scale.setObjectName("other_scale")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search.setText(_translate("Form", "Вывод"))
        self.label.setText(_translate("Form", "Широта:"))
        self.label_2.setText(_translate("Form", "Долгота:"))
        self.label_3.setText(_translate("Form", "Масштабирование(0-17):"))
        self.map_showing.setText(_translate("Form", "Схема"))
        self.sattelite_showing.setText(_translate("Form", "Спутник"))
        self.gibrid_showing.setText(_translate("Form", "Гибрид"))
        self.label_4.setText(_translate("Form", "Интересует какой-то определённый адрес?"))
        self.clear_dots.setText(_translate("Form", "Очистить"))
        self.label_5.setText(_translate("Form", "Масштабирование(0-17):"))
