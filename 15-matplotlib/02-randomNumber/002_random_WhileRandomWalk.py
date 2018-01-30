from class_model.randomWalk import RandomWalk
from matplotlib import pyplot as plt

'''
持续生成随机数据漫步图
'''
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.xvalues, rw.yvalues, c=rw.yvalues, cmap=plt.cm.Oranges, edgecolors='none', s=30)

# 设置起点的颜色为 Red
plt.scatter(0,0,c='red',s=100)
# 设置最后一步的点是 Green
plt.scatter(rw.xvalues[-1],rw.yvalues[-1],c='green',s=100)

plt.show()