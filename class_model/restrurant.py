class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name + " " + self.type)

    def pen_restaurant(self):
        print(self.name + " is opening!")