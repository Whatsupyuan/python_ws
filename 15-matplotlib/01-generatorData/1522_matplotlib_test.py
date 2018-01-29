import matplotlib.pyplot as pf

'''
15 绘制简单图表
'''
input_val = []
square = []
for num in range(1, 50):
    input_val.append(num)
    square.append(num * num)
pf.plot(input_val, square, linewidth=5)
pf.title("square平方", fontsize=23)
pf.xlabel("x-label", fontsize=10)
pf.ylabel("y-label", fontsize=10)
pf.tick_params(axis="both")
pf.show()
