from collections import OrderedDict

class Test():

    def __init__(self):
        self.favorite_languages = OrderedDict()
        self.favorite_languages["Kobe"] = "Italy"
        self.favorite_languages["Yuan"] = "Chinese"
        self.favorite_languages["Irving"] = "English"
        for key, val in self.favorite_languages.items():
            print(key + " " + val)


t = Test()
