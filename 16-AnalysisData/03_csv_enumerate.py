import csv
filename="sitka_weather_07-2014.csv"
with open(filename) as file:
    content = csv.reader(file)
        # print header's information index and content , enumerate[info] return dictionaries [index , value]
    for index , head_content in enumerate(next(content)):
        print(str(index) + " " + head_content)