# -*- coding: utf-8 -*-

import sys
import enchant
import Rep
import diag
import sres
import about
import sharedFun
import extendedCbox
import sqlite3
import os
import colorDiag
import threading

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *


sys.stderr = sys.stdout
reload(sys)
sys.setdefaultencoding('utf8')

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

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):

        Config = open("Config.txt", "r")
        self.lines = Config.readlines()
        Config.close()

        self.lng = 1
        self.Sresult = ""

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1127, 900)


#            Text EDIT ------------------------------------------------------------------------------------------------------

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 1081, 661))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.isUndoRedoEnabled ()

        self.textEdit.setFocusPolicy(Qt.StrongFocus)

            #Text EDIT ------------------------------------------------------------------------------------------------------

        self.dict = enchant.Dict("it_IT")

        self.highlighter = sharedFun.Highlighter(self.textEdit.document())
        self.highlighter.setDict(self.dict)

#            COMBO BOX ------------------------------------------------------------------------------------------------------


        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 251, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\PlayStation-4-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-2-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Games-Playstation-3-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\ita.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, _fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sony-Playstation-Portable-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, _fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\playstation-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, _fromUtf8(""))
        iconVR = QtGui.QIcon()
        iconVR.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\\vrIcon.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.comboBox.addItem(iconVR, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Security-Question-Shield-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, _fromUtf8(""))

        self.templatesComboBox = extendedCbox.ExtendedComboBox(MainWindow)
        self.templatesComboBox.setGeometry(QtCore.QRect(17, 187, 500, 21))

        leHand = lambda checked, :sharedFun.leHandler(self.comboBox,self.lineEdit)
        self.comboBox.activated.connect(leHand)


    #   RADIOBUTTONS ------------------------------------------------------------------------------------------------------

        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(300, 90, 77, 51))
        self.radioButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Italy-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon9)
        self.radioButton.setIconSize(QtCore.QSize(40, 40))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 90, 77, 51))
        self.radioButton_2.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\United-Kingdom-ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon10)
        self.radioButton_2.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(480, 90, 77, 51))
        self.radioButton_3.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Sweden-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_3.setIcon(icon11)
        self.radioButton_3.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(570, 90, 77, 51))
        self.radioButton_4.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Denmark-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_4.setIcon(icon12)
        self.radioButton_4.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(750, 90, 77, 51))
        self.radioButton_5.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Norway-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_5.setIcon(icon13)
        self.radioButton_5.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(660, 90, 77, 51))
        self.radioButton_6.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Finland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_6.setIcon(icon14)
        self.radioButton_6.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_7 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(840, 90, 77, 51))
        self.radioButton_7.setText(_fromUtf8(""))
        self.radioButton.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\Poland-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_7.setIcon(icon15)
        self.radioButton_7.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))

        itaLan = lambda checked,: self.r_clicked(1,"it_IT")
        eUkLan = lambda checked,: self.r_clicked(2,"en_GB")
        sweLan = lambda checked,: self.r_clicked(3,"sv_SE")
        danLan = lambda checked,: self.r_clicked(4,"da_DK")
        finLan = lambda checked,: self.r_clicked(5,"en_GB")
        norLan = lambda checked,: self.r_clicked(6,"nb_NO")
        polLan = lambda checked,: self.r_clicked(7,"pl_PL")
        self.radioButton.toggled.connect(itaLan)
        self.radioButton_2.toggled.connect(eUkLan)
        self.radioButton_3.toggled.connect(sweLan)
        self.radioButton_4.toggled.connect(danLan)
        self.radioButton_6.toggled.connect(finLan)
        self.radioButton_5.toggled.connect(norLan)
        self.radioButton_7.toggled.connect(polLan)

    #   PUSHBUTTONS ------------------------------------------------------------------------------------------------------

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 80, 111, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\edit-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 5, 50, 50))
        self.pushButton_2.setText(_fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\document-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon16)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(55, 5, 50, 50))
        self.pushButton_3.setText(_fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\dolder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon17)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(105, 5, 50, 50))
        self.pushButton_4.setText(_fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\disk-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon18)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(155, 5, 50, 50))
        self.pushButton_5.setText(_fromUtf8(""))
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\mail-receive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon19)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(205, 5, 50, 50))
        self.pushButton_6.setText(_fromUtf8(""))
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\mail-send-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon20)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(255, 5, 50, 50))
        self.pushButton_7.setText(_fromUtf8(""))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\document-cross-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon21)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(610, 155, 121, 32))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(929, 80, 61, 61))
        self.pushButton_8.setText(_fromUtf8(""))
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\copy-xxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon23)
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(1000, 10, 121, 32))
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\search-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon25)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_12.setIconSize(QtCore.QSize(26, 26))

        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\chive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon22)
        self.pushButton_10.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(525, 159, 50, 26))
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\ok-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon23)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_13.clicked.connect(self.addSoftTemplate)

        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(950, 159, 50, 26))
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\senIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14.setIconSize(QtCore.QSize(46, 46))

        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(825, 159, 50, 26))
        self.pushButton_15.setIcon(icon24)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_15.setIconSize(QtCore.QSize(31, 31))

        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\green-document-plus-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        openConf = lambda checked, : sharedFun.confirmEvent(self.textEdit.clear,"This will delete your current work,\n\n Do you want to proceed?")
        ripLastConf = lambda checked, : sharedFun.confirmEvent(self.Clear_Last,"This will remove your changes,\n\n Do you want to proceed?")
        opFile = lambda checked, : sharedFun.OpenButton(self.lines[24],self.textEdit)
        savFile = lambda checked, : sharedFun.SaveButton(self.lines[24],self.textEdit)
        CopyButton = lambda checked, : sharedFun.CopyButton(self.textEdit)
        MainButton = lambda checked, : sharedFun.AddTemplate(self.lng, self.lineEdit,self.comboBox,self.textEdit)

        self.pushButton.clicked.connect(MainButton) # sand
        self.pushButton_5.clicked.connect(self.textEdit.undo) #undo
        self.pushButton_6.clicked.connect(self.textEdit.redo) #redo
        self.pushButton_2.clicked.connect(openConf) # new
        self.pushButton_7.clicked.connect(ripLastConf) # clearlist
        self.pushButton_3.clicked.connect(opFile) # open
        self.pushButton_4.clicked.connect(savFile) # save
        self.pushButton_10.clicked.connect(self.MainButton2) # archive
        self.pushButton_8.clicked.connect(CopyButton) # copy
        self.pushButton_12.clicked.connect(self.Search_Temp) # search

        consoleTitle = lambda checked : sharedFun.consoleField(self.lng)
        senTitle = lambda checked : sharedFun.senField(self.lng)

        self.pushButton_14.clicked.connect(consoleTitle)
        self.pushButton_15.clicked.connect(senTitle)



#            LABEL -----------------------------------------------------------------------------------------------------

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 251, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 =  QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 145, 251, 20))
        self.label_2.setObjectName(_fromUtf8("label2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(900, 155, 50, 30))
        self.label_3.setObjectName(_fromUtf8("label2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(775, 155, 50, 30))
        self.label_4.setObjectName(_fromUtf8("label2"))

#            LINE EDITS  -----------------------------------------------------------------------------------------------

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setEnabled(False)

        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(740, 20, 251, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setPlaceholderText(_translate("dialog", "Search...", None))
        self.lineEdit_2.returnPressed.connect(self.Search_Temp)

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
        self.actionChangeTheme = QtGui.QAction(MainWindow)
        self.actionChangeTheme.setObjectName(_fromUtf8("actionChangeTheme"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionDropDB = QtGui.QAction(MainWindow)
        self.actionDropDB.setObjectName(_fromUtf8("actionDropDB"))
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
        self.menuTools.addAction(self.actionChangeTheme)
        self.menuTools.addAction(self.actionChangeMN)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionBrowse_Premade_Templates)
        self.menuTools.addAction(self.actionDropDB)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.quitProgram.triggered.connect(self.closeEvent)
        self.newFile.triggered.connect(openConf)
        self.openFile.triggered.connect(opFile)
        self.saveFile.triggered.connect(savFile)
        self.actionSelect_all.triggered.connect(self.textEdit.selectAll)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionConvert.triggered.connect(MainButton)
        self.actionBrowse_Premade_Templates.triggered.connect(self.MainButton2)
        self.actionChangeMN.triggered.connect(self.nameDiag)
        self.actionAbout.triggered.connect(self.callAbout)
        self.actionChangeTheme.triggered.connect(self.changeTheme)
        self.actionHelp.triggered.connect(self.helpFunc)
        self.actionDropDB.triggered.connect(self.clearDatabase)

        self.recentNumber = 0
        self.templatesList = []
        self.fillRecent()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.templatesComboBox.currentIndexChanged.connect(self.changeIcon)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Sandwich Reborn", "Hermes v2.0.0", None))
        self.pushButton.setText(_translate("MainWindow", "Convert", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "PlayStation 4 (PS4)", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "DualShock 4 (DS4)", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "PlayStation 3 (PS3)", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "DualShock3 (DS3)", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "PlayStation Vita (PS Vita)", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "PlayStation Portable (PSP)", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "SEN Account", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "PlayStation VR", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "Other", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "New", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Open", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Save", None))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Undo", None))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Redo", None))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Clear Last Change", None))
        self.pushButton_10.setText(_translate("MainWindow", "Archive", None))
        self.pushButton_10.setToolTip(_translate("MainWindow", "Archive", None))
        self.pushButton_13.setToolTip(_translate("MainWindow", "Add Template", None))
        self.pushButton_12.setToolTip(_translate("MainWindow", "Search Template", None))
        self.label.setText(_translate("MainWindow", "Topic", None))
        self.label_2.setText(_translate("MainWindow", "Recently used templates: "+str(self.recentNumber)+".\tBrowse:", None))
        self.label_3.setText(_translate("MainWindow", "PS4\nQuery", None))
        self.label_4.setText(_translate("MainWindow", "SEN\nQuery", None))
        self.textEdit.setDocumentTitle(_translate("MainWindow", "Sandwich", None))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Clear Last Change", None))
        self.pushButton_12.setText(_translate("MainWindow", "Search", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "Settings", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.actionChangeTheme.setText(_translate("MainWindow", "Set theme",None))
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
        self.actionBrowse_Premade_Templates.setText(_translate("MainWindow", "Browse", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help!", None))
        self.actionDropDB.setText(_translate("MainWindow", "Clear Database", None))
        self.textEdit.installEventFilter(self)
        self.setFont()

    def setFont(self):
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.comboBox.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        self.pushButton_8.setFont(font)
        self.pushButton_10.setFont(font)
        self.pushButton_12.setFont(font)
        self.pushButton_13.setFont(font)
        self.templatesComboBox.setFont(font)
        font.setPointSize(8)
        self.menuFile.setFont(font)
        self.menuTools.setFont(font)
        self.menuAbout.setFont(font)
        self.menubar.setFont(font)
        self.menuEdit.setFont(font)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress):
            selected = unicode(self.textEdit.textCursor().selectedText())
            if not selected.__contains__(" "):
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
                spell_menu.setStyleSheet(sharedFun.getColor())
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


    def MainButton2(self):
        self.myOtherWindow = Rep.Archive(self.textEdit, self.fillRecent, self.lng)
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.show()

    def callAbout(self):
        self.myOtherWindow = about.Ui_Ermes()
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.show()

    def r_clicked(self, num, dictionary):
        self.lng = num
        self.dict = enchant.Dict(dictionary)
        self.highlighter = sharedFun.Highlighter(self.textEdit.document())
        self.highlighter.setDict(self.dict)

    def nameDiag(self):
        text, ok = QtGui.QInputDialog.getText(None, 'Insert your name',
            'Enter your name:')

        if ok:
            f1 = open("Config.txt", 'w')
            self.lines[4] = text+"\n"
            f1.writelines(self.lines)
            f1.close
            self.nameDiagConf()

    def nameDiagConf(self):
        self.myOtherWindow = diag.changedDiag("Name Changed","Your name has been changed successfully.")
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.show()

    def Clear_Last(self):
        self.textEdit.clear()
        self.textEdit.insertPlainText(sharedFun.lastPTR)

    def open_close(fullpath):
        f1 = open(fullpath, 'r')
        mail = f1.read()
        f1.close()
        return mail

    def Search_Temp(self):
        Scontent = self.lineEdit_2.displayText()
        self.Sresult = Scontent
        if len(Scontent) < 3:
            self.myOtherWindow = diag.changedDiag("Length Error", "The searched word be longer than 3 (three) characters.")
            self.myOtherWindow.setStyleSheet(sharedFun.getColor())
            self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
            self.myOtherWindow.show()
        else:
            self.myOtherWindow = sres.SreS(self.Sresult, self.lng, self.lines)
            self.myOtherWindow.setStyleSheet(sharedFun.getColor())
            self.myOtherWindow.show()


    def closeEvent(self, event):
        quit_msg = "Are you sure you want to quit?"
        closeDialog = QtGui.QMessageBox
        reply = closeDialog.question(None, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QtGui.qApp.quit()
        else:
            event.ignore()

    def closeWarning(self):
        quit_msg = "New color scheme applied. \nPlease start the application again."
        self.myOtherWindow = diag.changedDiag("Rebooting...", quit_msg)
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.show()
        threading.Timer(3.0,QtGui.qApp.quit).start()

    def fillRecent(self):
        if os.path.isfile("Database\\agentDatabase.db"):
            self.recentNumber = 0
            self.templatesList = []
            database = sqlite3.connect("Database\\agentDatabase.db")
            visitCursor = database.cursor()
            visitCursor.execute("SELECT * FROM sqlite_master WHERE name = 'personal' and type = 'table'")
            if visitCursor.fetchone() != None:
                templateTriples = visitCursor.execute(
                    "SELECT  name, path, lang FROM personal WHERE lastUsed != 0 ORDER BY lastUsed DESC LIMIT 10")
                self.templatesComboBox.clear()
                for j, i in enumerate(templateTriples):
                    if os.path.isfile(i[1]):
                        self.templatesComboBox.addItem(i[2]+" - "+i[0].replace(".txt",""), i[1])
                        self.templatesList.append((i[0],i[1]))
                        self.recentNumber += 1
                database.close()
                self.label_2.setText(
                    _translate("MainWindow", "Recently used templates: " + str(self.recentNumber) + ".\t\t      Browse:", None))
                if(self.recentNumber != 0):
                    self.pushButton_13.setEnabled(True)

    def addSoftTemplate(self):
        checkedTemplate = self.templatesComboBox.currentText()
        variant = self.templatesComboBox.itemData(self.templatesComboBox.currentIndex())
        path = variant.toString()
        try:
            templateFile = open(path, 'r')
            with templateFile:
                self.textEdit.setText(templateFile.read())
                templateFile.close()
            sharedFun.increaseDBValue(str(path), self.lines[26])
        finally:
            self.fillRecent()

    def changeTheme(self):
        self.myOtherWindow = colorDiag.colorDialog(self.closeWarning)
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.show()

    def helpFunc(self):
        self.myOtherWindow = diag.changedDiag("Help","Full Guide Coming soon!\n"
                                              "Meanwhile for issues contact me at:\n\ndavide.morello@emea.sykes.com")
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.show()

    def changeIcon(self):
        if self.templatesComboBox.count() != 0:
            self.pushButton_13.setEnabled(True)
        else:
            self.pushButton_13.setEnabled(False)

    def clearDatabase(self):
        quit_msg = "This well clear your history and wipe the database. Proceed?"
        closeDialog = QtGui.QMessageBox
        reply = closeDialog.question(None, 'Message',
                                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            sharedFun.dropTable("Database\\agentDatabase.db")
            self.fillRecent()
            self.templatesComboBox.clear()
            self.recentNumber = 0
            self.label_2.setText(
                _translate("MainWindow", "Recently used templates: " + str(self.recentNumber) + ".\t\t      Browse:",
                           None))


