import matplotlib.pyplot as plt

x_values=[x for x in range(1,5001)]
y_values=[y**3 for y in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Oranges,edgecolors="none")
plt.title("1-5000立方计算",fontsize=20)
plt.axis()
plt.show()