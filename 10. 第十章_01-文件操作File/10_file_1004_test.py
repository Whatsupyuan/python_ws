with open("learning_python.txt") as file:
    content = file.read()
    print(content)

with open("learning_python.txt") as file:
    content = file.readlines()

print()
for l in content:
    print(l.rstrip())

print()
for l in content :
    # 字符串替换操作
    lContent = l.replace("Python" , "JAVA")
    print(lContent.rstrip())