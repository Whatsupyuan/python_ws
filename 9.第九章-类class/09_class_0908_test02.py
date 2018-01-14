# 9-10
from class_model.user import Admin

user = Admin("hr" , "yuan" , "bj")
user.great_user()
# 类中多级引用调用
user.privileges.show_privileges()