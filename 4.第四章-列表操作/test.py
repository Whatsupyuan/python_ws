# 4-3
# for num in range(1,20):
#     print(num)

def iteratorMethod(list):
    for val in list:
        print(val)


numArr = list(range(1, 1000 * 1000 + 1))
# iteratorMethod(numArr)

# print(min(numArr))
# print(max(numArr))
# print(sum(numArr))

# numArr = list(range(1,20,2))
# iteratorMethod(numArr)

# numArr = list(range(3, 31, 3))
# iteratorMethod(numArr)

# arr = []
# for num in range(1,11):
#     arr.append(num**3)
# iteratorMethod(arr)

# arrNum = [num**3 for num in range(1,11)]
# iteratorMethod(arrNum)

# orderedDict 保存插入字典中的顺序
from collections import OrderedDict
dict = OrderedDict()
dict["h3"] = "hello3"
dict["h1"] = "hello1"
dict["h2"] = "hello2"

for k, v in dict.items():
    print(k + " " + v)