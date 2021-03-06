from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import os
import sharedFun
import webbrowser

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

class SreS(QtGui.QWidget):
    def __init__(self, sResult, lang, lines):
        QMainWindow.__init__(self)
        self.buttonsStack = []
        self.searchTheStuff(sResult, lang, lines)
        self.setObjectName(_fromUtf8("self"))
        self.resize(500, 880)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(420, 830, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.close)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "Search Results", None))
        self.label.setText(_translate("self", "Search Results:", None))
        self.pushButton.setText(_translate("self", "Ok", None))
        self.setFont()

    def setFont(self):
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.pushButton.setFont(font)


    def closeEvent(self,event):
        self.close()

    def searchTheStuff(self,sResult, lang, lines):
        found = 0
        data = sResult
        Yinc = 25
        path = sharedFun.selLang(lang, lines)
        path = path.replace("\n","")
        Y = 40
        X = 20
        results = 0
        for path, dirs, files in os.walk(path, topdown=True):
            for name in files:
                if name.endswith('.txt'):
                    fullpath = os.path.join(path, name)
                    mail = self.open_close(fullpath)
                    if mail.find(data) != -1 and results < 64:
                        found = 1
                        self.buttonsStack.append(QtGui.QPushButton(self))
                        command = lambda checked, path=fullpath: webbrowser.open(path)
                        self.buttonsStack[results].clicked.connect(command)
                        self.buttonsStack[results].setText(_translate("self", name, None))
                        self.buttonsStack[results].setGeometry(QtCore.QRect(X, Y, 220, 20))
                        results = results+1
                        if results == 33:
                            X = 260
                            Y = 15
                        Y = Y + Yinc
        if found == 0:
            self.label = QtGui.QLabel(self)
            self.label.setGeometry(QtCore.QRect(20, 40, 321, 21))
            self.label.setText(_translate("self", "No templates have been found:", None))


    def open_close(self,fullpath):
        f1 = open(fullpath, 'r')
        mail = f1.read()
        f1.close()
        return mail






