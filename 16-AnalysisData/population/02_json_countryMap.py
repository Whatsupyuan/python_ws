import json
from pygal.maps.world import COUNTRIES

with open("population_data.json") as file:
    content = json.load(file)

# parse COUNTRIES to dictionary
def parse_countries_dic():
    dic_country = {}
    for country_code in sorted(COUNTRIES.keys()):
        dic_country[COUNTRIES[country_code].lower()] = country_code
    return dic_country

def get_country_code(dic_country , country_name):
    return dic_country[country_name.lower()]

#
# for jsonData in content:
#     if jsonData["Year"] == '2010':
#         country_city = jsonData["Country Name"]
#         value = int(float(jsonData["Value"]))

# main
dic_country = parse_countries_dic()


