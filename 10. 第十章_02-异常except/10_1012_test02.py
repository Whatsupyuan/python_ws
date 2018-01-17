# 与 10-13 类似
import json
def saveJsonFile():
    try:
        number = int(input("Please input your favorite number .."))
    except ValueError:
        print("error input nubmer")
    else:
        # 保存json到文件中
        saveJson(number)

def saveJson(number):
    try:
        with open("jsonFile.json" , "w") as file:
           json.dump(number , file)
    except:
        pass

def printNumber():
    try:
        with open("jsonFile.json") as file:
            content =json.load(file)
    except FileNotFoundError:
        print("you don't have any number")
        saveJsonFile()
        printNumber()
    else:
        print("I know your favorite number! It's " + str(content))

# 方法调用
printNumber()