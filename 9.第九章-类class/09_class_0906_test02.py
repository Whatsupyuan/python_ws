# 9-7
class User():
    def __init__(self , first_name , last_name , address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def describe_user(self):
        print("first name : " + self.first_name +"," + "last name : "+self.last_name + ", address : " + self.address)

    def great_user(self):
        print("Hello , " + str(self.first_name + " " + self.last_name).title())

class Admin(User):
    def __init__(self , first_name , last_name , address):
            super().__init__(first_name , last_name , address)
            self.privileges = ["can add post" , "can delete post" ,"can ban user"]
    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print("特殊权限 : " + privilege)

user = Admin("hr" , "y" , "BJ")
user.show_privileges()
