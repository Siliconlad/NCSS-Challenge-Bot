import unittest
from helpers import is_higher
from helpers import sort

class Test(unittest.TestCase):
    def test_is_higher(self):
        self.assertEqual(False, is_higher('3D', '3C'))
        self.assertEqual(True, is_higher('JS', 'JD'))
        self.assertEqual(True, is_higher('2S', '3D'))
        self.assertEqual(False, is_higher('3D', '3D'))

if __name__ == '__main__':
    unittest.main()