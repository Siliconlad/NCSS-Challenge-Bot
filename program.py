from helpers import *

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    # Sort the hand because all functions assume the hand is sorted
    sorted_hand = sort(hand)

    # If start of round then must play 3D
    if is_start_of_round:
        return ['3D']

    playable_cards = playable(sorted_hand, play_to_beat)
    # Return nothing when no cards available to play
    if len(playable_cards) == 0:
        return []

    # Play highest card when someone has one card left, to get rid of as many 
    # cards as possible. If I am the one with one card then this simply plays 
    # the remaining card.
    if 1 in hand_sizes:
        return [playable_cards[-1]]


    return [playable_cards[0]]

