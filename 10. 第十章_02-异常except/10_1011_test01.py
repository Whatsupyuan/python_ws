import json
def saveJsonFile():
    try:
        number = int(input("Please input your favorite number .."))
    except ValueError:
        print("error input nubmer")
    else:
        # 保存json到文件中
        savaJson(number)

def savaJson(number):
    try:
        with open("jsonFile.json" , "w") as file:
           json.dump(number , file)
    except:
        pass

def printNumber():
    with open("jsonFile.json") as file:
        content =json.load(file)
    print("I know your favorite number! It's " + str(content))

# 方法调用
saveJsonFile()
printNumber()