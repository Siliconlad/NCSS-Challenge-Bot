import unittest
from helpers import *

class Test(unittest.TestCase):
    def test_is_higher(self):
        self.assertEqual(False, is_higher('3D', '3C'))
        self.assertEqual(True, is_higher('JS', 'JD'))
        self.assertEqual(True, is_higher('2S', '3D'))
        self.assertEqual(False, is_higher('3D', '3D'))

    def test_sort(self):
        self.assertEqual(['3D', '3C', '3H', '3S'], sort(['3S', '3D', '3H', '3C']))
        self.assertEqual(['3D', '8D', '0D', 'AD', '2S'], sort(['AD', '2S', '0D', '8D', '3D']))

    def test_playable(self):
        hand = ['3D', '4D', '4S', '7C', '8S', 'JD', 'JC', 'JS', 'KD', 'KS', 'AS', '2D', '2H']
        self.assertEqual(['7C', '8S', 'JD', 'JC', 'JS', 'KD', 'KS', 'AS', '2D', '2H'], playable(hand, ['7D']))
        self.assertEqual(['2H'], playable(hand, ['2C']) )
        self.assertEqual( [], playable(hand, ['2S']) )
        self.assertEqual( hand, playable(hand, []) )

    def test_highest(self):
        hand = ['JD', '2H', '2S']
        round_history = [[[3, ['3D']], [0, ['6C']], [1, []], [2, ['6H']], [3, ['0H']]]]
        self.assertEqual(['2H', '2S'], highest(hand, round_history))

        hand = ['JD']
        round_history = [[]]
        self.assertEqual([], highest(hand, round_history))

        hand = ['4D', '2H']
        round_history = [[ [0, ['3D']], [1, ['3C']], [2, []], [3, ['4S']], [0, ['7D']], [1, ['9C']], [2, []], [3, ['JD']], [0, ['2C']], [1, ['2S']] ] , [ [1, ['3S']], [2, []], [3, []] ]]
        self.assertEqual(['2H'], highest(hand, round_history))

    def test_is_pair(self):
        self.assertEqual(True, is_pair('3D', '3S'))
        self.assertEqual(False, is_pair('JD', 'QD'))

    def test_is_higher_pair(self):
        self.assertEqual(True, is_higher_pair(['JD', 'JS'], ['0H', '0S']))
        self.assertEqual(True, is_higher_pair(['JD', 'JS'], ['JC', 'JC']))
        self.assertEqual(False, is_higher_pair(['3D', '3S'], ['2C', '2C']))

    def test_all_pairs(self):
        hand = ['3D', '3C', '3S', '4D', '8D', '8S', '0J', '2S']
        self.assertEqual([['3D', '3C'], ['3D', '3S'], ['3C', '3S'], ['8D', '8S']], all_pairs(hand))

    def test_sort_pairs(self):
        self.assertEqual([['3D', '3S']], sort_pairs([['3D', '3S']]))
        self.assertEqual([['3D', '3S'], ['2D', '2S']], sort_pairs([['2D', '2S'], ['3D', '3S']]))
        self.assertEqual([['2D', '2C'], ['2H', '2S']], sort_pairs([['2H', '2S'], ['2D', '2C']]))
if __name__ == '__main__':
    unittest.main()