from class_model.randomWalk import RandomWalk
from matplotlib import pyplot as plt
'''
持续生成随机数据漫步图
'''
while True:
    rw = RandomWalk()
    rw.fill_walk()
    print(len(rw.xvalues))
    plt.scatter(rw.xvalues, rw.yvalues, c=rw.yvalues, cmap=plt.cm.Blues, edgecolors='none', s=30)
    plt.show()

    text = input("Make anthor walk ? y/n")
    if text == 'n':
        break
