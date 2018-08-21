import unittest
from program import play

class Test(unittest.TestCase):
    def test_play(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']
        
        # Basic play lowest possible card tests
        self.assertEqual(['7H'], play(hand, False, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['9S'], play(hand, False, ['9D'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        # Tests for when a player has one card left
        self.assertEqual(['KH'], play(hand, False, ['9D'], [[]], 0, [9, 9, 10, 1], [0, 0, 0, 0], 0))
        self.assertEqual(['KH'], play(['KH'], False, ['9D'], [[]], 0, [1, 9, 10, 10], [0, 0, 0, 0], 0))

        # Tests for when the player can win because of the number of highest 
        # cards in its hand
        hand = ['7H', '2S']
        self.assertEqual(['2S'], play(hand, False, [], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))
        
        hand = ['7H', '2H', '2S']
        self.assertEqual(['2H'], play(hand, False, [], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))

if __name__ == '__main__':
    unittest.main()