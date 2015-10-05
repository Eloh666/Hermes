# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniME.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import Rep
import sharedFun
import enchant

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal

Config = open("Config.txt","r")
lines=Config.readlines()
Config.close()

global lng
lng = 1


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

class MiniMe(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(485, 667)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 120, 461, 501))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 90, 150, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setEnabled(False)

        self.dict = enchant.Dict("it_IT")

        self.highlighter = sharedFun.Highlighter(self.textEdit.document())
        self.highlighter.setDict(self.dict)

# PUSH BUTTONS

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 0, 73, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-archive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 0, 40, 40))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-document-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(37, 37))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2")
                                        )
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 0, 40, 40))
        self.pushButton_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-folder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(37, 37))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 0, 40, 40))
        self.pushButton_4.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-disk-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(37, 37))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 0, 40, 40))
        self.pushButton_5.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-document-cross-icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(37, 37))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 80, 73, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\edit-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.pushButton_7.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\copy-gxxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

# COMBO BOX

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 171, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Italy-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\United-Kingdom-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, _fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sweden-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon9, _fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Denmark-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon10, _fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Finland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon11, _fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Norway-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon12, _fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Poland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon13, _fromUtf8(""))

        self.comboBox.activated.connect(self.langSelect)

# COMBO BOX 2

        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 90, 171, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\PlayStation-4-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon14, _fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-2-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon15, _fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Games-Playstation-3-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon16, _fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon17, _fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\ita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon18, _fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-Portable-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon19, _fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon20, _fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Security-Question-Shield-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_2.addItem(icon21, _fromUtf8(""))
        self.setCentralWidget(self.centralwidget)

        leHand = lambda checked, :sharedFun.leHandler(self.comboBox_2,self.lineEdit)
        self.comboBox_2.activated.connect(leHand)

# MENU BAR

        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(self)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(self)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(self)
        self.actionSave.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionConvert = QtGui.QAction(self)
        self.actionConvert.setObjectName(_fromUtf8("actionConvert"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionConvert)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.pushButton.clicked.connect(self.marcCaller) # archive

        opFile = lambda checked, : sharedFun.OpenButton(lines[24],self.textEdit)
        savFile = lambda checked, : sharedFun.SaveButton(lines[24],self.textEdit)
        CopyButton = lambda checked, : sharedFun.CopyButton(self.textEdit)
        openConf = lambda checked, : sharedFun.confirmEvent(self.textEdit.clear,"This will delete your current work,\n\n Do you want to proceed?")
        ripLastConf = lambda checked, : sharedFun.confirmEvent(self.Clear_Last,"This will remove your changes,\n\n Do you want to proceed?")
        mainButton = lambda checked, : sharedFun.AddTemplate(lng,lines[4],self.lineEdit,self.comboBox_2,self.textEdit)

        self.pushButton_3.clicked.connect(opFile) # open
        self.pushButton_4.clicked.connect(savFile) # save
        self.pushButton_7.clicked.connect(CopyButton) # copy
        self.pushButton_2.clicked.connect(openConf) # new
        self.pushButton_5.clicked.connect(ripLastConf) # clearlist
        self.pushButton_6.clicked.connect(mainButton)

        self.actionNew.triggered.connect(openConf)
        self.actionOpen.triggered.connect(opFile)
        self.actionSave.triggered.connect(savFile)
        self.actionQuit.triggered.connect(self.close)
        self.actionConvert.triggered.connect(mainButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "Mini Me", None))
        self.pushButton_6.setText(_translate("self", "Template", None))
        self.pushButton.setText(_translate("MainWindow", "Archive", None))
        self.comboBox.setItemText(0, _translate("self", "Italian", None))
        self.comboBox.setItemText(1, _translate("self", "English", None))
        self.comboBox.setItemText(2, _translate("self", "Swedish", None))
        self.comboBox.setItemText(3, _translate("self", "Danish", None))
        self.comboBox.setItemText(4, _translate("self", "Finnish", None))
        self.comboBox.setItemText(5, _translate("self", "Norwegian", None))
        self.comboBox.setItemText(6, _translate("self", "Polish", None))
        self.comboBox_2.setItemText(0, _translate("self", "PlayStation 4 (PS4)", None))
        self.comboBox_2.setItemText(1, _translate("self", "DualShock 4 (DS4)", None))
        self.comboBox_2.setItemText(2, _translate("self", "PlayStation 3 (PS3)", None))
        self.comboBox_2.setItemText(3, _translate("self", "DualShock3 (DS3)", None))
        self.comboBox_2.setItemText(4, _translate("self", "PlayStation Vita (PS Vita)", None))
        self.comboBox_2.setItemText(5, _translate("self", "PlayStation Portable (PSP)", None))
        self.comboBox_2.setItemText(6, _translate("self", "SEN Account", None))
        self.comboBox_2.setItemText(7, _translate("self", "Other", None))
        self.menuFile.setTitle(_translate("self", "File", None))
        self.menuEdit.setTitle(_translate("self", "Edit", None))
        self.actionNew.setText(_translate("self", "New", None))
        self.actionOpen.setText(_translate("self", "Open", None))
        self.actionSave.setText(_translate("self", "Save", None))
        self.actionQuit.setText(_translate("self", "Quit", None))
        self.actionConvert.setText(_translate("self", "Convert", None))

        self.textEdit.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress):
            event = QMouseEvent(QEvent.MouseButtonPress, event.pos(),
                Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
            QTextEdit.mousePressEvent(self.textEdit, event)
            self.contextMenuEvent(event)
        return QtGui.QWidget.eventFilter(self, source, event)


    def contextMenuEvent(self, event):
        popup_menu = self.textEdit.createStandardContextMenu()
        cursor = self.textEdit.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        self.textEdit.setTextCursor(cursor)
        if self.textEdit.textCursor().hasSelection():
            text = unicode(self.textEdit.textCursor().selectedText())
            if not self.dict.check(text):
                spell_menu = QMenu('Spelling Suggestions')
                for word in self.dict.suggest(text):
                    action = sharedFun.SpellAction(word, spell_menu)
                    action.correct.connect(self.correctWord)
                    spell_menu.addAction(action)
                if len(spell_menu.actions()) != 0:
                    popup_menu.insertSeparator(popup_menu.actions()[0])
                    popup_menu.insertMenu(popup_menu.actions()[0], spell_menu)

        popup_menu.exec_(event.globalPos())

    def correctWord(self, word):
        cursor = self.textEdit.textCursor()
        cursor.beginEditBlock()
        cursor.removeSelectedText()
        cursor.insertText(word)
        cursor.endEditBlock()

    def marcCaller(self):
        self.myOtherWindow = Rep.Archive(self.textEdit)
        self.myOtherWindow.show()

    def Clear_Last(self):
        self.textEdit.clear()
        self.textEdit.insertPlainText(sharedFun.lastPTR)

    def langSelect(self):
        global lng
        checkFlag = self.comboBox.currentText()
        if checkFlag == "Italian":
            lng = 1;
            self.dict = enchant.Dict("it_IT")

        if checkFlag == "English":
            lng = 2;
            self.dict = enchant.Dict("en_GB")

        if checkFlag == "Swedish":
            lng = 3;
            self.dict = enchant.Dict("sv_SE")

        if checkFlag == "Danish":
            lng = 4;
            self.dict = enchant.Dict("da_DK")

        if checkFlag == "Finnish":
            lng = 5;
            self.dict = enchant.Dict("en_GB")

        if checkFlag == "Norwegian":
            lng = 6;
            self.dict = enchant.Dict("nb_NO")

        if checkFlag == "Polish":
            lng = 7;
            self.dict = enchant.Dict("pl_PL")
        self.highlighter = sharedFun.Highlighter(self.textEdit.document())
        self.highlighter.setDict(self.dict)