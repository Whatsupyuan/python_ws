# datetime.datetime.now()
# type() 查看类型
from datetime import datetime

startTime = datetime.now()
list1 = range(11)
print(type(list1))
list2 = [x for x in range(1,9900000+1)]
for num in list2:
    print(num)
# 运行时间 0:00:31.067810
print(datetime.now() - startTime)