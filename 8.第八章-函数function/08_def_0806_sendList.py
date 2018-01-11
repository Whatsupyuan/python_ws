def printVal(arr):
    if arr:
        for num in arr:
            print(num)
    else:
        print("列表为空")

# 方法调用
arr = []
# 返回列表为空
printVal(arr)
for i in range(1,21):
    arr.append(i)
printVal(arr)