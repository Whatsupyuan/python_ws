# 9-10
from class_model.restrurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self , name , type , flavors):
        super().__init__(name , type)
        self.flavors = flavors
    def showFlavors(self):
        print("餐厅名称:" + self.name)
        print("餐厅类型:" + self.type)
        for flavor in self.flavors:
            print(flavor)
restaurant = IceCreamStand("冰激凌餐厅" , "甜品" , ["巧克力","草莓","香草"])
restaurant.showFlavors()
