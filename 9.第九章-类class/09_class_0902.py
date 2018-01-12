class Cat():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # info 可以通过实例化进行访问
        self.info = name + " " + color
    # 方法重载有问题
    def eat(self):
        print("cat " + self.name + " is eat something")
    def eat(self,food):
        print("cat " + self.name + " is eat " + food , "this cat is " + self.info)


my_cat = Cat("cc", "Black")
my_cat.eat("fish")
print(my_cat.info)