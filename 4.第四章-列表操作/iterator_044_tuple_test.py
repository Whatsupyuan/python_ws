# tuple 用 () 声明，不可修改其中的元素，但可以重新赋值指向新的 tuple
# 4-13
foodTuple = ('rice', 'pipe', 'beef', 'beer', 'pickle', 123)
for food in foodTuple:
    print(food)

print()

# 下一行会报错,tuple不允许修改
# foodTuple[2] = "123" ;
foodTuple = ('大米', '派', "noodle")
for food in foodTuple:
    print(food)
