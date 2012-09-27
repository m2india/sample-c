# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usps.ui'
#
# Created: Wed Sep 26 17:47:49 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 100, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 160, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(26, 180, 81, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 250, 98, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "user name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

