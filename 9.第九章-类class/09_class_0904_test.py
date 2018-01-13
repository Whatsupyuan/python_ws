# 9-4
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + " " + self.type)

    def pen_restaurant(self):
        print(self.name + " is opening!")

    # 设置就餐人数
    def set_number_served(self , personNum):
        self.number_served = personNum

    def increment_number_served(self , personNum):
        self.number_served += personNum

    # 打印当前就餐人数
    def printCurrentPerson(self):
        print("当前就餐人数:" + str(self.number_served))

rest = Restaurant("aa" , "川菜")
rest.set_number_served(1)
rest.increment_number_served(10)
rest.printCurrentPerson()

# 9-5
class User():
    def __init__(self , first_name , last_name , address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.login_attempts = 0

    def describe_user(self):
        print("first name : " + self.first_name +"," + "last name : "+self.last_name + ", address : " + self.address)

    def great_user(self):
        print("Hello , " + str(self.first_name + " " + self.last_name).title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("hr" , "y" , "BJ")
for n in range(1,11):
    user.increment_login_attempts()
# 登陆记录
print(user.login_attempts)
# 重置登陆次数
user.reset_login_attempts()
# 打印重置后的登陆次数
print(user.login_attempts)


