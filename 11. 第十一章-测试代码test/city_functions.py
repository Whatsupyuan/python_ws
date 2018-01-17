def createCity(cityName , country , population=''):
    if population:
        return str(cityName + "," + country + "- population " + population).title()
    else:
        return str(cityName + "," + country).title()
