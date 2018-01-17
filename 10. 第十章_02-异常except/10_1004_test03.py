# 读取文件
def readFile(fileName):
    if fileName:
        try:
            with open(fileName,"r") as file:
                content = file.read()
        except FileNotFoundError:
            pass
        else:
            return content

# 调用
filename = "names1.txt"
content = readFile(filename)
if content:
    print(content.rstrip())