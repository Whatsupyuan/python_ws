favorite_num_dic = {"Kobe": 24, "Jame": 23, "Irving": 11}
# 自创方法,类似于Map遍历的方法
for num in favorite_num_dic:
    print(num + " " + str(favorite_num_dic[num]))

print()
# 高级遍历方法 items() 方法
print(favorite_num_dic.items())
for name,number in favorite_num_dic.items():
    print(name + " " + str(number))

print()
# key获取 字典 中的所有key --- keys()
# 如果将上述代码中的for name in favorite_languages.keys(): 替换为for name in favorite_languages: ，输出将不变。
for key in favorite_num_dic.keys():
    print(key)

print()
# 字典获取所有的 value --- values()
# 类似于 Map.keys() 与 Map.values()
vals = favorite_num_dic.values()
for val in vals:
    print(val)


