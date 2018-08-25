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

    highest_cards = highest(sorted_hand, round_history)

    # If the player has only one card which is not the highest card in the game
    # and the rest are the highest cards in the game, then play highest playable card
    if len(highest_cards) != 0 and len(highest_cards) == len(sorted_hand) - 1:
        playable_highest = playable(highest_cards, play_to_beat)
        if len(playable_highest) != 0:
            return [playable_highest[0]]
            

    # Play highest card when someone has one card left,
    # to get rid of as many cards as possible. 
    # If I am the one with one card then this simply plays the remaining card.
    if 1 in hand_sizes:
        return [playable_cards[-1]]

    return [playable_cards[0]]

