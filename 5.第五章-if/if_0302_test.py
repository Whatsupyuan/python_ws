# 5-3
killed_alien = "Green"
if "green" == killed_alien.lower():
    print("green alien. Add five point")

# 5-4
if "green" == killed_alien.lower():
    print("green alien. Add five point")
else:
    print("Add Ten Point");

# 5-5
if "green" == killed_alien.lower():
    print("green alien. Add five point")
elif "yellow" == killed_alien:
    print("Add Ten Points")
elif "red" == killed_alien:
    print("Add 15 Points")

# 5-6
age = 5
if age < 2:
    print("婴儿")
elif age >= 2 and age < 4:
    print("蹒跚学步")
elif age >=4 and age < 13:
    print("儿童")
elif age >=13 and age < 20:
    print("青少年")
elif age >=20 and age < 65:
    print("成年人")
elif age > 65:
    print("老年人")

# 5-7
favorite_fruits = ["apple","banana","grape","watermelon"]
for fur in favorite_fruits:
    if fur == "grape":
        print("grape 123!")
    if fur == "apple":
        print("apple 123!")

