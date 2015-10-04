# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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

class changedDiag(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(389, 100)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 25, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.close)


    def retranslateUi(self):
        self.setWindowTitle(_translate("Changed", "Changed", None))
        self.label.setText(_translate("self", "Your name has been changed.", None))
        self.pushButton.setText(_translate("self", "OK", None))

