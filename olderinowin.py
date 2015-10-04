# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import Rep
import os
import diag
import sres
import miniME


sys.stderr = sys.stdout
reload(sys)
sys.setdefaultencoding('utf8')

tempFolder = open("newTempPath.txt","r")
temp = tempFolder.read()
tempFolder.close()
lng = 1
Sresult = ""
lastPTR = ""

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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1127, 880)

#            Text EDIT ------------------------------------------------------------------------------------------------------

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 1081, 661))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.isUndoRedoEnabled ()


#            COMBO BOX ------------------------------------------------------------------------------------------------------


        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 251, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("PlayStation-4-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Sony-Playstation-2-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Games-Playstation-3-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Sony-Playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("18j1fnh34eyqkjpg.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, _fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Sony-Playstation-Portable-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, _fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Security-Question-Shield-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, _fromUtf8(""))

        self.comboBox.activated.connect(self.leHandler)

    #   RADIOBUTTONS ------------------------------------------------------------------------------------------------------

        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(300, 90, 77, 51))
        self.radioButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Italy-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon9)
        self.radioButton.setIconSize(QtCore.QSize(50, 50))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 90, 77, 51))
        self.radioButton_2.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("United-Kingdom-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon10)
        self.radioButton_2.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(480, 90, 77, 51))
        self.radioButton_3.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Sweden-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_3.setIcon(icon11)
        self.radioButton_3.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(570, 90, 77, 51))
        self.radioButton_4.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Denmark-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_4.setIcon(icon12)
        self.radioButton_4.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(750, 90, 77, 51))
        self.radioButton_5.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Norway-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_5.setIcon(icon13)
        self.radioButton_5.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(660, 90, 77, 51))
        self.radioButton_6.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Finland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_6.setIcon(icon14)
        self.radioButton_6.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_7 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(840, 90, 77, 51))
        self.radioButton_7.setText(_fromUtf8(""))
        self.radioButton.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Poland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_7.setIcon(icon15)
        self.radioButton_7.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))

        self.radioButton.toggled.connect(self.r1_clicked)
        self.radioButton_2.toggled.connect(self.r2_clicked)
        self.radioButton_3.toggled.connect(self.r3_clicked)
        self.radioButton_4.toggled.connect(self.r4_clicked)
        self.radioButton_5.toggled.connect(self.r5_clicked)
        self.radioButton_6.toggled.connect(self.r6_clicked)
        self.radioButton_7.toggled.connect(self.r7_clicked)

    #   PUSHBUTTONS ------------------------------------------------------------------------------------------------------

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 80, 111, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("edit-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 0, 50, 50))
        self.pushButton_2.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("red-document-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 0, 50, 50))
        self.pushButton_3.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("red-folder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon17)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 0, 50, 50))
        self.pushButton_4.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("red-disk-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon18)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 0, 50, 50))
        self.pushButton_5.setText(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("red-mail-receive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon19)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 0, 50, 50))
        self.pushButton_6.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("red-mail-send-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon20)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 0, 50, 50))
        self.pushButton_7.setText(_fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("red-document-cross-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon21)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(610, 10, 121, 31))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(929, 80, 61, 61))
        self.pushButton_8.setText(_fromUtf8(""))
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("copy-xxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon23)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 0, 50, 50))
        self.pushButton_11.setText(_fromUtf8(""))
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("red-ok-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon24)
        self.pushButton_11.setIconSize(QtCore.QSize(44, 50))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))

        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1000, 10, 121, 32))
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("red-search-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon25)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))

        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("red-archive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon22)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 810, 91, 21))
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("green-document-plus-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon26)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 810, 91, 21))
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("yellow-document-plus-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon27)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 810, 91, 21))
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("blue-document-plus-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon28)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))


        self.pushButton.clicked.connect(self.MainButton) # sand
        self.pushButton_5.clicked.connect(self.textEdit.undo) #undo
        self.pushButton_6.clicked.connect(self.textEdit.redo) #redo
        self.pushButton_2.clicked.connect(self.textEdit.clear) # new
        self.pushButton_3.clicked.connect(self.OpenButton) # open
        self.pushButton_4.clicked.connect(self.SaveButton) # save
        self.pushButton_10.clicked.connect(self.MainButton2) # archive
        self.pushButton_8.clicked.connect(self.CopyButton) # copy
        self.pushButton_7.clicked.connect(self.Clear_Last) # copy
        self.pushButton_12.clicked.connect(self.Search_Temp) # search
        self.pushButton_9.clicked.connect(self.StartMiniMe) # search


#            LABEL -----------------------------------------------------------------------------------------------------

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 251, 20))
        self.label.setObjectName(_fromUtf8("label"))

#            LINE EDITS  -----------------------------------------------------------------------------------------------

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(740, 20, 251, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.lineEdit.setEnabled(False)

#            MENU ------------------------------------------------------------------------------------------------------

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.newFile = QtGui.QAction(MainWindow)
        self.newFile.setObjectName(_fromUtf8("newFile"))
        self.openFile = QtGui.QAction(MainWindow)
        self.openFile.setObjectName(_fromUtf8("openFile"))
        self.saveFile = QtGui.QAction(MainWindow)
        self.saveFile.setObjectName(_fromUtf8("saveFile"))
        self.quitProgram = QtGui.QAction(MainWindow)
        self.quitProgram.setObjectName(_fromUtf8("quitProgram"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionChangeMN = QtGui.QAction(MainWindow)
        self.actionChangeMN.setObjectName(_fromUtf8("actionChangeMN"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSelect_all = QtGui.QAction(MainWindow)
        self.actionSelect_all.setObjectName(_fromUtf8("actionSelect_all"))
        self.actionConvert = QtGui.QAction(MainWindow)
        self.actionConvert.setObjectName(_fromUtf8("actionConvert"))
        self.actionMini_SpellCheck = QtGui.QAction(MainWindow)
        self.actionMini_SpellCheck.setObjectName(_fromUtf8("actionMini_SpellCheck"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionBrowse_Premade_Templates = QtGui.QAction(MainWindow)
        self.actionBrowse_Premade_Templates.setObjectName(_fromUtf8("actionBrowse_Premade_Templates"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.newFile)
        self.menuFile.addAction(self.openFile)
        self.menuFile.addAction(self.saveFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quitProgram)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionMini_SpellCheck)
        self.menuEdit.addAction(self.actionConvert)
        self.menuTools.addAction(self.actionChangeMN)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionBrowse_Premade_Templates)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.quitProgram.triggered.connect(QtGui.qApp.quit)
        self.newFile.triggered.connect(self.textEdit.clear)
        self.openFile.triggered.connect(self.OpenButton)
        self.saveFile.triggered.connect(self.SaveButton)
        self.actionSelect_all.triggered.connect(self.textEdit.selectAll)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionConvert.triggered.connect(self.MainButton)
        self.actionBrowse_Premade_Templates.triggered.connect(self.MainButton2)
        self.actionChangeMN.triggered.connect(self.nameDiag)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Sandwich Reborn", "Sandwich Reborn", None))
        self.pushButton.setText(_translate("MainWindow", "Convert", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "PlayStation 4", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "DualShock 4", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "PlayStation 3", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "DualShock3", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "PlayStation Vita", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "PlayStation Portable", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "SEN Account", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "Other", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "New", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Open", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Save", None))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Undo", None))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Redo", None))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Clear Last Change", None))
        self.pushButton_10.setText(_translate("MainWindow", "Archive", None))
        self.label.setText(_translate("MainWindow", "Topic", None))
        self.textEdit.setDocumentTitle(_translate("MainWindow", "Sandwich", None))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Clear Last Change", None))
        self.pushButton_11.setToolTip(_translate("MainWindow", "Clear Last Change", None))
        self.pushButton_12.setText(_translate("MainWindow", "Search", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.newFile.setText(_translate("MainWindow", "New", None))
        self.openFile.setText(_translate("MainWindow", "Open", None))
        self.saveFile.setText(_translate("MainWindow", "Save", None))
        self.quitProgram.setText(_translate("MainWindow", "Quit", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionChangeMN.setText(_translate("MainWindow", "Change My name", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionSelect_all.setText(_translate("MainWindow", "Select all", None))
        self.actionConvert.setText(_translate("MainWindow", "Convert", None))
        self.actionMini_SpellCheck.setText(_translate("MainWindow", "Mini-SpellCheck", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionBrowse_Premade_Templates.setText(_translate("MainWindow", "Browse Premade Templates", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help!", None))
        self.pushButton_9.setText(_translate("MainWindow", "ExtraPad 1", None))
        self.pushButton_13.setText(_translate("MainWindow", "ExtraPad 2", None))
        self.pushButton_14.setText(_translate("MainWindow", "ExtraPad 3", None))


    def MainButton2(self):
	    self.myOtherWindow = Rep.Archive()
	    self.myOtherWindow.show()

    def InitIssue(self):
        result = self.comboBox.currentText()
        if result == "SEN Account":
            if lng == 1:
                result = 'il tuo Account Sony Entertainment Network (SEN).'
            if lng == 2:
                result = 'your Sony Entertainment Network (SEN) Account.'
        if result == "Other":
            result = self.lineEdit.displayText()
        result = result + '.'
        result = unicode(result)
        return result

    def proofreader(self, text):
        text = unicode(text)
        first_char = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z', 'y', 'j', 'k', 'x', ',', '.', ';', ':', "'", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z', 'Y', 'J', 'K', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '\xc2\xa3', '^', '%', '&', '*', '-', '=', '+', '|', '@', '?', '<', '~', '#')
        for i in first_char:
            text = text.replace(',' + i, ', ' + i)
            text = text.replace(';' + i, '; ' + i)
            text = text.replace(':' + i, ': ' + i)
            for j in first_char:
                a = i + '  ' + j
                b = i + ' ' + j
                text = text.replace(a, b)
        text = text.replace(' ,', ',')
        text = text.replace(' .', '.')
        text = text.replace(' ;', ';')
        text = text.replace(' :', ':')
        text = text.replace(" '", "'")
        if lng == 1:
            text = text.replace("l' ", "l'")
            text = text.replace("l ' ", "l'")
            text = text.replace("n' ", "n'")
            text = text.replace("n ' ", "n'")
            text = text.replace("a'", 'à')
            text = text.replace("e'", 'è')
            text = text.replace("i'", 'ì')
            text = text.replace("o'", 'ò')
            text = text.replace("u'", 'ù')
            text = text.replace("A'", 'À')
            text = text.replace("E'", 'È')
            text = text.replace("I'", 'Ì')
            text = text.replace("O'", 'Ò')
            text = text.replace("U'", 'Ù')
        text = text.replace(' )', ')')
        text = text.replace('( ', '(')
        text = text.replace('$ contacts.name.first', '$contacts.name.first')
        text = text.replace('$ incidents.ref_no', '$incidents.ref_no')
        return text

    def MainButton(self):
        global lastPTR
        data = self.textEdit.toPlainText()
        data = self.proofreader(data)
        lastPTR = data
        f1 = open("myName.txt",'r')
        name = f1.read()
        f1.close()
        newbody = ""
        language = lng
        if language == 1:
            newbody += 'Ciao $contacts.name.first,\n\n'
            newbody +='Grazie per il tuo recente contatto con il Supporto PlayStation per quanto riguarda '
        if language == 2:
            newbody +='Hi $contacts.name.first,\n\n'
            newbody +='Thanks for contacting PlayStation support regarding '
        if language == 3:
            newbody +='Hei $contacts.name.first,\n\n'
            newbody +='Tack för ditt meddelande till PlayStation Support.'
        if language == 4:
            newbody +='Hej $contacts.name.first,\n\n'
            newbody +='Tak for din henvendelse til PlayStation Support. Dit referencenummer er $incidents.ref_no.'
        if language == 5:
            newbody +='Hei! $contacts.name.first,\n\n'
            newbody +='Kiitos yhteydenotostasi PlayStation-tukeen.'
        if language == 6:
            newbody +='Hei $contacts.name.first,\n\n'
            newbody +='Takk for e-posten din til PlayStation Support - referansenummeret ditt er $incidents.ref_no.'
        if language == 7:
            newbody +='Szanowny Panie/Szanowna Pani,\n\n'
            newbody +='Dzi\xc4\x99kuj\xc4\x99 za skontaktowanie si\xc4\x99 z Centrum Obs\xc5\x82ugi Klienta PlayStation.'
            newbody +='\nDotyczy zg\xc5\x82oszenia o numerze: $incidents.ref_no '
        if language != 7:
            issue = self.InitIssue()
            newbody += issue
        newbody += '\n\n'
        newbody += data
        if language == 1:
            newbody += '\n\nNel caso avessi bisogno di ulteriore assistenza ti invitiamo a ricontattare il Supporto PlayStation citando il numero di Riferimento $incidents.ref_no, usando i dettagli in fondo a questa pagina, o rispondendo a questa e-mail, ed un membro del nostro team sarà lieto di aiutarti.'
            newbody += '\n\nGrazie,'
        if language == 2:
            newbody += "\nIf you are in need of further assistance please don't hesitate to contact us again, quoting this reference number $incidents.ref_no, through the details at the bottom of this page and by replying to this message. A member of our team will be happy to help."
            newbody += '\n\nRegards,'
        if language == 3:
            newbody += '\nSJag hoppas det här varit till hjälp, om du har några fler frågor kan du kontakta PlayStation Support via uppgifterna nedan eller genom att svara på det här meddelandet. Uppge <as-html><b>$incidents.ref_no</b></as-html> om du kontaktar oss igen.'
            newbody += '\n\nVänliga hälsningar'
        if language == 4:
            newbody += '\nJeg håber dette har været til hjælp. Hvis du har yderligere spørgsmål kan du kontakte PlayStation Support på telefon eller ved at svare på denne e-mail. Oplys venligst følgende referencenummer, når du kontakter os: $incidents.ref_no.'
            newbody += '\n\nMed venlig hilsen,'
        if language == 5:
            newbody += '\nToivottavasti tästä oli apua. Jos sinulle tulee lisää kysyttävää, ota yhteyttä PlayStation-tukeen käyttämällä alla olevia yhteystietoja tai vastaamalla tähän sähköpostiin. Yhteyttä ottaessanne mainitkaa tapausnumeronne $incidents.ref_no.'
            newbody += '\n\nKiitos!'
        if language == 6:
            newbody += '\nJeg håper dette hjelper, men hvis du har flere spørsmål kan du ta kontakt med PlayStation Support ved hjelp av kontaktinformasjonen nedenfor eller ved å svare på denne e-posten.'
            newbody += 'Hilsen,'
        if language == 7:
            newbody += '\nW przypadku dodatkowych pyta\xc5\x84 zach\xc4\x99cam do kontaktu z COK PlayStation odpowiadaj\xc4\x85c bezpo\xc5\x9brednio na t\xc4\x85 wiadomo\xc5\x9b\xc4\x87 b\xc4\x85d\xc5\xba korzystaj\xc4\x85c z danych kontaktowych poni\xc5\xbcej.'
            newbody += '\n\nSerdecznie pozdrawiam,'
        newbody += '\n'
        newbody += '\n\n'
        newbody += name
        if language == 1:
            newbody += '\nSupporto PlayStation'
        if language == 2:
            newbody += '\nPlayStation Support'
        if language == 3:
            newbody += '\nPlayStation Support'
        if language == 4:
            newbody += '\nPlayStation Support'
        if language == 5:
            newbody += '\nPlayStation-tukit'
        if language == 6:
            newbody += '\nPlayStation Support'
        if language == 7:
            newbody += '\nCentrum Obs\xc5\x82ugi Klienta PlayStation'
        newbody = unicode(newbody)
        self.textEdit.clear()
        self.textEdit.insertPlainText(newbody)
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(newbody, mode=cb.Clipboard)


    def r1_clicked(self, enabled):
        if enabled:
            global lng
            lng = 1
    def r2_clicked(self, enabled):
        if enabled:
            global lng
            lng = 2
    def r3_clicked(self, enabled):
        if enabled:
            global lng
            lng = 3
    def r4_clicked(self, enabled):
        if enabled:
            global lng
            lng = 4
    def r5_clicked(self, enabled):
        if enabled:
            global lng
            lng = 5
    def r6_clicked(self, enabled):
        if enabled:
            global lng
            lng = 6
    def r7_clicked(self, enabled):
        if enabled:
            global lng
            lng = 7

    def OpenButton(self):

        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file',temp,
                           ("Text (*.txt *.rtf)"))

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def SaveButton(self):

        data = self.textEdit.toPlainText()
        fname = QtGui.QFileDialog.getSaveFileName(None,"Save File",
                           temp+"/myNewTemplate.txt",
                           ("Text (*.txt *.rtf)"))

        f = open(fname, 'w')

        with f:
            f.write(data)
            f.close()

    def CopyButton(self):
        data = self.textEdit.toPlainText()
        data = unicode(data)
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(data, mode=cb.Clipboard)

    def nameDiag(self):
        text, ok = QtGui.QInputDialog.getText(None, 'Insert your name',
            'Enter your name:')

        if ok:
            f1 = open("myName.txt", 'w')
            f1.write(text)
            f1.close
            self.nameDiagConf()

    def nameDiagConf(self):
	    self.myOtherWindow = diag.changedDiag()
	    self.myOtherWindow.show()

    def Clear_Last(self):
        self.textEdit.clear()
        self.textEdit.insertPlainText(lastPTR)

    def leHandler(self):
        checkFlag = self.comboBox.currentText()
        if checkFlag == "Other":
            self.lineEdit.setEnabled(True)
        else:
            self.lineEdit.setEnabled(False)


    def open_close(fullpath):
        f1 = open(fullpath, 'r')
        mail = f1.read()
        f1.close()
        return mail

    def Search_Temp(self):
        Scontent = self.lineEdit_2.displayText()
        found = 0
        global Sresult
        Sresult = Scontent
        if len(Scontent) < 3:
            error = QtGui.QErrorMessage(None)
            error.setWindowTitle(_translate("Length Error", "Length Error", None))
            error.showMessage("The search parameter must be longer than 3 (three) characters.")
            error.accept(self.closeEvent)
        else:
            self.myOtherWindow = sres.SreS()
            self.myOtherWindow.show()

    def closeEvent(self,event):
        self.close()

    def StartMiniMe(self):
	    self.myOtherWindow = miniME.MiniMe()
	    self.myOtherWindow.show()



def intermediateCall():
    return Sresult












