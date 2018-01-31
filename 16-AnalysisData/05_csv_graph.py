import csv
import matplotlib.pyplot as plt

filename="sitka_weather_07-2014.csv"
with open(filename) as file:
    content = csv.reader(file)
    # first Row
    header_row = next(content)

    hight = []
    for row in content:
        # parse int type
        hight.append(int(row[1]))

plt.plot(hight)
plt.show()