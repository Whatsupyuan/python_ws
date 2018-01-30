import matplotlib.pyplot as pf

rangeList = range(1,11)
print("rangList 类型: " + str(type(rangeList)))
xList = [x for x in range(10)]
yList = [y*y for y in range(10)]

print("xList 类型: " + str(type(xList)))
# xList = [1, 2, 3, 4, 5]
# yList = [1, 4, 9, 16, 25]

pf.scatter(xList , yList , s=100)
pf.show()