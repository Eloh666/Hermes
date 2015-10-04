# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Ermes(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(330, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("winged_foot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 10, 311, 171))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(15, 170, 301, 300))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Icons\hermes.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 490, 300, 30))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.close)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "About", None))
        self.label.setText(_translate("self", "Hermes is a Customer Service oriented email writing help program with intergrated template archive and browser.\n"
"\n"
"Every right reserved to Davide Maurilio Morello, coder and lead designer. We hope that using this program will ease out your work days and make your hours more bearable. \n"
"\n"
"For any further information or bug report please do refer to:\n"
"\n"
"davidemaurilio.morello@gmail.com\n"
"", None))
        self.pushButton.setText(_translate("self", "OK", None))

