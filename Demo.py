import sys
from No1 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoNo1(QDialog):
    def __init__(self,parent = None):
        QDialog. __init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonTambah)
        self.ui.pushButton_2.clicked.connect(self.buttonEdit)
        self.ui.pushButton_3.clicked.connect(self.buttonClear)
        self.ui.pushButton_4.clicked.connect(self.buttonHapus)

    def buttonTambah(self):
        QMessageBox.information(self, 'Tambah', 'Data %s Sukses ditambah!' %self.ui.lineEdit.text())
        QMessageBox.information(self, 'Tambah', 'Data %s Sukses ditambah!' %self.ui.lineEdit_2.text())
        QMessageBox.information(self, 'Tambah', 'Data %s Sukses ditambah!' %self.ui.lineEdit_3.text())
        QMessageBox.information(self, 'Tambah', 'Data %s Sukses ditambah!' %self.ui.lineEdit_4.text())
    def buttonEdit(self):
        QMessageBox.information(self, 'Edit', 'Data %s Sukses di Edit!' %self.ui.lineEdit.text())
        QMessageBox.information(self, 'Edit', 'Data %s Sukses di Edit!' %self.ui.lineEdit_2.text())
        QMessageBox.information(self, 'Edit', 'Data %s Sukses di Edit!' %self.ui.lineEdit_3.text())
        QMessageBox.information(self, 'Edit', 'Data %s Sukses di Edit!' %self.ui.lineEdit_4.text())
    def buttonClear(self):
        QMessageBox.information(self, 'Clear', 'Data %s Sukses di Clear!' %self.ui.lineEdit.text())
        QMessageBox.information(self, 'Clear', 'Data %s Sukses di Clear!' %self.ui.lineEdit_2.text())
        QMessageBox.information(self, 'Clear', 'Data %s Sukses di Clear!' %self.ui.lineEdit_3.text())
        QMessageBox.information(self, 'Clear', 'Data %s Sukses di Clear!' %self.ui.lineEdit_4.text())
    def buttonHapus(self):
        QMessageBox.information(self, 'Hapus', 'Data %s Sukses di Hapus!' %self.ui.lineEdit.text())
        QMessageBox.information(self, 'Hapus', 'Data %s Sukses di Hapus!' %self.ui.lineEdit_2.text())
        QMessageBox.information(self, 'Hapus', 'Data %s Sukses di Hapus!' %self.ui.lineEdit_3.text())
        QMessageBox.information(self, 'Hapus', 'Data %s Sukses di Hapus!' %self.ui.lineEdit_4.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = DemoNo1()
    form.show()
    a.exec_()
