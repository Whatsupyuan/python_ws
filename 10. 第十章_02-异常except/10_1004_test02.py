def plus():
    try:
        num1 = int(input("Please input first number.."))
        num2 = int(input("Please input second number.."))
    except TypeError:
        print("error.")
    except ValueError:
        print("valueError")
    else:
        return num1 + num2

flag = True
while flag:
    num = plus()
    print(num)