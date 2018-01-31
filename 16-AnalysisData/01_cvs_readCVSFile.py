import csv
filename="sitka_weather_07-2014.csv"
with open(filename) as file:
    content = csv.reader(file)
    # 读取csv文件头信息
    head_now = next(content)
    print(head_now)