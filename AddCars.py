# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCars.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddNewCar(object):
    def setupUi(self, AddNewCar):
        AddNewCar.setObjectName("AddNewCar")
        AddNewCar.resize(436, 364)
        self.centralwidget = QtWidgets.QWidget(AddNewCar)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Add_Make = QtWidgets.QLabel(self.centralwidget)
        self.label_Add_Make.setGeometry(QtCore.QRect(30, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Add_Make.setFont(font)
        self.label_Add_Make.setObjectName("label_Add_Make")
        self.label_Add_Model = QtWidgets.QLabel(self.centralwidget)
        self.label_Add_Model.setGeometry(QtCore.QRect(30, 130, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Add_Model.setFont(font)
        self.label_Add_Model.setObjectName("label_Add_Model")
        self.label_Add_PNum = QtWidgets.QLabel(self.centralwidget)
        self.label_Add_PNum.setGeometry(QtCore.QRect(30, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Add_PNum.setFont(font)
        self.label_Add_PNum.setObjectName("label_Add_PNum")
        self.label_Add_Fuel = QtWidgets.QLabel(self.centralwidget)
        self.label_Add_Fuel.setGeometry(QtCore.QRect(30, 230, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Add_Fuel.setFont(font)
        self.label_Add_Fuel.setObjectName("label_Add_Fuel")
        self.label_Add_Color = QtWidgets.QLabel(self.centralwidget)
        self.label_Add_Color.setGeometry(QtCore.QRect(30, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Add_Color.setFont(font)
        self.label_Add_Color.setObjectName("label_Add_Color")
        self.cBox_Add_Fuel = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_Add_Fuel.setGeometry(QtCore.QRect(120, 230, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cBox_Add_Fuel.setFont(font)
        self.cBox_Add_Fuel.setObjectName("cBox_Add_Fuel")
        self.cBox_Add_Fuel.addItem("")
        self.cBox_Add_Fuel.addItem("")
        self.cBox_Add_Fuel.addItem("")
        self.cBox_Add_Fuel.addItem("")
        self.cBox_Add_Fuel.addItem("")
        self.lineEdit_Add_PNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Add_PNum.setGeometry(QtCore.QRect(120, 30, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Add_PNum.setFont(font)
        self.lineEdit_Add_PNum.setObjectName("lineEdit_Add_PNum")
        self.lineEdit_Add_Make = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Add_Make.setGeometry(QtCore.QRect(120, 80, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Add_Make.setFont(font)
        self.lineEdit_Add_Make.setObjectName("lineEdit_Add_Make")
        self.lineEdit_Add_Model = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Add_Model.setGeometry(QtCore.QRect(120, 130, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Add_Model.setFont(font)
        self.lineEdit_Add_Model.setObjectName("lineEdit_Add_Model")
        self.lineEdit_Add_Color = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Add_Color.setGeometry(QtCore.QRect(120, 180, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Add_Color.setFont(font)
        self.lineEdit_Add_Color.setObjectName("lineEdit_Add_Color")
        self.pushBtn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_Add.setGeometry(QtCore.QRect(260, 280, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushBtn_Add.setFont(font)
        self.pushBtn_Add.setObjectName("pushBtn_Add")
        AddNewCar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewCar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 21))
        self.menubar.setObjectName("menubar")
        AddNewCar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewCar)
        self.statusbar.setObjectName("statusbar")
        AddNewCar.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewCar)
        QtCore.QMetaObject.connectSlotsByName(AddNewCar)

    def retranslateUi(self, AddNewCar):
        _translate = QtCore.QCoreApplication.translate
        AddNewCar.setWindowTitle(_translate("AddNewCar", "Add Car"))
        self.label_Add_Make.setText(_translate("AddNewCar", "Make"))
        self.label_Add_Model.setText(_translate("AddNewCar", "Model"))
        self.label_Add_PNum.setText(_translate("AddNewCar", "Plate number"))
        self.label_Add_Fuel.setText(_translate("AddNewCar", "Fuel"))
        self.label_Add_Color.setText(_translate("AddNewCar", "Color"))
        self.cBox_Add_Fuel.setItemText(0, _translate("AddNewCar", "Diesel"))
        self.cBox_Add_Fuel.setItemText(1, _translate("AddNewCar", "Gasoline"))
        self.cBox_Add_Fuel.setItemText(2, _translate("AddNewCar", "Gas"))
        self.cBox_Add_Fuel.setItemText(3, _translate("AddNewCar", "Bio-Diesel"))
        self.cBox_Add_Fuel.setItemText(4, _translate("AddNewCar", "Electric"))
        self.pushBtn_Add.setText(_translate("AddNewCar", "Add"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewCar = QtWidgets.QMainWindow()
    ui = Ui_AddNewCar()
    ui.setupUi(AddNewCar)
    AddNewCar.show()
    sys.exit(app.exec_())