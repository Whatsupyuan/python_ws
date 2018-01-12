# 9-1
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name + " " + self.type)

    def pen_restaurant(self):
        print(self.name + " is opening!")

restaurant = Restaurant("qq" , "川菜")
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.pen_restaurant()

# 9-2
restaurant2 = Restaurant("ww","鲁菜")
restaurant3 = Restaurant("ee","粤菜")
restaurant2.pen_restaurant()
restaurant3.pen_restaurant()

# 9-3
class User():
    def __init__(self , first_name , last_name , address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def describe_user(self):
        print("first name : " + self.first_name +"," + "last name : "+self.last_name + ", address : " + self.address)

    def great_user(self):
        print("Hello , " + str(self.first_name + " " + self.last_name).title())

u1 = User("hr" , "yuan" , "BJ")
u1.great_user()