'''函数声明
    info="Russia" 为默认赋值
'''
def printInfo(username,info="Russia"):
    print("Hello ," + username)
    print("Info , " + info)
    print()

# 函数调用时 , 使用参数名进行绑定
printInfo(username="Kobe",info="los angles")
printInfo(info="clc",username="James")
printInfo(username="yuan")
printInfo(username="yuan" , info="bj")