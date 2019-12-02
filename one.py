import unittest
from math import floor


class MassCalculator:

    @staticmethod
    def get_requirements_from_file():
        file = open('inputs/one.txt')
        print(MassCalculator.calculate_total_fuel_requirements(file.readlines()))

    @staticmethod
    def calculate_total_fuel_requirements(mass_inputs):
        return sum([MassCalculator.calculate_fuel(int(x)) for x in mass_inputs])

    @staticmethod
    def calculate_fuel(mass):
        return floor(mass / 3) - 2


class TestOne(unittest.TestCase):

    def test_calculate_12(self):
        fuel = MassCalculator.calculate_fuel(12)
        self.assertEqual(fuel, 2)

    def test_calculate_14(self):
        fuel = MassCalculator.calculate_fuel(14)
        self.assertEqual(fuel, 2)

    def test_calculate_1969(self):
        fuel = MassCalculator.calculate_fuel(1969)
        self.assertEqual(fuel, 654)

    def test_calculate_100756(self):
        fuel = MassCalculator.calculate_fuel(100756)
        self.assertEqual(fuel, 33583)

    def test_calculate_total_fuel(self):
        fuel = MassCalculator.calculate_total_fuel_requirements(['12'])
        self.assertEqual(fuel, 2)

    def test_calculate_total_fuel_2(self):
        fuel = MassCalculator.calculate_total_fuel_requirements(['12', '12'])
        self.assertEqual(fuel, 4)


if __name__ == '__main__':

    unittest.main()
