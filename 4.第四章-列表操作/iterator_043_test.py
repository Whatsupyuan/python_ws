# 4.3
arr = list(range(1,20+1))
for num in arr:
    print(num)

# 4.4
arr = list(range(1,100**3+1))
# for num in arr:
#     print(num)

print()
# 4.5
print("最小值" + str(min(arr)))
print("最大值" + str(max(arr)))
print("总和" + str(sum(arr)))

# 4.6 1-20奇数 , 并打印
for num in range(1 , 20+1 , 2):
    print(num)

print()

# 4.7 3~30 3的倍数
for num in range(3,30+1,3):
    print(num)

# 4.8 1-10 整数立方列表打印
arr = []
for num in range(1,11):
    arr.append(num**3)
print(arr)

# 4.9 1-10 整数立方列表打印(列表解析)
arr = [num**3 for num in range(1,11)]
print(arr)





