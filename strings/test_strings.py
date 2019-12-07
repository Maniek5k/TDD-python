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
        result = strings.return_capitalize('capitalize')
        self.assertEqual(result, 'Capitalize')

    def test_len(self):
        result = strings.return_length('length')
        self.assertEqual(result, 6)

    def test_title(self):
        result = strings.return_title('this is test phrase')
        self.assertEqual(result, 'This Is-- Test Phrase')


if __name__ == "__main__":
    unittest.main()
