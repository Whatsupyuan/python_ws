from class_model.privileges import Privileges

class User():
    def __init__(self , first_name , last_name , address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def describe_user(self):
        print("first name : " + self.first_name +"," + "last name : "+self.last_name + ", address : " + self.address)

    def great_user(self):
        print("Hello , " + str(self.first_name + " " + self.last_name).title())

# user 的子类
class Admin(User):
    def __init__(self , first_name , last_name , address):
            super().__init__(first_name , last_name , address)
            # 引用 , 空的构造方法
            self.privileges = Privileges()