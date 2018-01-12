# 声明类
# 本例测试中,Dog() 之后的括号是否存在不影响程序运行
class Dog():
    # 初始化(构造)方法
    def __init__(self , name , age):
        self.name = name
        self.age = age
    # 传递self是必须的
    def setDown(self):
        print("Please set down , " + self.name)
    def up(self):
        print("Please up here , " + self.name + " " + str(self.age))

my_dog = Dog("kk" , 2)
# 访问变量
print(my_dog.name)
print(my_dog.age)
# 调用方法
my_dog.setDown()

# 如果传递构造参数,则以下代码报错
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# my_dog2 = Dog()