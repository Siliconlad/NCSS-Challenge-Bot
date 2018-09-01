import unittest
from program import *

class Test(unittest.TestCase):
    def test_play_singles(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']
        self.assertEqual(['7H'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['9S'], play(hand, True, ['8C'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['KH'], play(hand, True, ['8C'], [[]], 0, [9, 9, 10, 1], [0, 0, 0, 0], 0))

    def test_play_doubles(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']
        self.assertEqual(['8D', '8S'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual([], play(hand, True, ['0D', '0C'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

    def test_play_triples(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']
        self.assertEqual(['JD', 'JH', 'JS'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['JD', 'JH', 'JS'], play(hand, True, ['0D', '0C', '0H'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual([], play(hand, True, ['AD', 'AC', 'AH'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

    # Tests for starting the round
    def test_play_start_round(self):
        # Starts round with multiple cards
        hand = ['3D', '3C', '3H', '3S', '4D', '7S', '0D']
        self.assertEqual(['3D', '3C', '3H'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        hand = ['3D', '3C', '3S', '4D', '7S', '0D']
        self.assertEqual(['3D', '3C', '3S'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        hand = ['3D', '3S', '4D', '7S', '0D']
        self.assertEqual(['3D', '3S'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        hand = ['3D', '3S', '4D', '7S', '0D', '0S']
        self.assertEqual(['3D', '3S'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        hand = ['3D', '4D', '7S', '0D', '0S']
        self.assertEqual(['3D'], play(hand, True, [], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
    
    # Tests for starting a trick
    def test_play_start_trick(self):
        # When hand contains all singles
        self.assertEqual(['AH'], play(['4S', '5C', '8C', '7S', 'AH'], False, [], [[]], 0, [5, 5, 1, 5], [0, 0, 0, 0], 0))
        self.assertEqual(['4S'], play(['4S', '5C', '8C', '7S', 'AH'], False, [], [[]], 0, [5, 5, 5, 5], [0, 0, 0, 0], 0))

        # When hand contains singles
        self.assertEqual(['7C', '7S'], play(['4S', '5C', '7C', '7S', 'AH'], False, [], [[]], 0, [5, 5, 1, 5], [0, 0, 0, 0], 0))
        self.assertEqual(['7C', '7S'], play(['4S', '5C', '7C', '7S', 'AH'], False, [], [[]], 0, [5, 5, 5, 5], [0, 0, 0, 0], 0))

        # When hand contains all doubles
        self.assertEqual(['5C', '5S'], play(['5C', '5S', '7C', '7S', 'AH', 'AS'], False, [], [[]], 0, [5, 5, 5, 5], [0, 0, 0, 0], 0))
        self.assertEqual(['5C', '5S'], play(['5C', '5S', '7C', '7S', 'AH', 'AS'], False, [], [[]], 0, [5, 5, 1, 5], [0, 0, 0, 0], 0))

        # When hand contains all triples
        self.assertEqual(['5D', '5C', '5S'], play(['5D', '5C', '5S', 'AD', 'AH', 'AS'], False, [], [[]], 0, [5, 5, 5, 5], [0, 0, 0, 0], 0))

        # When hand contains no singles
        self.assertEqual(['AD', 'AH', 'AS'], play(['5C', '5S', '7C', '7S', 'AD', 'AH', 'AS'], False, [], [[]], 0, [5, 5, 5, 5], [0, 0, 0, 0], 0))
    # Tests for playing singles
    def test_play_singles(self):
        hand = ['7H', '8D', '8S', '9S', '0S', 'JD', 'JH', 'JS', 'KH']
        
        # Basic play lowest possible card tests
        self.assertEqual(['0S'], play(hand, False, ['0D'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))
        self.assertEqual(['9S'], play(hand, False, ['9D'], [[]], 0, [9, 9, 10, 10], [0, 0, 0, 0], 0))

        # Tests for when a player has one card left
        self.assertEqual(['KH'], play(hand, False, ['9D'], [[]], 0, [9, 9, 10, 1], [0, 0, 0, 0], 0))
        self.assertEqual(['KH'], play(['KH'], False, ['9D'], [[]], 0, [1, 9, 10, 10], [0, 0, 0, 0], 0))

        # Tests for when the player can win because of the number of highest 
        # cards in its hand
        hand = ['7H', '2S']
        self.assertEqual(['2S'], play(hand, False, ['AD'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))
        
        hand = ['7H', '2H', '2S']
        self.assertEqual(['2H'], play(hand, False, ['AS'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))

        self.assertEqual(['KH'], play(['KH', 'AS' ,'2H'], False, ['JC'], [[[1, ['3D']], [2, ['3C']], [3, ['3S']], [0, ['5S']], [1, ['6C']], [2, ['7S']], [3, ['8D']], [0, ['8C']], [1, ['9H']], [2, ['0C']], [3, ['0S']], [0, ['JD']], [1, ['JH']], [2, ['JS']], [3, ['KS']], [0, ['AC']], [1, []], [2, []], [3, ['AH']], [0, ['2D']], [1, []], [2, []], [3, []]], [[0, ['6D']], [1, ['6H']], [2, ['8S']], [3, ['9S']], [0, ['0D']], [1, ['0H']], [2, ['QD']], [3, []], [0, ['QS']], [1, ['KD']], [2, ['AD']], [3, []], [0, ['2C']], [1, []], [2, []], [3, ['2S']], [0, []], [1, []], [2, []]], [[3, ['4H']], [0, ['7H']], [1, ['QC']], [2, ['QH']], [3, ['JC']]]], 0, [3, 5, 5, 4], [-14, -5, 26, -7], 6)) 

        self.assertEqual(['2H'], play(['JC', 'KH', '2H'], False, ['AS'], [[[1, ['3D']], [2, ['3C']], [3, ['3S']], [0, ['5S']], [1, ['6C']], [2, ['7S']], [3, ['8D']], [0, ['8C']], [1, ['9H']], [2, ['0C']], [3, ['0S']], [0, ['JD']], [1, ['JH']], [2, ['JS']], [3, ['KS']], [0, ['AC']], [1, []], [2, []], [3, ['AH']], [0, ['2D']], [1, []], [2, []], [3, []]], [[0, ['6D']], [1, ['6H']], [2, ['8S']], [3, ['9S']], [0, ['0D']], [1, ['0H']], [2, ['QD']], [3, []], [0, ['QS']], [1, ['KD']], [2, ['AD']], [3, []], [0, ['2C']], [1, []], [2, []], [3, ['2S']], [0, []], [1, []], [2, []]], [[3, ['4H']], [0, ['7H']], [1, ['QC']], [2, ['QH']], [3, ['AS']]]], 0, [3, 5, 5, 4], [-14, -5, 26, -7], 6)) 

    # Tests for playing doubles
    def test_play_doubles(self):
        hand = ['3S', '4D', '4C', '5C', '5H', '5S', '6C', '6H', '7C', '7H', '7S', '8S', '9D', '9S', '0D', '0C', 'QD', 'QC', 'QS', 'KD', 'KH', 'KS', 'AH', 'AS']
        self.assertEqual(['4D', '4C'], play(hand, False, ['3D', '3C'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))
        self.assertEqual(['6C', '6H'], play(hand, False, ['4H', '4S'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))

    # Tests for playing triples
    def test_play_triples(self):
        hand = ['3S', '4D', '4C', '5C', '5H', '5S', '6C', '6H', '7C', '7H', '7S', '8S', '9D', '9S', '0D', '0C', 'QD', 'QC', 'QS', 'KD', 'KH', 'KS', 'AH', 'AS']

        self.assertEqual(['5C', '5H', '5S'], play(hand, False, ['3D', '3C', '3H'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))
        self.assertEqual([], play(hand, False, ['2D', '2C', '2H'], [[]], 0, [2, 13, 13, 13], [0, 0, 0, 0], 0))

if __name__ == '__main__':
    unittest.main()