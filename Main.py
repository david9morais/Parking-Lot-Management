import csv

class Car:
    def __init__(self):
        self.__plate = []
        self.__make = []
        self.__model = []
        self.__color = []
        self.__fuel = []
        self.__cars = []
        self.inputCars()

    def getPlate(self, i):
        return self.__plate[i]

    def getMake(self, i):
        return self.__make[i]

    def getModel(self, i):
        return self.__model[i]

    def getColor(self, i):
        return self.__color[i]

    def getFuel(self, i):
        return self.__fuel[i]

    def inputCars(self):
        file = open('Cars.txt', 'r')
        for line in file:
            tmp = line.split(';')
            self.__plate.append(tmp[0])
            self.__make.append(tmp[1])
            self.__model.append(tmp[2])
            self.__color.append(tmp[3])
            self.__fuel.append(tmp[4])
            self.__cars.append(tmp[0] + ";" + tmp[1] + ";" + tmp[2] + ";" + tmp[3] + ";" + tmp[4] + ";")

        file.close()
        return self.__cars

#MAIN
a = Car()