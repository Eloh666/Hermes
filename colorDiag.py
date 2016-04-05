# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import diag
import sharedFun
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class colorDialog(QtGui.QWidget):

    def __init__(self, closeFunc):
        QtGui.QWidget.__init__(self)
        self.setupUi(self, closeFunc)
        self.selectedValue = 0


    def setupUi(self, Form, closeFunc):
        Form.setObjectName(_fromUtf8("Change Theme"))
        Form.resize(501, 121)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 80, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 461, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 181, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 80, 181, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.initializeStatus()
        changeColorLight = lambda : self.changeColor(0)
        changeColorDark = lambda : self.changeColor(1)
        self.radioButton.clicked.connect(changeColorLight)
        self.radioButton_2.clicked.connect(changeColorDark)
        okButton = lambda : self.okButton(closeFunc)
        self.pushButton.clicked.connect(okButton)
        self.pushButton_2.clicked.connect(self.close)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.radioButton.setText(_translate("Form", "Default", None))
        self.radioButton_2.setText(_translate("Form", "Dark Style", None))
        self.label.setText(_translate("Form", "Do you wanna change the color scheme of the application?", None))
        self.pushButton.setText(_translate("Form", "Ok (Restart Required)", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))

        self.setFont()

    def setFont(self):
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)
        self.radioButton.setFont(font)
        self.radioButton_2.setFont(font)
        self.label.setFont(font)

    def changeColor(self, value):
        self.selectedValue = value

    def okButton(self, closeFunc):
        if self.selectedValue == 1:
            replaced = "light"
            replacer = "dark"
        elif self.selectedValue == 0:
            replaced = "dark"
            replacer = "light"
        if self.configData[6].__contains__(replacer):
            print self.configData[6]
            self.myOtherWindow = diag.changedDiag("Reboot not necessary", "No changes made, theme already active.")
            self.myOtherWindow.setStyleSheet(sharedFun.getColor())
            self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
            self.myOtherWindow.show()
        else:
            config = open("Config.txt", "w")
            self.configData[6] = self.configData[6].replace(replaced,replacer)
            config.writelines(self.configData)
            config.close()
            closeFunc()

    def initializeStatus(self):
        f = open("Config.txt","r")
        self.configData = f.readlines()
        if self.configData[6].__contains__("dark"):
            self.radioButton_2.setChecked(True)
            self.selectedValue = 1
        else:
            self.radioButton.setChecked(True)
            self.selectedValue = 0
        f.close()