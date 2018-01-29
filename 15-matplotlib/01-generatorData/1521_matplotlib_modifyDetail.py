import matplotlib.pyplot as pf

'''
15 绘制简单图表
'''
input_val = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
pf.plot(input_val, square, linewidth=5)
pf.title("square平方", fontsize=23)
pf.xlabel("x-label", fontsize=10)
pf.ylabel("y-label", fontsize=10)
pf.tick_params(axis="both", labelsize=14)
pf.show()
