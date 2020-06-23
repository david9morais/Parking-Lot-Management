import sys, csv
from PyQt5 import QtWidgets, QtCore, QtGui

from CarsUI import Ui_CarList
from AddCars import Ui_AddNewCar
from ModifyCars import Ui_ModifyCar
from Main import Car

class Controller:
    def __init__(self):
        #colors for lines
        self._red = QtGui.QBrush(QtCore.Qt.red)
        self._green = QtGui.QBrush(QtCore.Qt.green)

        self.CarsUI = QtWidgets.QMainWindow()
        self.ui = Ui_CarList()
        self.ui.setupUi(self.CarsUI)
        self.ui.pushBtn_AddCar.clicked.connect(self.openAddCar)
        self.ui.pushBtn_ModCar.clicked.connect(self.openModifyCar)
        self.ui.pushBtn_DelCar.clicked.connect(self.deleteCar)
        self.ui.pushBtn_VInv.clicked.connect(self.Validate)
        self.ui.listWidget_Cars.setWindowFilePath(self.addFile())
        self.CarsUI.show()

    def openAddCar(self):
        self.addNewCarWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_AddNewCar()
        self.ui2.setupUi(self.addNewCarWindow)
        self.ui2.pushBtn_Add.clicked.connect(self.addNewCar)
        self.addNewCarWindow.show()

    def addNewCar(self):
        #Verify if user is entering the complete car information(ADD)
        if self.ui2.lineEdit_Add_PNum.text() == '' or\
           self.ui2.lineEdit_Add_Make.text() == '' or\
           self.ui2.lineEdit_Add_Model.text() == '' or\
           self.ui2.lineEdit_Add_Color.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should enter the complete car information!")
            msg.exec()
        else:
            validCar = "v"
            newCar = []
            newCar.append(self.ui2.lineEdit_Add_PNum.text())#fill the file with Plate Number that we write
            newCar.append(self.ui2.lineEdit_Add_Make.text())#fill the file with Make that we write
            newCar.append(self.ui2.lineEdit_Add_Model.text())#fill the file with Model that we write
            newCar.append(self.ui2.lineEdit_Add_Color.text())#fill the file with Color that we write
            newCar.append(self.ui2.cBox_Add_Fuel.currentText())#fill the file with Fuel that we choose
            newCar.append(validCar)#fill the file with car valid by default

            outFile = open("Cars.txt", "a")#Open the file to append the car information
            writer = csv.writer(outFile, delimiter=";", lineterminator='\n')
            writer.writerow(newCar)
            outFile.close()

            self.addNewCarWindow.close()
            self.ui.listWidget_Cars.addItem(self.ui2.lineEdit_Add_PNum.text())

            row = self.ui.listWidget_Cars.count() - 1
            item = self.ui.listWidget_Cars.item(row)
            item.setBackground(self._green)#fill the new car with valid color by default
            self.CarsUI.show()

    def openModifyCar(self):
        self.item = self.ui.listWidget_Cars.currentItem()
        if not self.item:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any Car from the list!")
            msg.exec()
        else:
            self.modifyCarWindow = QtWidgets.QMainWindow()
            self.ui3 = Ui_ModifyCar()
            self.ui3.setupUi(self.modifyCarWindow)
            self.ui3.lineEdit_Modify_PNum.setWindowFilePath(self.addText())
            self.ui3.lineEdit_Modify_Make.setWindowFilePath(self.addText())
            self.ui3.lineEdit_Modify_Model.setWindowFilePath(self.addText())
            self.ui3.lineEdit_Modify_Color.setWindowFilePath(self.addText())
            self.ui3.cBox_Modify_Fuel.setWindowFilePath(self.addText())
            self.ui3.pushBtn_Modify.clicked.connect(self.modifyCar)
            self.modifyCarWindow.show()

    def modifyCar(self):
        #Verify if the user is entering the complete car information(MOD)
        if self.ui3.lineEdit_Modify_PNum.text() == '' or\
           self.ui3.lineEdit_Modify_Make.text() == '' or\
           self.ui3.lineEdit_Modify_Model.text() == '' or\
           self.ui3.lineEdit_Modify_Color.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should enter the complete car information!")
            msg.exec()
        else:
            self.row = self.ui.listWidget_Cars.currentRow()
            self.item = self.ui.listWidget_Cars.item(self.row)
            item = self.ui.listWidget_Cars.takeItem(self.row)

            f = open("Cars.txt", "r")
            tmpCars = list(csv.reader(f, delimiter=";"))
            newAdd = []
            newAdd.append(self.ui3.lineEdit_Modify_PNum.text())
            newAdd.append(self.ui3.lineEdit_Modify_Make.text())
            newAdd.append(self.ui3.lineEdit_Modify_Model.text())
            newAdd.append(self.ui3.lineEdit_Modify_Color.text())
            newAdd.append(self.ui3.cBox_Modify_Fuel.currentText())

            f = open("Cars.txt", "w")
            writer = csv.writer(f, delimiter=";", lineterminator='\n')
            for line in tmpCars:
                if line[0] != item.text():
                    writer.writerow(line)
                else:
                    newAdd.append(line[5])
                    writer.writerow(newAdd)
            f.close()

            self.modifyCarWindow.close()
            self.CarsUI.show()
            self.ui.listWidget_Cars.clear()#Clear the list widget
            self.ui.listWidget_Cars.setWindowFilePath(self.addFile())#fill the list widget with modified file

    def addText(self):
        a = Car()
        num_lines = sum(1 for line in open('Cars.txt'))#Give the exact number of lines in file
        for x in range(num_lines):
            #Verify the plate that we selected and fill the text edit with its information
            if self.item.text() == a.getPlate(x):
                self.ui3.lineEdit_Modify_PNum.setText(a.getPlate(x))
                self.ui3.lineEdit_Modify_Make.setText(a.getMake(x))
                self.ui3.lineEdit_Modify_Model.setText(a.getModel(x))
                self.ui3.lineEdit_Modify_Color.setText(a.getColor(x))
                self.ui3.cBox_Modify_Fuel.setCurrentText(a.getFuel(x))

    def addFile(self):
        f = open("Cars.txt", "r")
        tmpCars = list(csv.reader(f, delimiter=";"))
        self.b = 0
        for line in tmpCars:
            self.ui.listWidget_Cars.addItem(line[0])
            item = self.ui.listWidget_Cars.item(self.b)
            self.b += 1
            if line[5] == "v":
                item.setBackground(self._green)
            else:
                item.setBackground(self._red)
        f.close()

    def deleteCar(self):
        row = self.ui.listWidget_Cars.currentRow()
        item = self.ui.listWidget_Cars.item(row)
        if item is None:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any Car from the list!")
            msg.exec()
        else:
            item = self.ui.listWidget_Cars.takeItem(row)

            f = open("Cars.txt", "r")
            tmpCars = list(csv.reader(f, delimiter=";"))

            f = open("Cars.txt", "w")
            writer = csv.writer(f, delimiter=";", lineterminator='\n')
            #the selected line will not be written
            for line in tmpCars:
                #verify if the plate wasn't selected
                if line[0] != item.text():
                    writer.writerow(line)
            f.close()
            del item

    def Validate(self):
        row = self.ui.listWidget_Cars.currentRow()
        item = self.ui.listWidget_Cars.item(row)
        if item is None:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any Car from the list!")
            msg.exec()
        else:
            color = item.background()
            #modify item color background
            item.setBackground(self._red if color == self._green else self._green)
            f = open("Cars.txt", "r")
            tmpCars = list(csv.reader(f, delimiter=";"))
            f = open("Cars.txt", "w")
            writer = csv.writer(f, delimiter=";", lineterminator='\n')
            #If the car is valid, the v in the file will chance to i and vice versa
            for line in tmpCars:
                if line[0] == item.text():
                    if color == self._green:
                        line[5] = "i"
                    else:
                        line[5] = "v"
                writer.writerow(line)
            f.close()
            item.setSelected(False)

# MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())