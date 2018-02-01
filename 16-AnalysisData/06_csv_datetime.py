import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename="sitka_weather_2014.csv"
with open(filename) as file:
    content = csv.reader(file)
    # first Row
    header_row = next(content)

    dates , hight = [],[]
    for row in content:
        # parse int type
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)
        hight.append(int(row[1]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,hight,color='red')
# 倾斜 xlable 的内容,避免重叠
fig.autofmt_xdate()
plt.xlabel('',fontsize=10)
plt.show()


# %Y-%m-%d %H:%M:%S
frist_date = datetime.strptime("2018-01-01 14:12:36" , "%Y-%m-%d %H:%M:%S")
print(frist_date)