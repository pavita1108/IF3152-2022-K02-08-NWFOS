# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ITB\Sem 5\RPL\Tubes\RPL_Kelompok8\src\cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cart(object):
    def setupUi(self, Cart):
        Cart.setObjectName("Cart")
        Cart.resize(1279, 720)
        Cart.setStyleSheet("")
        self.tableWidget = QtWidgets.QTableWidget(Cart)
        self.tableWidget.setGeometry(QtCore.QRect(20, 190, 1231, 431))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableQidget #tableWidget{\n"
"    border-style : solid;\n"
"    border : 0px;\n"
"    padding : 10px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.labelHarga = QtWidgets.QLabel(Cart)
        self.labelHarga.setGeometry(QtCore.QRect(320, 110, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelHarga.setFont(font)
        self.labelHarga.setStyleSheet("QLabel#labelHarga{\n"
"    border-radius : 10px;\n"
"    border : 1px;\n"
"    border-style : solid;\n"
"    font : 20px;\n"
"    padding : 6px;\n"
"}")
        self.labelHarga.setFrameShape(QtWidgets.QFrame.Box)
        self.labelHarga.setText("")
        self.labelHarga.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHarga.setObjectName("labelHarga")
        self.labelNama = QtWidgets.QLabel(Cart)
        self.labelNama.setGeometry(QtCore.QRect(20, 110, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelNama.setFont(font)
        self.labelNama.setStyleSheet("QLabel#labelNama{\n"
"    border-radius : 10px;\n"
"    border : 1px;\n"
"    border-style : solid;\n"
"    font : 20px;\n"
"    padding : 6px;\n"
"}")
        self.labelNama.setFrameShape(QtWidgets.QFrame.Box)
        self.labelNama.setText("")
        self.labelNama.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNama.setObjectName("labelNama")
        self.labelTotal = QtWidgets.QLabel(Cart)
        self.labelTotal.setGeometry(QtCore.QRect(530, 110, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelTotal.setFont(font)
        self.labelTotal.setStyleSheet("QLabel#labelTotal{\n"
"    border-radius : 10px;\n"
"    border : 1px;\n"
"    border-style : solid;\n"
"    font : 20px;\n"
"    padding : 6px;\n"
"}")
        self.labelTotal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelTotal.setText("")
        self.labelTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTotal.setObjectName("labelTotal")
        self.kuantitasText = QtWidgets.QLineEdit(Cart)
        self.kuantitasText.setGeometry(QtCore.QRect(900, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kuantitasText.setFont(font)
        self.kuantitasText.setStyleSheet("QLineEdit#kuantitasText{\n"
"    border-radius: 10px;\n"
"    border:1px;\n"
"    border-style:solid;\n"
"    font:14px;\n"
"    padding:6px;\n"
"}")
        self.kuantitasText.setText("")
        self.kuantitasText.setFrame(True)
        self.kuantitasText.setObjectName("kuantitasText")
        self.minButton = QtWidgets.QPushButton(Cart)
        self.minButton.setGeometry(QtCore.QRect(850, 120, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.minButton.setFont(font)
        self.minButton.setStyleSheet("QPushButton#minButton {\n"
"    background-color: #56BB86;\n"
"    border-radius: 10px;\n"
"    font:30px;\n"
"    color:#000;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#minButton:hover {\n"
"    background-color:rgb(46, 209, 119);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton#minButton:pressed {\n"
"    background-color:rgb(58, 127, 90);\n"
"    border-style: inset;\n"
"}")
        self.minButton.setObjectName("minButton")
        self.plusButton = QtWidgets.QPushButton(Cart)
        self.plusButton.setGeometry(QtCore.QRect(990, 120, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("QPushButton#plusButton {\n"
"    background-color: #56BB86;\n"
"    border-radius: 10px;\n"
"    font:28px;\n"
"    color:#000;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#plusButton:hover {\n"
"    background-color:rgb(46, 209, 119);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton#plusButton:pressed {\n"
"    background-color:rgb(58, 127, 90);\n"
"    border-style: inset;\n"
"}")
        self.plusButton.setObjectName("plusButton")
        self.resiButton = QtWidgets.QPushButton(Cart)
        self.resiButton.setGeometry(QtCore.QRect(1100, 640, 141, 41))
        self.resiButton.setStyleSheet("QPushButton#resiButton {\n"
"    background-color: rgb(225, 225, 225);\n"
"    border-radius: 10px;\n"
"    border:1px;\n"
"    border-style:solid;\n"
"    font:16px;\n"
"    color:#000;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#resiButton:hover {\n"
"    background-color:rgb(213, 231, 231);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton#resiButton:pressed {\n"
"    background-color:rgb(190, 190, 190);\n"
"    border-style: inset;\n"
"}")
        self.resiButton.setObjectName("resiButton")
        self.cartHeader = QtWidgets.QFrame(Cart)
        self.cartHeader.setGeometry(QtCore.QRect(0, 0, 1281, 71))
        self.cartHeader.setStyleSheet("QFrame#cartHeader{\n"
"    background-color : rgb(86, 187, 134)\n"
"}")
        self.cartHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cartHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cartHeader.setObjectName("cartHeader")
        self.cartLabel = QtWidgets.QLabel(self.cartHeader)
        self.cartLabel.setGeometry(QtCore.QRect(550, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cartLabel.setFont(font)
        self.cartLabel.setStyleSheet("QLabel#cartLabel{\n"
"    font:32px;\n"
"    font-weight: bold;\n"
"    color:#fff;\n"
"}")
        self.cartLabel.setObjectName("cartLabel")
        self.back_2 = QtWidgets.QPushButton(self.cartHeader)
        self.back_2.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.back_2.setFont(font)
        self.back_2.setStyleSheet("QPushButton#back_2 {\n"
"    background-color: rgb(86, 187, 134);\n"
"    border-radius: 10px;\n"
"    font:28px;\n"
"    font-weight: bold;\n"
"    color:#fff;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton#back_2:pressed {\n"
"    color:#ddd;\n"
"    border-style: inset;\n"
"}")
        self.back_2.setObjectName("back_2")
        self.label_4 = QtWidgets.QLabel(Cart)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Cart)
        self.label_5.setGeometry(QtCore.QRect(320, 90, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Cart)
        self.label_2.setGeometry(QtCore.QRect(530, 90, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cartHeader.raise_()
        self.tableWidget.raise_()
        self.labelHarga.raise_()
        self.labelNama.raise_()
        self.labelTotal.raise_()
        self.kuantitasText.raise_()
        self.minButton.raise_()
        self.plusButton.raise_()
        self.resiButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_2.raise_()

        self.retranslateUi(Cart)
        QtCore.QMetaObject.connectSlotsByName(Cart)

    def retranslateUi(self, Cart):
        _translate = QtCore.QCoreApplication.translate
        Cart.setWindowTitle(_translate("Cart", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Cart", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Cart", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Cart", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Cart", "Total"))
        self.minButton.setText(_translate("Cart", "-"))
        self.plusButton.setText(_translate("Cart", "+"))
        self.resiButton.setText(_translate("Cart", "Cetak Resi"))
        self.cartLabel.setText(_translate("Cart", "Keranjang"))
        self.back_2.setText(_translate("Cart", "< Back"))
        self.label_4.setText(_translate("Cart", "Nama Makanan"))
        self.label_5.setText(_translate("Cart", "Harga (Rp)"))
        self.label_2.setText(_translate("Cart", "Total (Rp)"))
