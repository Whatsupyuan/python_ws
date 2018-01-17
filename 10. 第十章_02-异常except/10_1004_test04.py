# 统计一份文件中出现的关键字次数
# 读取文件
def readFile(fileName):
    if fileName:
        try:
            with open(fileName,"r") as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found")
        else:
            return content

# 调用
fileContent = readFile("Plague of Pythons by Frederik Pohl.txt")
countNum = fileContent.lower().count("the")
if countNum:
    print(countNum)