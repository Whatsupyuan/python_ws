'''
父类 , 子类
继承
'''
class Car():
    def __init__(self , name , series):
        self.name = name
        self.series = series

    def carInfo(self):
        print(self.name + " " + self.series)


class ElectriCar(Car):
    def __init__(self , name , series ):
        # super() 必须写成方法体形态 , 与JAVA不同
        super().__init__(name , series)

    def printElectriCarInfo(self):
        print(self.name + " " + self.series + "Electri")

car = Car("toyota" , "霸道")
car.carInfo()

carElec = ElectriCar("特斯拉" , "P80")
carElec.printElectriCarInfo()


# 输出
# toyota 霸道
# 特斯拉 P80Electri