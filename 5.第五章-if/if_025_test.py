# 5.2.1
str1 = "print info"
str2 = "print name"
print(str1 == str2)

# 5.2.2
print(str1.lower() == str2)

# 5.2.3
int1 = 100
int2 = 110
print(int1 == int2)
print(int1 != int2)
print(int1 > int2)
print(int1 < int2)
print(int1 >= int2)
print(int1 <= int2)

# 5.2.4
if int1 == int2 or int1 <= int2:
    print(1)
if int1 != int2 and int1 < int2:
    print(22)

# 5.2.5
print()
cars = ["benz", "bmw", "toyota"]
if "uia" in cars:
    print(1)
if "uia" not in cars:
    print(2)