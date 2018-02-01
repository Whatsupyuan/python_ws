import csv
import matplotlib.pyplot as plt
from datetime import datetime
'''
绘制两条线，最低温度和最高温度
'''
# throw ValueError
filename="death_valley_2014.csv"
with open(filename) as file:
    content = csv.reader(file)
    # first Row
    header_row = next(content)
    dates , hight , low = [],[],[]
    for row in content:
        # catch exception
        try:
            # parse int type
            date = datetime.strptime(row[0], "%Y-%m-%d")
            hight_val = int(row[1])
            low_val = int(row[3])
        except ValueError:
            print("error data" + row[0] + row[1] + row[3])
            continue
        else:
            dates.append(date)
            hight.append(hight_val)
            low.append(low_val)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,hight,color='red')
plt.plot(dates,low , color="blue")
# 倾斜 xlable 的内容,避免重叠
fig.autofmt_xdate()
plt.xlabel('',fontsize=10)
# 设置两条中间值内容填充
plt.fill_between(dates, hight, low, facecolor="blue", alpha=0.1)
plt.show()


# %Y-%m-%d %H:%M:%S
frist_date = datetime.strptime("2018-01-01 14:12:36" , "%Y-%m-%d %H:%M:%S")
print(frist_date)