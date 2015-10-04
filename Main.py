# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
import MainWin

sys.stderr = sys.stdout
reload(sys)
sys.setdefaultencoding('utf8')

lng = 1
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


class Main(QtGui.QMainWindow, MainWin.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainWin.Ui_MainWindow()
        self.ui.setupUi(self)

    def OpenButton(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Icons\winged_foot.png'))
    window = Main()
    window.show()
    sys.exit(app.exec_())




