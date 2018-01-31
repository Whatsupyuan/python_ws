from class_model.randomWalk import RandomWalk
from matplotlib import pyplot as plt

'''
持续生成随机数据漫步图
'''
rw = RandomWalk(num_points=5000)
rw.fill_walk()
plt.plot(rw.xvalues, rw.yvalues)

# 设置起点的颜色为 Red ， s 设置点大小
# plt.plot(0,0,c='red',s=50)
# 设置最后一步的点是 Green
# plt.plot(rw.xvalues[-1],rw.yvalues[-1],c='green',s=50)
# invisible axes
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.show()