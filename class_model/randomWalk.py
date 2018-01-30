from random import choice
'''
生成随机数class
'''
class RandomWalk():
    def __init__(self, num_points=5000 , ntet=0):
        self.num_points = num_points
        self.xvalues = [0]
        self.yvalues = [0]

    def fill_walk(self):
        while len(self.xvalues) < self.num_points:
            # list 中随机选择一个数 -1与1中进行随机选择
            x_distinction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_distinction

            y_distinction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_distinction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            x_step = self.xvalues[-1] + x_step
            y_step = self.yvalues[-1] + y_step

            self.xvalues.append(x_step)
            self.yvalues.append(y_step)