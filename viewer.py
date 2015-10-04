# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
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

class Ui_zoomTem(QMainWindow):

    def __init__(self,content,num):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(820, 977)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 800, 920))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 930, 800, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.close)
        self.textBrowser.setOpenExternalLinks(True)

        if num == 6:
            self.textBrowser.setText(content)
        if num == 8:
            self.textBrowser.setHtml(content)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "Zoomed Template", None))
        self.pushButton.setText(_translate("self", "Close Viewer", None))

