favorite_num_dic = {"Kobe": 24, "Jame": 23, "Irving": 11 , "Kobe" : 66}
print(favorite_num_dic)

print()
for name in set(favorite_num_dic.keys()):
    print(name)
    print(favorite_num_dic[name])

print(set(favorite_num_dic.keys()))