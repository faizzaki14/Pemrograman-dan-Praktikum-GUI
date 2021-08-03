# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Payment.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Again import Ui_MainWindow3

class Ui_MainWindow6(object):

    def toAgain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 60, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 24pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.confirmbutton = QtWidgets.QPushButton(self.frame)
        self.confirmbutton.setGeometry(QtCore.QRect(160, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirmbutton.setFont(font)
        self.confirmbutton.setStyleSheet("background-color: rgb(235, 89, 110);\n"
"color: rgb(255, 255, 255);")
        self.confirmbutton.setObjectName("confirmbutton")

        self.confirmbutton.clicked.connect(self.toAgain)
        self.confirmbutton.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Transaksi Berhasil"))
        self.confirmbutton.setText(_translate("MainWindow", "Konfirmasi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

