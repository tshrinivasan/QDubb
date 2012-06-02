# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QDubb.ui'
#
# Created: Sat Jun  2 14:58:26 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QDubb(object):
    def setupUi(self, QDubb):
        QDubb.setObjectName(_fromUtf8("QDubb"))
        QDubb.resize(800, 600)
        self.centralwidget = QtGui.QWidget(QDubb)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.buttonLoad = QtGui.QPushButton(self.centralwidget)
        self.buttonLoad.setGeometry(QtCore.QRect(30, 160, 98, 27))
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.textLine = QtGui.QTextEdit(self.centralwidget)
        self.textLine.setGeometry(QtCore.QRect(30, 40, 641, 84))
        self.textLine.setObjectName(_fromUtf8("textLine"))
        self.textFile = QtGui.QTextEdit(self.centralwidget)
        self.textFile.setGeometry(QtCore.QRect(30, 230, 431, 311))
        self.textFile.setObjectName(_fromUtf8("textFile"))
        self.buttonClose = QtGui.QPushButton(self.centralwidget)
        self.buttonClose.setGeometry(QtCore.QRect(480, 510, 98, 27))
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.buttonPrevious = QtGui.QPushButton(self.centralwidget)
        self.buttonPrevious.setGeometry(QtCore.QRect(160, 160, 98, 27))
        self.buttonPrevious.setObjectName(_fromUtf8("buttonPrevious"))
        self.buttonNext = QtGui.QPushButton(self.centralwidget)
        self.buttonNext.setGeometry(QtCore.QRect(310, 160, 98, 27))
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.labelCounter = QtGui.QLabel(self.centralwidget)
        self.labelCounter.setGeometry(QtCore.QRect(710, 80, 66, 17))
        self.labelCounter.setText(_fromUtf8(""))
        self.labelCounter.setObjectName(_fromUtf8("labelCounter"))
        QDubb.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QDubb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QDubb.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QDubb)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QDubb.setStatusBar(self.statusbar)

        self.retranslateUi(QDubb)
        QtCore.QObject.connect(self.buttonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), QDubb.close)
        QtCore.QMetaObject.connectSlotsByName(QDubb)

    def retranslateUi(self, QDubb):
        QDubb.setWindowTitle(QtGui.QApplication.translate("QDubb", "QDubb", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoad.setText(QtGui.QApplication.translate("QDubb", "Load a File", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClose.setText(QtGui.QApplication.translate("QDubb", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPrevious.setText(QtGui.QApplication.translate("QDubb", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNext.setText(QtGui.QApplication.translate("QDubb", "Next", None, QtGui.QApplication.UnicodeUTF8))

