# 读取不同目录下文件内容
#with open("/Users/hryuan911/develop/1.txt") as fileTxt:
# 本地文件夹下
with open("1.txt") as fileTxt:
    read = fileTxt.read()
    print(read.rstrip())

# 去除两端存在 ['s' , ‘a’ , 'y'] 前后两端中包含的字符，直到替换完为止
sayStr = "saaaay yes a no yaaaass"
print(sayStr.strip("say"))