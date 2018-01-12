# *号传递任意的不固定的参数
def how_magicians(*filename):
    for name in filename:
        print(name)
# 可以接收 任意类型 的形参
how_magicians("1", "2", 3, 4)