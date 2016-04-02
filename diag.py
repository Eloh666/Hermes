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
    def __init__(self, title, message):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(648, 140)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 10, 421, 111))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setFont(font)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(500, 40, 111, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        font = QtGui.QFont()
        font.setPointSize(11)

        if(title == "Rebooting..."):
            self.pushButton.setEnabled(False)


        self.retranslateUi(title, message)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.close)


    def retranslateUi(self, title, message):
        self.setWindowTitle(_translate("Changed", title, None))
        self.label.setText(_translate("self", message, None))
        self.pushButton.setText(_translate("self", "OK", None))



