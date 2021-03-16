from unittest import main, TestCase
from error_limits import imprecise, Range
from math import pi, sin


class TestStringMethods(TestCase):

    def test_readme_example_1(self):
        @imprecise
        def calculate_area(r):
            return pi * r ** 2

        area = calculate_area(Range(0.52, 0.56))
        self.assertEqual(area.lower, calculate_area(0.52).lower)
        self.assertEqual(area.lower, calculate_area(0.52).upper)
        self.assertEqual(area.upper, calculate_area(0.56).lower)
        self.assertEqual(area.upper, calculate_area(0.56).upper)

    def test_readme_example_2(self):
        @imprecise
        def calculate(a, b, c, d=1, e=0):
            return (a * sin(b + c)) ** d + e

        result = calculate(Range(2, 3), 4, 0, e=Range(1, 2))

        self.assertEqual(result.lower, calculate(3, 4, 0, e=1).lower)
        self.assertEqual(result.lower, calculate(3, 4, 0, e=1).upper)
        self.assertEqual(result.upper, calculate(2, 4, 0, e=2).lower)
        self.assertEqual(result.upper, calculate(2, 4, 0, e=2).upper)


if __name__ == '__main__':
    main()
