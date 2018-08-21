import unittest
from helpers import is_higher
from helpers import sort

class Test(unittest.TestCase):
    def test_is_higher(self):
        self.assertEqual(False, is_higher('3D', '3C'))
        self.assertEqual(True, is_higher('JS', 'JD'))
        self.assertEqual(True, is_higher('2S', '3D'))
        self.assertEqual(False, is_higher('3D', '3D'))

    def test_sort(self):
        self.assertEqual(['3D', '3C', '3H', '3S'], sort(['3S', '3D', '3H', '3C']))
        self.assertEqual(['3D', '8D', '0D', 'AD', '2S'], sort(['AD', '2S', '0D', '8D', '3D']))

if __name__ == '__main__':
    unittest.main()