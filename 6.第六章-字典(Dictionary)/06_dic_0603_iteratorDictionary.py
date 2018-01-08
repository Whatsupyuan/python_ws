favorite_num_dic = {"Kobe": 24, "Jame": 23, "Irving": 11}
# 自创方法,类似于Map遍历的方法
for num in favorite_num_dic:
    print(num + " " + str(favorite_num_dic[num]))

# 高级遍历方法 items() 方法
print(favorite_num_dic.items())
for name,number in favorite_num_dic.items():
    print(name + " " + str(number))

