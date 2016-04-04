# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import sharedFun

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

class searchDialog(QtGui.QWidget):

    def __init__(self, tree, wordList):
        QtGui.QWidget.__init__(self)
        self.setupUi(self, tree, wordList)
        self.indexCount = 0
        self.researchResults = 0
        self.resultsList = []

    def setupUi(self, dialog, tree, wordList):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(457, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit = QtGui.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 15, 311, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 15, 75, 23))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 45, 81, 23))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 45, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(130, 55, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 55, 47, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 55, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.completeSearch(wordList)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        searchFunc = lambda : self.searchTemplate(tree)
        self.pushButton.clicked.connect(searchFunc)

        selectNext = lambda : self.selectNext()
        selectPrevious = lambda : self.selectPrevious()

        self.pushButton_2.clicked.connect(selectPrevious)
        self.pushButton_3.clicked.connect(selectNext)
        self.lineEdit.returnPressed.connect(searchFunc)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Search...", None))
        self.lineEdit.setPlaceholderText(_translate("dialog", "Search...", None))
        self.pushButton.setToolTip(_translate("dialog", "Search", None))
        self.pushButton.setText(_translate("dialog", "Search", None))
        self.pushButton_2.setToolTip(_translate("dialog", "Previous template", None))
        self.pushButton_2.setText(_translate("dialog", "<< Previous", None))
        self.pushButton_3.setToolTip(_translate("dialog", "Next Template", None))
        self.pushButton_3.setText(_translate("dialog", "Next >>", None))
        self.label.setText(_translate("dialog", "0", None))
        self.label_2.setText(_translate("dialog", "of", None))
        self.label_3.setText(_translate("dialog", "0", None))

    def searchTemplate(self, tree):
        key = self.lineEdit.text()
        if len(key) > 0:
            current = tree.selectedItems()
            if len(current) != 0:
                current[0].setSelected(False)
            self.indexCount = 0
            self.resultsList = []
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.navigateTree(tree.invisibleRootItem(), key)
            self.researchResults = len(self.resultsList)
            if self.researchResults == 0:
                self.label.setText("0")
                self.label_3.setText("0")
            else:
                self.label.setText("1")
                self.label_3.setText(str(self.researchResults))
                self.resultsList[self.indexCount].setSelected(True)
                self.pushButton_3.setEnabled(True)

    def navigateTree(self, root, key):
        for i in range(root.childCount()):
            item = root.child(i)
            itemName = item.text(0)
            if itemName.toLower().__contains__(key.toLower()) and item.childCount() == 0:
                self.resultsList.append(item)
            elif item.childCount != 0:
                self.navigateTree(item, key)

    def selectNext(self):
        if self.researchResults == 0 or self.indexCount >= self.researchResults -1:
            self.pushButton_3.setEnabled(False)
        elif self.indexCount < self.researchResults -1:
            self.pushButton_3.setEnabled(True)
            self.resultsList[self.indexCount].setSelected(False)
            self.indexCount += 1
            self.label.setText(str(self.indexCount + 1))
            self.resultsList[self.indexCount].setSelected(True)
            if self.indexCount >= self.researchResults -1:
                self.pushButton_3.setEnabled(False)
            if self.indexCount != 0:
                self.pushButton_2.setEnabled(True)

    def selectPrevious(self):
        if self.researchResults == 0 or self.indexCount == 0:
            self.pushButton_2.setEnabled(False)
        elif self.indexCount > 0:
            self.pushButton_2.setEnabled(True)
            self.resultsList[self.indexCount].setSelected(False)
            self.indexCount -= 1
            self.label.setText(str(self.indexCount + 1))
            self.resultsList[self.indexCount].setSelected(True)
            if self.indexCount == 0:
                self.pushButton_2.setEnabled(False)
            if self.indexCount < self.researchResults -1:
                self.pushButton_3.setEnabled(True)

    def completeSearch(self, wordList):
        completer = QCompleter()
        self.lineEdit.setCompleter(completer)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        model = QStringListModel()
        completer.setModel(model)
        completer.popup().setStyleSheet(sharedFun.getColor())
        fixedList = []
        for i in wordList:
            fixedList.append(i.replace(".txt",""))
        model.setStringList(fixedList)



