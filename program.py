from helpers import *

def play_singles(sorted_hand, play_to_beat, round_history, hand_sizes):
    size_of_hand = len(sorted_hand)

    highest_cards = highest(sorted_hand, round_history)
    size_of_highest = len(highest_cards)
    if size_of_highest != 0:
        # If a player can win the round by playing all their highest cards 
        if size_of_highest >= size_of_hand-1:
            playable_highest = playable(highest_cards, play_to_beat)
            if len(playable_highest) != 0:
                return [playable_highest[0]]

    playable_cards = playable(sorted_hand, play_to_beat)
    # If someone has one card left play the highest card to delay their win
    # If I have one card left play it
    if 1 in hand_sizes:
        return [playable_cards[-1]]
    
    # Play lowest card that is not part of a pair or triple
    pairs = all_pairs(sorted_hand)
    for card in playable_cards:
        if not_in_pair(card, pairs):
            return [card]

    # Pass if nothing is satisfied
    return []

def play_pairs(sorted_hand, play_to_beat):
    if len(play_to_beat) != 0:
        playable_cards = playable(sorted_hand, play_to_beat)
    else:
        playable_cards = all_pairs(sorted_hand)

    triples = all_triples(sorted_hand)
    # Play the lowest card not in triples
    for pair in playable_cards:
        
        if not_in_triple(pair, triples):
            return pair
    return []

def play_triples(sorted_hand, play_to_beat):
    if len(play_to_beat) != 0:
        playable_hand = playable(sorted_hand, play_to_beat)
    else:
        playable_hand = all_triples(sorted_hand)

    if len(playable_hand) > 0:
        return playable_hand[0]
    else:
        return []

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    # Sort the hand because all functions assume the hand is sorted
    sorted_hand = sort(hand)

    triples = all_triples(sorted_hand)
    pairs = all_pairs(sorted_hand)
    if is_start_of_round:
        # Because pairs and triples are sorted first item must be the lowest
        # Hence for loop does not cost anything
        for triple in triples:
            if '3D' in triple[0]:
                return triple
        
        for pair in pairs:
            if '3D' in pair:
                return pair
        
        return ['3D']

    playable_cards = playable(sorted_hand, play_to_beat)
    size_of_playable = len(playable_cards)
    # Allows rest of program to assume there is at least one card to play
    if size_of_playable == 0:
        return []

    size_of_play_to_beat = len(play_to_beat)
    # If we are starting a trick
    if size_of_play_to_beat == 0:
        output = play_triples(sorted_hand, play_to_beat)

        if output == []:
            output = play_pairs(sorted_hand, play_to_beat)

        if output == []:
            output =  play_singles(sorted_hand, play_to_beat, round_history, hand_sizes)

        return output
    # Rules for single cards
    elif size_of_play_to_beat == 1:
        return play_singles(sorted_hand, play_to_beat, round_history, hand_sizes)
    # Rules for playing doubles
    elif size_of_play_to_beat == 2:
        return play_pairs(sorted_hand, play_to_beat)
    elif size_of_play_to_beat == 3:
        return play_triples(sorted_hand, play_to_beat)
    else:
        return []