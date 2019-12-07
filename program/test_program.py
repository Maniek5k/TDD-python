import unittest

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


if __name__ == "__main__":
    unittest.main()
