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
        rand2 = random.randint(5, 50)
        summ = program.calc_sum(rand1, rand2)
        self.assertEqual(summ, (rand1 + rand2))

    def test_calc_diff(self):
        rand1 = random.randint(1, 5)
        rand2 = random.randint(5, 50)
        diff = program.calc_diff(rand1, rand2)
        self.assertEqual(diff, (rand1 - rand2))

    def test_calc_multiply(self):
        rand1 = random.randint(1, 5)
        rand2 = random.randint(5, 50)
        multiply = program.calc_multi(rand1, rand2)
        self.assertEqual(multiply, (rand1 * rand2))

    def test_calc_divide(self):
        rand1 = random.randint(1, 5)
        rand2 = random.randint(5, 50)
        divide = program.calc_divide(rand1, rand2)
        self.assertEqual(divide, (rand1 / rand2))


if __name__ == "__main__":
    unittest.main()
