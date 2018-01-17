from unittest import TestCase
from city_functions import createCity

class TestCreateCity(TestCase):
    def test_createCity(self):
        name = createCity("los","american")
        self.assertEqual(name , "Los,American")

    def test_createCity_population(self):
        name = createCity("los","american","5k")
        self.assertEqual(name, "Los,American- Population 5K")


testClass = TestCreateCity()
testClass.test_createCity()
testClass.test_createCity_population()
