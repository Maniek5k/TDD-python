import unittest

import strings


class TestStrings(unittest.TestCase):

    def test_upper(self):
        result = strings.return_upper('upper')
        self.assertEqual(result, 'UPPER')

    def test_lower(self):
        result = strings.return_lower('LOWER')
        self.assertEqual(result, 'lower')

    def test_capitalize(self):
        result = strings.returl_capitalize('capitalize')
        self.assertEqual(result, 'Capitalize')

    def


if __name__ == "__main__":
    unittest.main()
