from helpers import *

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    # Sort the hand because all functions assume the hand is sorted
    sorted_hand = sort(hand)

    # If start of round then must play 3D
    if is_start_of_round:
        return ['3D']

    playable_cards = playable(sorted_hand, play_to_beat)
    # Play lowest card
    if len(playable_cards) != 0:
        return [playable_cards[0]]
    else:
        return []

