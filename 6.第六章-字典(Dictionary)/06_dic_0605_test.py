# 6-4
person = {"name": "yuan", "age": 27, "address": "Beijing"}
for field,val in person.items():
    print(field + " " + str(val))

print()

favorite_num_dic = {"Kobe": 24, "Jame": 23, "Irving": 11}
for name , age in favorite_num_dic.items():
    print(name + " " + str(age))

print()
# 6-5
riverDic = {'nile': 'egypt' , "yellowRevice" : "china" , "amazonRiver" : "Brazil"}
for rName,country in riverDic.items():
    print("The\t" + rName +  " runs throngh " + country)
print()
for river in riverDic.keys():
    print(river)
print()
for country in riverDic.values():
    print(country)

# 6-6
favorite_num_dic = {"Kobe": 24, "Jame": 23, "Irving": 11}
notInclud = ["hryuan" , "yuan911"]
includList = ["Kobe" , "Jame"]
for userName in set(favorite_num_dic.keys()):
    if userName in notInclud:
        print(userName + " ," + "请参与调查")
    elif userName not in notInclud and userName in includList:
        print(userName + ",已经完成调查,谢谢")
    else:
        print("未知人员,"+userName)

print()

# set 去重复
# 去重复展示value中的值
arr = ["kobe","kobe","kobe"]
for val in set(arr):
    print(val)
print()
for val in set(favorite_num_dic.values()):
    print(val)
