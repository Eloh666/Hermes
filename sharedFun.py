# -*- coding: utf-8 -*-

import re

from PyQt4 import QtGui
from PyQt4.Qt import *

lastPTR = ""

def leHandler(comboBox,lineEdit):
    checkFlag = comboBox.currentText()
    if checkFlag == "Other":
        lineEdit.setEnabled(True)
    else:
        lineEdit.setEnabled(False)

def OpenButton(line,textEdit):
    path = line.replace("\n","")
    fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file',path,
                        ("Text (*.txt *.rtf)"))
    f = open(fname, 'r')
    with f:
        data = f.read()
        textEdit.setText(data)

def SaveButton(line,textEdit):
    path = line.replace("\n","")
    data = textEdit.toPlainText()
    fname = QtGui.QFileDialog.getSaveFileName(None,"Save File",
                        path+"/myNewTemplate.txt",
                        ("Text (*.txt *.rtf)"))
    f = open(fname, 'w')
    with f:
        f.write(data)
        f.close()

def CopyButton(textEdit):
    data = textEdit.toPlainText()
    data = unicode(data)
    cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(data, mode=cb.Clipboard)

def confirmEvent(event, eventMessage):
    reply = QtGui.QMessageBox.question(None, 'Message',
    eventMessage, QtGui.QMessageBox.Yes |
    QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
        event()

def InitIssue(lng,lineEdit,comboBox):
    result = comboBox.currentText()
    if result == "SEN Account":
        if lng == 1:
            result = 'il tuo Account Sony Entertainment Network (SEN)'
        if lng == 2:
            result = 'your Sony Entertainment Network (SEN) Account'
    if result == "Other":
        result = lineEdit.displayText()
    result = result + '.'
    result = unicode(result)
    return result

def proofreader(lng, text):
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

def AddTemplate(lng,name,lineEdit,comboBox, textEdit):
    data = textEdit.toPlainText()
    data = proofreader(lng, data)
    global lastPTR
    lastPTR = data
    name = name.replace("\n","")
    newbody = ""
    if lng == 1:
        newbody += 'Ciao $contacts.name.first,\n\n'
        newbody +='Grazie per il tuo recente contatto con il Supporto PlayStation per quanto riguarda '
    if lng == 2:
        newbody +='Hi $contacts.name.first,\n\n'
        newbody +='Thanks for contacting PlayStation support regarding '
    if lng == 3:
        newbody +='Hei $contacts.name.first,\n\n'
        newbody +='Tack för ditt meddelande till PlayStation Support.'
    if lng == 4:
        newbody +='Hej $contacts.name.first,\n\n'
        newbody +='Tak for din henvendelse til PlayStation Support. Dit referencenummer er $incidents.ref_no.'
    if lng == 5:
        newbody +='Hei! $contacts.name.first,\n\n'
        newbody +='Kiitos yhteydenotostasi PlayStation-tukeen.'
    if lng == 6:
        newbody +='Hei $contacts.name.first,\n\n'
        newbody +='Takk for e-posten din til PlayStation Support - referansenummeret ditt er $incidents.ref_no.'
    if lng == 7:
        newbody +='Szanowny Panie/Szanowna Pani,\n\n'
        newbody +='Dzi\xc4\x99kuj\xc4\x99 za skontaktowanie si\xc4\x99 z Centrum Obs\xc5\x82ugi Klienta PlayStation.'
        newbody +='\nDotyczy zg\xc5\x82oszenia o numerze: $incidents.ref_no '
    if lng ==1 or lng == 2:
        issue = InitIssue(lng,lineEdit,comboBox)
        newbody += issue
    newbody += '\n\n'
    newbody += data
    if lng == 1:
        newbody += '\n\nNel caso avessi bisogno di ulteriore assistenza ti invitiamo a ricontattare il Supporto PlayStation citando il numero di Riferimento $incidents.ref_no, usando i dettagli in fondo a questa pagina, o rispondendo a questa e-mail, ed un membro del nostro team sarà lieto di aiutarti.'
        newbody += '\n\nGrazie,'
    if lng == 2:
        newbody += "\n\nIf you are in need of further assistance please don't hesitate to contact us again, quoting this reference number $incidents.ref_no, through the details at the bottom of this page and by replying to this message. A member of our team will be happy to help."
        newbody += '\n\nRegards,'
    if lng == 3:
        newbody += '\n\nJag hoppas det här varit till hjälp, om du har några fler frågor kan du kontakta PlayStation Support via uppgifterna nedan eller genom att svara på det här meddelandet. Uppge <as-html><b>$incidents.ref_no</b></as-html> om du kontaktar oss igen.'
        newbody += '\n\nVänliga hälsningar'
    if lng == 4:
        newbody += '\n\nJeg håber dette har været til hjælp. Hvis du har yderligere spørgsmål kan du kontakte PlayStation Support på telefon eller ved at svare på denne e-mail. Oplys venligst følgende referencenummer, når du kontakter os: $incidents.ref_no.'
        newbody += '\n\nMed venlig hilsen,'
    if lng == 5:
        newbody += '\n\nToivottavasti tästä oli apua. Jos sinulle tulee lisää kysyttävää, ota yhteyttä PlayStation-tukeen käyttämällä alla olevia yhteystietoja tai vastaamalla tähän sähköpostiin. Yhteyttä ottaessanne mainitkaa tapausnumeronne $incidents.ref_no.'
        newbody += '\n\nKiitos!'
    if lng == 6:
        newbody += '\n\nJeg håper dette hjelper, men hvis du har flere spørsmål kan du ta kontakt med PlayStation Support ved hjelp av kontaktinformasjonen nedenfor eller ved å svare på denne e-posten.'
        newbody += 'Hilsen,'
    if lng == 7:
        newbody += '\n\nW przypadku dodatkowych pyta\xc5\x84 zach\xc4\x99cam do kontaktu z COK PlayStation odpowiadaj\xc4\x85c bezpo\xc5\x9brednio na t\xc4\x85 wiadomo\xc5\x9b\xc4\x87 b\xc4\x85d\xc5\xba korzystaj\xc4\x85c z danych kontaktowych poni\xc5\xbcej.'
        newbody += '\n\nSerdecznie pozdrawiam,'
    newbody += '\n'
    newbody += '\n\n'
    newbody += name
    if lng == 1:
        newbody += '\nSupporto PlayStation'
    if lng == 2:
        newbody += '\nPlayStation Support'
    if lng == 3:
        newbody += '\nPlayStation Support'
    if lng == 4:
        newbody += '\nPlayStation Support'
    if lng == 5:
        newbody += '\nPlayStation-tukit'
    if lng == 6:
        newbody += '\nPlayStation Support'
    if lng == 7:
        newbody += '\nCentrum Obs\xc5\x82ugi Klienta PlayStation'
    newbody = unicode(newbody)
    textEdit.clear()
    textEdit.insertPlainText(newbody)
    cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(newbody, mode=cb.Clipboard)


class Highlighter(QSyntaxHighlighter):

    WORDS = u'(?iu)[\w\']+'

    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)

        self.dict = None

    def setDict(self, dict):
        self.dict = dict

    def highlightBlock(self, text):
        if not self.dict:
            return

        text = unicode(text)

        format = QTextCharFormat()
        format.setUnderlineColor(Qt.red)
        format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)

        for word_object in re.finditer(self.WORDS, text):
            if not self.dict.check(word_object.group()):
                self.setFormat(word_object.start(),
                    word_object.end() - word_object.start(), format)


class SpellAction(QAction):

    '''
    A special QAction that returns the text in a signal.
    '''

    correct = pyqtSignal(unicode)

    def __init__(self, *args):
        QAction.__init__(self, *args)

        self.triggered.connect(lambda x: self.correct.emit(
            unicode(self.text())))
