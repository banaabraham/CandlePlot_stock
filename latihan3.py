# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latihan3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from yahoo_finance import Share

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 2, 3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 3, 3, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 1, 4, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 2, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 3, 1, 1, 1)
        self.PE_ratio = QtWidgets.QLineEdit(self.centralwidget)
        self.PE_ratio.setObjectName("PE_ratio")
        self.gridLayout_6.addWidget(self.PE_ratio, 3, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_6.addLayout(self.gridLayout_3, 4, 0, 2, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 5, 1, 1, 1)
        self.PEG_ratio = QtWidgets.QLineEdit(self.centralwidget)
        self.PEG_ratio.setObjectName("PEG_ratio")
        self.gridLayout_6.addWidget(self.PEG_ratio, 5, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6.addLayout(self.gridLayout_4, 6, 0, 2, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 7, 1, 1, 1)
        self.divyield = QtWidgets.QLineEdit(self.centralwidget)
        self.divyield.setObjectName("divyield")
        self.gridLayout_6.addWidget(self.divyield, 7, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.calculate)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Detail"))
        self.label.setText(_translate("MainWindow", "Input Ticker"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.label_2.setText(_translate("MainWindow", "P/E ratio"))
        self.label_3.setText(_translate("MainWindow", "PEG"))
        self.label_4.setText(_translate("MainWindow", "Div Yield"))

    def calculate(self):
        s=Share(str(self.lineEdit.text()))
        self.PE_ratio.setText(str(s.get_price_earnings_ratio()))
        self.PEG_ratio.setText(str(s.get_price_earnings_growth_ratio()))
        self.divyield.setText(str(s.get_dividend_yield()))
         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

