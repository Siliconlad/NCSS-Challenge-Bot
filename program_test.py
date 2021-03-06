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

        self.assertEqual(['KH'], play(['KH', 'AS' ,'2H'], False, ['JC'], [[[1, ['3D']], [2, ['3C']], [3, ['3S']], [0, ['5S']], [1, ['6C']], [2, ['7S']], [3, ['8D']], [0, ['8C']], [1, ['9H']], [2, ['0C']], [3, ['0S']], [0, ['JD']], [1, ['JH']], [2, ['JS']], [3, ['KS']], [0, ['AC']], [1, []], [2, []], [3, ['AH']], [0, ['2D']], [1, []], [2, []], [3, []]], [[0, ['6D']], [1, ['6H']], [2, ['8S']], [3, ['9S']], [0, ['0D']], [1, ['0H']], [2, ['QD']], [3, []], [0, ['QS']], [1, ['KD']], [2, ['AD']], [3, []], [0, ['2C']], [1, []], [2, []], [3, ['2S']], [0, []], [1, []], [2, []]], [[3, ['4H']], [0, ['7H']], [1, ['QC']], [2, ['QH']], [3, ['JC']]]], 0, [3, 5, 5, 4], [-14, -5, 26, -7], 6)) 

        self.assertEqual(['2H'], play(['JC', 'KH', '2H'], False, ['AS'], [[[1, ['3D']], [2, ['3C']], [3, ['3S']], [0, ['5S']], [1, ['6C']], [2, ['7S']], [3, ['8D']], [0, ['8C']], [1, ['9H']], [2, ['0C']], [3, ['0S']], [0, ['JD']], [1, ['JH']], [2, ['JS']], [3, ['KS']], [0, ['AC']], [1, []], [2, []], [3, ['AH']], [0, ['2D']], [1, []], [2, []], [3, []]], [[0, ['6D']], [1, ['6H']], [2, ['8S']], [3, ['9S']], [0, ['0D']], [1, ['0H']], [2, ['QD']], [3, []], [0, ['QS']], [1, ['KD']], [2, ['AD']], [3, []], [0, ['2C']], [1, []], [2, []], [3, ['2S']], [0, []], [1, []], [2, []]], [[3, ['4H']], [0, ['7H']], [1, ['QC']], [2, ['QH']], [3, ['AS']]]], 0, [3, 5, 5, 4], [-14, -5, 26, -7], 6)) 

if __name__ == '__main__':
    unittest.main()