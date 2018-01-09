# 6-7
personArr = []
person = {"name": "yuan", "age": 27, "address": "Beijing"}
person1 = {"name": "Kobe", "age": 30, "address": "los"}
person2 = {"name": "James", "age": 40, "address": "clc"}
personArr.append(person)
personArr.append(person1)
personArr.append(person2)

for p in personArr:
    print(p)
    print(p["name"])
    print(p["age"])
    print(p["address"])
    for k,v in p.items():
        print(str(k) + " : " + str(v))
print()

# 6-8
dog = {"name":"dog" , "age" : "1" , "masterName" : "kobe"}
cat = {"name":"cat" , "age" : "2" , "masterName" : "Jame"}
snack = {"name":"snack" , "age" : "3" , "masterName" : "Irving"}
pets = []
pets.append(dog)
pets.append(cat)
pets.append(snack)
for pet in  pets:
    print(pet)
    for k , v in dog.items():
        print(k + " : " + v)

# 6-9 字典嵌套list
print("-----")
favorite_places = {"Kobe":["los angeles","germary"] , "James" : ["NYC","Canada"], "Irving":["Russia","Japan"]}
for name , place in favorite_places.items():
    print(name)
    for p in place:
        print(p)
    print("-----")

# 6-10
print("-----")
favorite_number = {"Kobe" : [1,2,3],"James":[23,24],"Irving":[88,99]}
for name,fnum in favorite_number.items():
    print(name)
    for num in fnum:
        print(num)
    print("-----")

# 6-11
cityArr = {"NYC":{"county" : "American" , "population" : "4k" , "fact" : "Good"},
        "BeiJing":{"county" : "China" , "population" : "44k" , "fact" : "ss"},
        "DC":{"county" : "American" , "population" : "5k" , "fact" : "aa"}}
for cityName,info in cityArr.items():
    print(cityName)
    for key,val in info.items():
        print(key + " " + val)


