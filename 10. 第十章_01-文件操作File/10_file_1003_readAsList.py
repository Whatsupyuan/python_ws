# 文件读取至一个list中 - readlines
# 可以在with 代码块以外操作文件内容
fileName = "1.txt"
with open(fileName) as file:
    # 读取所有的文件内容 readLines
    line = file.readlines()

# str()
# int() , float() 数字 , 浮点数转换
str1 = ''
for l in line:
    print(l.rstrip())
    str1 += str(l.strip())
print(str1)

fileName ="圆周率.txt"
with open(fileName) as file:
    line = file.readlines()
for l in  line:
    print(len(l.strip()))


# 判断生日在不在圆周率中
content = ""
with open(fileName) as file:
    lines = file.readlines()
for l in lines :
    content += str(l)

brithday = input("Please input your brithDay?")
if brithday in content:
    print("包含")
else:
    print("不包含")



