import csv
filename="sitka_weather_07-2014.csv"
with open(filename) as file:
    content = csv.reader(file)
    for line in content:
        print(line)