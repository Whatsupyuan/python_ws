'''
计算器,输入 1+2 , 1 +2 , 1+ 2
进行计算
'''
val = input("Input value?")
try:
    if val:
        print(eval(val))
    else:
        print("Error : no input value")
        # 手动抛出异常
        raise ValueError("输入值不能为空")
except NameError:
    print("Error : error input")
except IndexError:
    print("Error : input error")
# 捕获任意的异常信息,并打印
except:
    import sys
    tuple = sys.exc_info()
    for val in tuple:
        print(val)