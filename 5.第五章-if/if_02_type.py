cars = ["benz", "bmw", "toyota"]
print("honda" in cars)
# 区分大小写
print("benz" in cars)

if "honda" in cars and "benz" in cars:
    print(1)
else:
    print(2)

# or
if "honda" in cars or "benz" in cars:
    print(1)
else:
    print(2)

# age judge
age = 12
print(age == 32)
print(age == 12)

# list - in
print("bmw" in cars)

# list - not in
print("bmw" not in cars)