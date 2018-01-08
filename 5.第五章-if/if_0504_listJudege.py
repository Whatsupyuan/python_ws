# if 之后可以直接判断
# 类似于 javascript 中的判断方法
cars = []
if cars:
    print("不为空")
else:
    print("空")

# 对空的 list 进行遍历时也不会报错,但没有任何的输出内容
for car in cars:
    print(car)

