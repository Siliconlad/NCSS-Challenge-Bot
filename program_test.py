import unittest
from program import play

class Test(unittest.TestCase):
    def test_play(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']

        self.assertEqual(['7H'], play(hand, False, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['9S'], play(hand, False, ['9D'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))



if __name__ == '__main__':
    unittest.main()