def countWord(fileName):
    if fileName:
        try:
            with open(fileName) as file:
                content = file.readlines()
        # except 之后要捕获的异常可以不写
        # 程序一样会执行
        except FileNotFoundError:
            print("文件不存在")
        else:
            wordsCount = 0
            for line in content:
                wordsCount += len(line.split())
            return wordsCount

num = countWord("10_1001_exception.py")
if num:
    print(num)