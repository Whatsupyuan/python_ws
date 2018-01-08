# 字段 Dictionary
dic = {"name":"alien","age":27,"color":"blue"}
print(dic["name"]);
print(dic["age"]);
print(dic["color"]);
print(dic)

# 修改 key-value
dic["age"] = 29
print(dic)

# 添加 key-value
dic["x-position"] = 25
dic["y-positon"] = 30
print(dic)

# 空字典操作
dic={}
dic["name"]="hryuan911"
dic["address"]="BeiJing"
dic["age"]=27
print(str(dic["age"]))
print(dic)

# 删除 del key-value
del dic["name"]
print(dic)
# 删除 删除一个不存在的 key 时会报错
# 报错信息 : KeyError: 'name'
# del dic["name"]
# print(dic)

# 区分大小写
dic["Name"] = "ithome"
dic["name"] = "ithome"
print(dic)


