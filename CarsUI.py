# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarsUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CarList(object):
    def setupUi(self, CarList):
        CarList.setObjectName("CarList")
        CarList.resize(422, 611)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        CarList.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CarList)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Cars = QtWidgets.QLabel(self.centralwidget)
        self.label_Cars.setGeometry(QtCore.QRect(30, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Cars.setFont(font)
        self.label_Cars.setObjectName("label_Cars")
        self.pushBtn_AddCar = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_AddCar.setGeometry(QtCore.QRect(40, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushBtn_AddCar.setFont(font)
        self.pushBtn_AddCar.setObjectName("pushBtn_AddCar")
        self.pushBtn_ModCar = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_ModCar.setGeometry(QtCore.QRect(170, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushBtn_ModCar.setFont(font)
        self.pushBtn_ModCar.setObjectName("pushBtn_ModCar")
        self.pushBtn_DelCar = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_DelCar.setGeometry(QtCore.QRect(300, 520, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushBtn_DelCar.setFont(font)
        self.pushBtn_DelCar.setObjectName("pushBtn_DelCar")
        self.pushBtn_VInv = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_VInv.setGeometry(QtCore.QRect(280, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushBtn_VInv.setFont(font)
        self.pushBtn_VInv.setObjectName("pushBtn_VInv")
        self.listWidget_Cars = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Cars.setGeometry(QtCore.QRect(30, 100, 361, 391))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.listWidget_Cars.setFont(font)
        self.listWidget_Cars.setObjectName("listWidget_Cars")
        CarList.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarList)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        CarList.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(CarList)
        self.toolBar.setObjectName("toolBar")
        CarList.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(CarList)
        QtCore.QMetaObject.connectSlotsByName(CarList)

    def retranslateUi(self, CarList):
        _translate = QtCore.QCoreApplication.translate
        CarList.setWindowTitle(_translate("CarList", "Car List"))
        self.label_Cars.setText(_translate("CarList", "Cars:"))
        self.pushBtn_AddCar.setText(_translate("CarList", "Add car"))
        self.pushBtn_ModCar.setText(_translate("CarList", "Modify car"))
        self.pushBtn_DelCar.setText(_translate("CarList", "Delete car"))
        self.pushBtn_VInv.setText(_translate("CarList", "Valid/Invalid"))
        self.toolBar.setWindowTitle(_translate("CarList", "toolBar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarList = QtWidgets.QMainWindow()
    ui = Ui_CarList()
    ui.setupUi(CarList)
    CarList.show()
    sys.exit(app.exec_())