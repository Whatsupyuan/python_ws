# 5-8
names = ["James","Kobe","Yuan","Irving","admin"]
for name in names:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello Eric, thank you for logging in again")

# 5-9
names = []
if names:
    print("列表非空")
else:
    print("We need to find some users")

# 5-10
print()
names = ["James","Kobe","Yuan","Irving","admin"]
new_users = ["testUser02","testUser03","Yuan","Irving","testUser01"]
for nu in new_users:
    if nu in names:
        print(nu + ",用户名已经重复")

# 5-11
print()
num_arr = list(range(1,10))
for num in num_arr:
    if num == 1:
        print(str(num) +"st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")