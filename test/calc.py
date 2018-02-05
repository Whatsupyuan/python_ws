'''
计算器,输入 1+2 , 1 +2 , 1+ 2
进行计算
'''
def chargeOperation(val):
    if val:
        if val.find("+") > 0:
            operate = "+"
        elif val.find("-") > 0:
            operate = "-"
        elif val.find("*") > 0:
            operate = "*"
        elif val.find("/") > 0:
            operate = "/"
        return operate
    else:
        raise NameError("Error value")

def calc():
    val = input("Input value?")
    try:
        if val:
            operate = chargeOperation(val)
            valArr = val.strip().split(operate)
            val_1 = int(valArr[0])
            val_2 = int(valArr[1])
        else:
            print("Error : no input value")
            # 手动抛出异常
            raise ValueError("输入值不能为空")
    # 捕获任意的异常信息,并打印
    except:
        import sys
        tuple = sys.exc_info()
        traceback = sys.exc_traceback()
        for val in tuple:
            print(val)
        for val in traceback:
            print(val)
    else:
        if operate == "+":
            print(val_1 + val_2)
        elif operate == "-":
            print(val_1 - val_2)
        elif operate == "*":
            print(val_1 * val_2)
        elif operate == "/":
            print(val_1 / val_2)

while True:
    calc()