# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latihan3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from closeprice import *
import pyqtgraph as pg
from candleplot import *
from yahoo_finance import Share
import numpy as np
import threading
lock = threading.Lock()

rbf=[]
lin=[]
def rbf_func(s):
    global rbf
    #lock.acquire()
    rbf=prediction_rbf(s)
    #lock.release()
def lin_func(s):
    global lin
    #lock.acquire()
    lin=prediction_lin(s)
    #lock.release()
    
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 3, 3, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_6.addLayout(self.gridLayout_3, 4, 0, 3, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 6, 1, 1, 1)
        self.PEG_ratio = QtWidgets.QLineEdit(self.centralwidget)
        self.PEG_ratio.setObjectName("PEG_ratio")
        self.gridLayout_6.addWidget(self.PEG_ratio, 6, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6.addLayout(self.gridLayout_4, 7, 0, 2, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 1, 4, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 2, 3)
        self.PE_ratio = QtWidgets.QLineEdit(self.centralwidget)
        self.PE_ratio.setObjectName("PE_ratio")
        self.gridLayout_6.addWidget(self.PE_ratio, 3, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 2, 3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.showplot = QtWidgets.QPushButton(self.centralwidget)
        self.showplot.setObjectName("showplot")
        self.gridLayout_7.addWidget(self.showplot, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 4, 4, 3, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(15, 168, 57, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(15, 415, 57, 20))
        self.label_4.setObjectName("label_4")
        self.divyield = QtWidgets.QLineEdit(self.centralwidget)
        self.divyield.setGeometry(QtCore.QRect(78, 415, 412, 20))
        self.divyield.setObjectName("divyield")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.calculate)
        self.showplot.clicked.connect(self.splot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Analyzer"))
        self.label.setText(_translate("MainWindow", "Input Ticker"))
        self.label_3.setText(_translate("MainWindow", "PEG"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.showplot.setText(_translate("MainWindow", "Show Plot"))
        self.label_2.setText(_translate("MainWindow", "P/E ratio"))
        self.label_4.setText(_translate("MainWindow", "Div Yield"))

    def calculate(self):
        s=Share(str(self.lineEdit.text()))
        self.PE_ratio.setText(str(s.get_price_earnings_ratio()))
        self.PEG_ratio.setText(str(s.get_price_earnings_growth_ratio()))
        self.divyield.setText(str(s.get_dividend_yield()))
    def splot(self):
        global rbf
        global lin
        s=str(self.lineEdit.text())
        
        v=volume(s)
        t=np.arange(1,len(v)+1,1.0)
        #bg=pg.BarGraphItem(x=t, height=v, width=0.6,brush='b')
        judul=s.upper()
          
        a=[rbf_func,lin_func]
        threads=[]
        #threading process 
        for i in a:
            t=threading.Thread(target=i , args=(s,))
            threads.append(t)    
            t.start()
        for thread in threads:
            thread.join()
        #rbf_func(s)
        #lin_func(s)
        judul=s.upper()
        plt = pg.plot(title=judul)
        plt.addLegend()
        item = CandlestickItem(get_data(s))
        plt.addItem(item)
        plt.plot(rbf)
        plt.plot(lin)
        plt.plot(ma_20(s), pen=pg.mkPen('b', width=1),name='MA_20')
        plt.plot(ma_50(s), pen=pg.mkPen('r', width=1), name='MA_50')
        
        #plt.plot(np.reshape(prediction_neural(s),(a,)), pen=pg.mkPen('g', width=1), label = 'Neural')
        #plt.setXRange(100, 150, padding=0) 
        #plt.plot(prediction_poly(s))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

