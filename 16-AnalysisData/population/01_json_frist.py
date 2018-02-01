import json

with open("population_data.json") as file:
    content = json.load(file)

print(content)
for jsonData in content:
    if jsonData["Year"] == '2010':
        country_city = jsonData["Country Name"]
        value = jsonData["Value"]
        print(country_city + " " + value)