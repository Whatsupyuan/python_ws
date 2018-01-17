def plus():
    try:
        num1 = int(input("Please input first number.."))
        num2 = int(input("Please input second number.."))
    # python 3.6 捕获多个异常，不能使用 ， 号分隔
    except TypeError:
        print("error.")
    except ValueError:
        print("valueError")
    else:
        return num1 + num2

print(plus())