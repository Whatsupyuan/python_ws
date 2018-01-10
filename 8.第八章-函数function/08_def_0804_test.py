# 8-3
def make_shirt(size , logo):
    print("T shirt size is " + size + ", and Logo is " + logo)

# 8-4
def make_shirt_two(size , logo="I love Python"):
    print("T shirt size is " + size + ", and Logo is " + logo)

make_shirt_two(str(32))
make_shirt_two(size=str(32))

# 如果调用函数时 , 如果有一个参数为绑定参数的方式调用,则之后的也必须为绑定参数
# 下一行被注释代码报错
# make_shirt_two(size=str(27) , "nike")

# 8-5
make_shirt_two(size=str(27) , logo="nike")
make_shirt_two(str(28) , "adidas")