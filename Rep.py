# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import viewer




Config = open("Config.txt","r")
lines=Config.readlines()
Config.close()

htmlData = ""
currentNum = 6

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

    def __init__(self, tedit):
        QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("self"))
        self.resize(1198, 636)


#            TEXT BROWSER

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
        #self.pushButton_5 = QtGui.QPushButton(self)
        #self.pushButton_5.setGeometry(QtCore.QRect(280, 10, 81, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons\search-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.pushButton_5.setIcon(icon2)
        #self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        #self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        #self.pushButton_6 = QtGui.QPushButton(self)
        #self.pushButton_6.setGeometry(QtCore.QRect(840, 10, 81, 31))
        #self.pushButton_6.setIcon(icon2)
        #self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        #self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 50, 181, 20))
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_3.clicked.connect(self.close)
        command3 = lambda checked, : self.addTemplate(tedit,self.textBrowser.toPlainText())
        self.pushButton_2.clicked.connect(command3)
        self.pushButton_4.clicked.connect(self.copyTemplate)
        self.pushButton_7.clicked.connect(self.zoomTemplate)
        self.pushButton_2.setEnabled(False)
        self.pushButton_7.setEnabled(False)

#           LABELS

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(320, 20, 391, 41))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)

#            TREE WIDGET 1

        self.treeWidget = QtGui.QTreeWidget(self)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 261, 621))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)

        command = lambda : self.loadAllMessages(self.treeWidget.selectedItems(),6)
        self.treeWidget.itemSelectionChanged.connect(command)


#            TREE WIDGET 2

        self.treeWidget_2 = QtGui.QTreeWidget(self)
        self.treeWidget_2.setGeometry(QtCore.QRect(930, 10, 261, 621))
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)

        command2 = lambda : self.loadAllMessages(self.treeWidget_2.selectedItems(),8)
        self.treeWidget_2.itemSelectionChanged.connect(command2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Archive", "Archive", None))

#Tree Widget 1
        self.treeWidget.headerItem().setText(0, _translate("self", "Topics", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("self", "Templates UK", None))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("self", "PlayStation 4", None))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("self", "Online RMA", None))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("self", "Safemode PS4", None))
        self.treeWidget.topLevelItem(0).child(0).child(2).setText(0, _translate("self", "And all the other templates", None))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("self", "PlayStation 3", None))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("self", "Safemode PS3", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

#Tree Widget 2
        self.treeWidget_2.headerItem().setText(0, _translate("self", "Topics", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("self", "Guides UK", None))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("self", "PlayStation 4", None))
        self.treeWidget_2.topLevelItem(0).child(0).child(0).setText(0, _translate("self", "PS4 on fire", None))
        self.treeWidget_2.topLevelItem(0).child(0).child(1).setText(0, _translate("self", "Restore Licences", None))
        self.treeWidget_2.topLevelItem(0).child(0).child(2).setText(0, _translate("self", "Something Something", None))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, _translate("self", "PlayStation 3", None))
        self.treeWidget_2.topLevelItem(0).child(1).child(0).setText(0, _translate("self", "Safemode PS3", None))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)

#Push Buttons
        self.pushButton_2.setText(_translate("self", "Add", None))
        self.pushButton_3.setText(_translate("self", "Cancel", None))
        self.pushButton_4.setText(_translate("self", "Copy", None))
        #self.pushButton_5.setText(_translate("self", "Search", None))
        #self.pushButton_6.setText(_translate("self", "Search", None))
        self.pushButton_7.setText(_translate("self", "Zoom", None))
#Label
        self.label.setText(_translate("self", "Welcome to the Archive! Please select a template.", None))


    def loadAllMessages(self, tree, num):
        global currentNum
        currentNum = num
        if num == 8:
            self.pushButton_2.setEnabled(False)
            self.pushButton_7.setEnabled(False)
        getSelected = tree
        if getSelected:
            baseNode = getSelected[0]
            Node = baseNode.text(0)
            Node = str(Node)
            self.label.setText("Please select a category")
            prePath = lines[num].replace("\n","")

            try:
                NodePath = prePath+Node+".txt"
                f1 = open(NodePath, 'r')
                title = f1.readline(-1)
                title = title.replace("\n","")
                f1.readline(-1)
                global htmlData
                htmlData = f1.read()
                self.pushButton_7.setEnabled(True)
                if num == 8:
                    self.textBrowser.setHtml(htmlData)
                if num == 6:
                    self.textBrowser.setText(htmlData)
                    self.pushButton_2.setEnabled(True)
                self.label.setText(title)
                f1.close()
            except:
                txt = ""
                self.textBrowser.setPlainText("")
                self.label.setText("Please select a template")
                self.pushButton_2.setEnabled(False)
                self.pushButton_2.setEnabled(False)


    def copyTemplate(self):
        data = self.textBrowser.toPlainText()
        data = unicode(data)
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(data, mode=cb.Clipboard)

    def zoomTemplate(self):
        self.myOtherWindow = viewer.Ui_zoomTem(htmlData, currentNum)
        self.myOtherWindow.show()

    def addTemplate(self,editor,data):
        editor.setText(data)
        self.close()
