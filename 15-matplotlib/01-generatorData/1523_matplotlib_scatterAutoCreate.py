import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# RGB设置颜色
# plt.scatter(x_values , y_values , c=(0.8, 0, 0), edgecolor='none' ,s=40)
# 颜色名称设置 orange
plt.scatter(x_values , y_values , c='orange' , edgecolor='blue' ,s=40)
plt.title("散点图Scatter",fontsize=20)
plt.xlabel("基数",fontsize=20)
plt.ylabel("乘积" , fontsize=20)

plt.axis([0, 1000, 0 , 11000])
plt.show()