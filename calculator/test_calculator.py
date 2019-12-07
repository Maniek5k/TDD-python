import unittest
import calculator_python

calc = calculator_python


class TestCalculator(unittest.TestCase):

    def test_calc_sum(self):
        summ1 = calc.calc_sum(5, 10)
        summ2 = calc.calc_sum(12, 11)
        self.assertEqual(summ1, 15)
        self.assertEqual(summ2, 23)

    def test_calc_diff(self):
        diff1 = calc.calc_diff(10, 5)
        diff2 = calc.calc_diff(50, 25)
        self.assertEqual(diff1, 5)
        self.assertEqual(diff2, 25)

    def test_calc_multiply(self):
        multiply1 = calc.calc_multi(5, 5)
        multiply2 = calc.calc_multi(10, 10)
        self.assertEqual(multiply1, 25)
        self.assertEqual(multiply2, 100)

    def test_calc_divide(self):
        divide1 = calc.calc_divide(50, 5)
        divide2 = calc.calc_divide(20, 10)
        self.assertEqual(divide1, 10)
        self.assertEqual(divide2, 2)


if __name__ == "__main__":
    unittest.main()
