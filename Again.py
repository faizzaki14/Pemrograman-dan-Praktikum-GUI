# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Again.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):

    def tomain(self):
        from Rantang import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.setupUi(self.window)
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
        self.buttonYa = QtWidgets.QPushButton(self.frame)
        self.buttonYa.setGeometry(QtCore.QRect(80, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonYa.setFont(font)
        self.buttonYa.setStyleSheet("background-color: rgb(235, 89, 110);\n"
"color: rgb(255, 255, 255);")
        self.buttonYa.setObjectName("buttonYa")

        self.buttonYa.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tomain()))
        self.buttonYa.clicked.connect(MainWindow.close)

        self.ButtonTidak = QtWidgets.QPushButton(self.frame)
        self.ButtonTidak.setGeometry(QtCore.QRect(240, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonTidak.setFont(font)
        self.ButtonTidak.setStyleSheet("background-color: rgb(235, 89, 110);\n"
"color: rgb(255, 255, 255);")
        self.ButtonTidak.setObjectName("ButtonTidak")

        self.ButtonTidak.clicked.connect(MainWindow.close)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 60, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 24pt \"Rockwell\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonYa.setText(_translate("MainWindow", "YA"))
        self.ButtonTidak.setText(_translate("MainWindow", "Tidak"))
        self.label.setText(_translate("MainWindow", "Transaksi Kembali ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

