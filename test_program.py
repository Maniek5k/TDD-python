import unittest
import random

import program


class TestProgram(unittest.TestCase):

    def test_return_100(self):
        result = program.return_100()
        self.assertEqual(result, 100)
        pass

    def test_return_param(self):
        result = program.return_param("parametr podany")
        self.assertEqual(result, "parametr podany")

    def test_hello(self):
        hello = program.hello_world()
        self.assertEqual(hello.split(), ['Hello', 'World'])

    def test_calc_sum(self):
        rand1 = random.randint(1, 5)
        print(rand1)
        rand2 = random.randint(5, 50)
        print(rand2)
        calc = program.calc_sum(rand1, rand2)
        print(calc)
        # self.assertEqual(calc, sum(rand1, rand2))

    def test_calc_diff(self):
        diff = program.calc_diff(5, 2)
        self.assertEqual(diff, 3)

    def test_calc_multiply(self):
        multiply = program.calc_multi(10, 10)
        self.assertEqual(multiply, 100)

    def test_calc_divide(self):
        divide = program.calc_divide(100, 5)
        self.assertEqual(divide, 20)


if __name__ == "__main__":
    unittest.main()