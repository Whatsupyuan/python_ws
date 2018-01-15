# 读取不同目录下文件内容
#with open("/Users/hryuan911/develop/1.txt") as fileTxt:
# 本地文件夹下
with open("1.txt") as fileTxt:
    read = fileTxt.read()
    print(read.rstrip())