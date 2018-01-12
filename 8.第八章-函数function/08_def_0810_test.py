# 8-12
def makeSandwich(*raws):
    for raw in raws:
        print(raw)
makeSandwich("meat","Lettuce", "bread")

'''
meat
Lettuce
bread
'''
print()

# 8-13
def build_profile(firstName , lastName , **personInfo):
    dic={}
    dic["firstName"] = firstName
    dic["lastName"] = lastName
    for key,val in personInfo.items():
        dic[key] = val
    return dic

dic = build_profile("hr", "y" , address="bj" , age="27" , sex="male")
print(dic)

'''
{'firstName': 'hr', 'lastName': 'y', 'address': 'bj', 'age': '27', 'sex': 'male'}
'''
print()


# 8-14
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
def make_car(brand , serie , **carInfo):
    dic={}
    dic[brand] = serie
    for key , val in carInfo.items():
        dic[key] = val
    return dic
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

'''
{'subaru': 'outback', 'color': 'blue', 'tow_package': True}
'''

