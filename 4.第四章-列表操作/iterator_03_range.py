# range
# 包前不包后,类似于 String.substring(int startIndex , int endIndex) ;
# range(开始数字,结束数字,步长<step>)
for num in range(1,6):
    print(num)

# 使用range创建数字列表
numList = list(range(1,11));
for num in numList:
    print(num)

print()
numList = list(range(1,20,2));
for num in numList:
    print(num)

# 平方计算
print()
numList = []
for num in range(1,11):
    numList.append(num**2);
print(numList)

# 数字计算函数
print("list中最小数：" + str(min(numList)))
print("list中最大数：" + str(max(numList)))
print("list总和：" + str(sum(numList)))
