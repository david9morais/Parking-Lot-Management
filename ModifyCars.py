# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyCars.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyCar(object):
    def setupUi(self, ModifyCar):
        ModifyCar.setObjectName("ModifyCar")
        ModifyCar.resize(438, 363)
        self.centralwidget = QtWidgets.QWidget(ModifyCar)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Modify_PNum = QtWidgets.QLabel(self.centralwidget)
        self.label_Modify_PNum.setGeometry(QtCore.QRect(30, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Modify_PNum.setFont(font)
        self.label_Modify_PNum.setObjectName("label_Modify_PNum")
        self.cBox_Modify_Fuel = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_Modify_Fuel.setGeometry(QtCore.QRect(120, 230, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cBox_Modify_Fuel.setFont(font)
        self.cBox_Modify_Fuel.setObjectName("cBox_Modify_Fuel")
        self.cBox_Modify_Fuel.addItem("")
        self.cBox_Modify_Fuel.addItem("")
        self.cBox_Modify_Fuel.addItem("")
        self.cBox_Modify_Fuel.addItem("")
        self.cBox_Modify_Fuel.addItem("")
        self.label_Modify_Make = QtWidgets.QLabel(self.centralwidget)
        self.label_Modify_Make.setGeometry(QtCore.QRect(30, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Modify_Make.setFont(font)
        self.label_Modify_Make.setObjectName("label_Modify_Make")
        self.lineEdit_Modify_Color = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Modify_Color.setGeometry(QtCore.QRect(120, 180, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Modify_Color.setFont(font)
        self.lineEdit_Modify_Color.setObjectName("lineEdit_Modify_Color")
        self.label_Modify_Model = QtWidgets.QLabel(self.centralwidget)
        self.label_Modify_Model.setGeometry(QtCore.QRect(30, 130, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Modify_Model.setFont(font)
        self.label_Modify_Model.setObjectName("label_Modify_Model")
        self.label_Modify_Color = QtWidgets.QLabel(self.centralwidget)
        self.label_Modify_Color.setGeometry(QtCore.QRect(30, 180, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Modify_Color.setFont(font)
        self.label_Modify_Color.setObjectName("label_Modify_Color")
        self.lineEdit_Modify_Model = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Modify_Model.setGeometry(QtCore.QRect(120, 130, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Modify_Model.setFont(font)
        self.lineEdit_Modify_Model.setObjectName("lineEdit_Modify_Model")
        self.label_Modify_Fuel = QtWidgets.QLabel(self.centralwidget)
        self.label_Modify_Fuel.setGeometry(QtCore.QRect(30, 230, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Modify_Fuel.setFont(font)
        self.label_Modify_Fuel.setObjectName("label_Modify_Fuel")
        self.lineEdit_Modify_PNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Modify_PNum.setGeometry(QtCore.QRect(120, 30, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Modify_PNum.setFont(font)
        self.lineEdit_Modify_PNum.setObjectName("lineEdit_Modify_PNum")
        self.lineEdit_Modify_Make = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Modify_Make.setGeometry(QtCore.QRect(120, 80, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_Modify_Make.setFont(font)
        self.lineEdit_Modify_Make.setObjectName("lineEdit_Modify_Make")
        self.pushBtn_Modify = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn_Modify.setGeometry(QtCore.QRect(260, 280, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushBtn_Modify.setFont(font)
        self.pushBtn_Modify.setObjectName("pushBtn_Modify")
        ModifyCar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyCar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        ModifyCar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifyCar)
        self.statusbar.setObjectName("statusbar")
        ModifyCar.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyCar)
        QtCore.QMetaObject.connectSlotsByName(ModifyCar)

    def retranslateUi(self, ModifyCar):
        _translate = QtCore.QCoreApplication.translate
        ModifyCar.setWindowTitle(_translate("ModifyCar", "Modify Car"))
        self.label_Modify_PNum.setText(_translate("ModifyCar", "Plate number"))
        self.cBox_Modify_Fuel.setItemText(0, _translate("ModifyCar", "Diesel"))
        self.cBox_Modify_Fuel.setItemText(1, _translate("ModifyCar", "Gasoline"))
        self.cBox_Modify_Fuel.setItemText(2, _translate("ModifyCar", "Gas"))
        self.cBox_Modify_Fuel.setItemText(3, _translate("ModifyCar", "Bio-Diesel"))
        self.cBox_Modify_Fuel.setItemText(4, _translate("ModifyCar", "Electric"))
        self.label_Modify_Make.setText(_translate("ModifyCar", "Make"))
        self.label_Modify_Model.setText(_translate("ModifyCar", "Model"))
        self.label_Modify_Color.setText(_translate("ModifyCar", "Color"))
        self.label_Modify_Fuel.setText(_translate("ModifyCar", "Fuel"))
        self.pushBtn_Modify.setText(_translate("ModifyCar", "Modify"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyCar = QtWidgets.QMainWindow()
    ui = Ui_ModifyCar()
    ui.setupUi(ModifyCar)
    ModifyCar.show()
    sys.exit(app.exec_())