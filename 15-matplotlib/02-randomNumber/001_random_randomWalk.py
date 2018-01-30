from class_model.randomWalk import RandomWalk
from matplotlib import pyplot as plt

rw = RandomWalk()
rw.fill_walk()
print(len(rw.xvalues))
plt.scatter(rw.xvalues, rw.yvalues, c=rw.yvalues, cmap=plt.cm.Blues, edgecolors='none', s=15)
plt.show()
