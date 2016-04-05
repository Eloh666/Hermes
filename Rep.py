# -*- coding: utf-8 -*-

from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import viewer
import os
import searchTab
import sqlite3
import sharedFun

Config = open("Config.txt","r")
lines=Config.readlines()
Config.close()

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

class Archive(QtGui.QWidget):

    def __init__(self, tedit, fillRecent, selectedLang):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resultsList = []
        self.templatesLocations = []
        self.guidesLocations = []
        self.currentlyDisplayedTemplate = ""
        self.htmlData = ""
        self.resize(1198, 636)

#           TEXT BROWSER

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(280, 70, 641, 521))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.textBrowser.setOpenExternalLinks(True)


#            PUSH BUTTONS

        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 600, 91, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\document-download-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 600, 81, 31))
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 600, 91, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\copy-xxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 10, 81, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\search-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(840, 10, 81, 31))
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 50, 181, 20))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\zoom-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_3.clicked.connect(self.close)
        command3 = lambda checked, : self.addTemplate(tedit,self.textBrowser.toPlainText(),fillRecent, selectedLang)
        self.pushButton_2.clicked.connect(command3)
        command4 = lambda checked,: self.copyTemplate(fillRecent, selectedLang)
        self.pushButton_4.clicked.connect(command4)
        self.pushButton_7.clicked.connect(self.zoomTemplate)
        self.pushButton_2.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_4.setEnabled(False)
#           LABELS

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(420, 0, 360, 41))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

#            TREE WIDGET 1

        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 261, 621))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _translate("self", "Topics", None))

        self.templatesLocations = self.initializeLists(self.treeWidget, sharedFun.selLang(selectedLang, lines).replace("\n",""))

        self.databaseFill()
        fillRecent()

        command = lambda : self.displaySelected(self.treeWidget.selectedItems(), 6, selectedLang)
        self.treeWidget.itemSelectionChanged.connect(command)

#            TREE WIDGET 2

        self.treeWidget_2 = QtGui.QTreeWidget(self)
        self.treeWidget_2.setGeometry(QtCore.QRect(930,10, 261, 621))
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget_2.headerItem().setText(0, _translate("self", "Topics", None))

        self.guidesLocations = self.initializeLists(self.treeWidget_2, lines[8].replace("\n","\\"))


        command2 = lambda : self.displaySelected(self.treeWidget_2.selectedItems(), 8, [])
        self.treeWidget_2.itemSelectionChanged.connect(command2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Archive", "Archive", None))

#Push Buttons
        self.pushButton_2.setText(_translate("self", "Add", None))
        self.pushButton_3.setText(_translate("self", "Cancel", None))
        self.pushButton_4.setText(_translate("self", "Copy", None))
        self.pushButton_5.setText(_translate("self", "Search", None))
        self.pushButton_6.setText(_translate("self", "Search", None))
        self.pushButton_7.setText(_translate("self", "Zoom", None))

        searchTree = lambda : self.searchButton(self.treeWidget, self.templatesLocations)
        self.pushButton_5.clicked.connect(searchTree)

        searchTree = lambda: self.searchButton(self.treeWidget_2, self.guidesLocations)
        self.pushButton_6.clicked.connect(searchTree)

#Label
        self.label.setText(_translate("self", "Welcome to the Archive! Please select a template.", None))

        self.setFont()

    def setFont(self):
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.treeWidget.setFont(font)
        self.treeWidget_2.setFont(font)
        font.setBold(False)
        self.textBrowser.setFont(font)

    def copyTemplate(self, fillRecent, selectedLang):
        data = self.textBrowser.toPlainText()
        data = unicode(data)
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(data, mode=cb.Clipboard)
        node = self.treeWidget.selectedItems()
        selectedNode = node[0]
        path = sharedFun.selLang(selectedLang, lines).replace("\n","")+self.backWardPath(selectedNode)+self.currentlyDisplayedTemplate
        sharedFun.increaseDBValue(self.currentlyDisplayedTemplate, str(path), lines[26])
        fillRecent()

    def zoomTemplate(self):
        self.myOtherWindow = viewer.Ui_zoomTem(self.htmlData)
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.show()

    def addTemplate(self,editor,data, fillRecent, selectedLang):
        editor.setText(data)
        node = self.treeWidget.selectedItems()
        selectedNode = node[0]
        path = sharedFun.selLang(selectedLang, lines).replace("\n", "") + self.backWardPath(
        selectedNode) + self.currentlyDisplayedTemplate
        sharedFun.increaseDBValue(self.currentlyDisplayedTemplate, str(path), lines[26])
        fillRecent()
        self.close()

    def initializeLists(self, tree, path):
        locationTuples = []
        for files in os.listdir(path):
            item = QTreeWidgetItem([files.replace(".txt", "")])
            if os.path.isdir(os.path.join(path, files)):
                locationTuples = self.addSubItems(tree, item, path+"\\"+files, locationTuples)
            else:
                locationTuples.append((path,files))
            if os.path.isdir(os.path.join(path, files)) or files.endswith("txt") or files.endswith("html"):
                tree.addTopLevelItem(item)
        return locationTuples


    def addSubItems(self, tree, item, path, locationTuples):
        for files in os.listdir(path):
                newItem = QTreeWidgetItem([files.replace(".txt", "")])
                if os.path.isdir(os.path.join(path, files)):
                    locationTuples = self.addSubItems(tree, newItem, path+"\\"+files, locationTuples)
                else:
                    locationTuples.append((path,files))
                if os.path.isdir(os.path.join(path, files)) or files.endswith("txt") or files.endswith("html"):
                    item.addChild(newItem)
        return locationTuples

    def searchButton(self, tree, tuplesList):
        wordList = []
        for i in tuplesList:
            wordList.append(i[1])
        self.myOtherWindow = searchTab.searchDialog(tree, wordList)
        self.myOtherWindow.setWindowModality(Qt.ApplicationModal)
        self.myOtherWindow.setStyleSheet(sharedFun.getColor())
        self.myOtherWindow.show()

    def databaseFill(self):
        database = sqlite3.connect("Database\\agentDatabase.db")
        visitCursor = database.cursor()
        visitCursor.execute('''CREATE TABLE IF NOT EXISTS personal(
                            usedTimes int,
                            name text,
                            path text,
                            lastUsed datetime,
                            UNIQUE(name,
                            path)
                            )''')
        for i,j in self.templatesLocations:
            visitCursor.execute("INSERT OR IGNORE INTO personal "
                                "VALUES (?, ?, ?, ?)", (0, j, i+"\\"+j, 0))
        database.commit()
        database.close()
        self.updateMainDB()

    def displaySelected(self, tree, num, selectedLang):
        if len(tree) != 0:
            node = tree[0]
            if num == 6:
                path =  sharedFun.selLang(selectedLang, lines).replace("\n","") + self.backWardPath(node) + node.text(0) + ".txt"
            else:
                path = lines[num].replace("\n", "") + self.backWardPath(node) + node.text(0) + ".txt"
            self.openTemplate(path, num, str(node.text(0)))

    def openTemplate(self, value, num, title):
        try:
            f1 = open(value, 'r')
            global data
            data = f1.read()
            self.pushButton_7.setEnabled(True)
            if num == 8:
                self.textBrowser.setHtml(data)
                self.pushButton_2.setEnabled(False)
                self.pushButton_4.setEnabled(False)
            if num == 6:
                self.textBrowser.setText(data)
                self.pushButton_2.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.label.setText(title)
                self.currentlyDisplayedTemplate = title + ".txt"
            f1.close()
            self.htmlData = data
        except:
            self.textBrowser.setPlainText("Template invalid, please check if the file has been modified.")
            self.label.setText("Please select a template")
            self.pushButton_2.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_7.setEnabled(False)

    def backWardPath(self, item):
        parents = []
        path = "\\"
        cursor = item.parent()
        while cursor != None:
            parents.append(cursor.text(0) + "\\")
            cursor = cursor.parent()
        for i in reversed(parents):
            path += i
        return path

    def updateMainDB(self):
        mainDatabasePath = lines[26] + "\\mainDatabase.db"
        mainDatabase = sqlite3.connect(mainDatabasePath)
        mainDatabaseCursor = mainDatabase.cursor()
        mainDatabaseCursor.execute('''CREATE TABLE IF NOT EXISTS usageInformation(
                                usedTimes int,
                                name text,
                                path text,
                                lastUsed datetime,
                                UNIQUE(name,
                                path)
                                )''')
        personalDatabasePath = "Database\\agentDatabase.db"
        agentDatabase = sqlite3.connect(personalDatabasePath)
        agentDatabaseCursor = agentDatabase.cursor()
        agentDatabaseData = agentDatabaseCursor.execute(
            "SELECT * FROM personal")
        for usedTimes, name, path, lastUsed in agentDatabaseData:
            mainDatabaseCursor.execute("INSERT OR IGNORE INTO usageInformation "
                                       "VALUES (?, ?, ?, ?)", (usedTimes, name, path, lastUsed))
        mainDatabase.commit()
        mainDatabase.close()
        agentDatabase.close()




