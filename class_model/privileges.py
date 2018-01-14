# class
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print("特殊权限 : " + privilege)
