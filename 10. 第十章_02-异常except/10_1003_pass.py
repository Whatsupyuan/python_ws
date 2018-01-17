def countWord(fileName):
    if fileName:
        try:
            with open(fileName) as file:
                content = file.readlines()
        # except 之后要捕获的异常可以不写
        # 程序一样会执行
        except FileNotFoundError:
            # pass 当程序出现异常时 , 什么操作都不执行
            pass
        else:
            wordsCount = 0
            for line in content:
                wordsCount += len(line.split())
            return wordsCount

# 第二种方法: 一次性读取所有文件内容
def countFileIncludWord(fileName):
    if fileName:
        try:
            with open(fileName) as file:
                content = file.read()
        except:
            pass
        else:
            return len(content.split())

num = countWord("10_1001_exception.py")
num2 = countFileIncludWord("10_1001_exception.py")
if num:
    print(num)
if num2:
    print(num2)