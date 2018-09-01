import itertools

SUIT_SCORE = {"D":0, "C":1, "H":2, "S":3}
RANK_SCORE = {"3":0, "4":1, "5":2, "6":3, "7":4, "8":5, "9":6, "0": 7, "J":8, "Q":9, "K":10, "A":11, "2":12}

# Functions relating to single cards

def is_better_play(first, second):    
    '''
    The function, given two lists, determines which play, first or second, is a better play.

    The function compares two lists which can be either a one, two or three card play and compares whether the first play or the second play is better. If they are of different lengths then False is returned.

    Keyword arguements:
    first -- LIST
    second -- LIST

    Return value:
    True -- if first is a better play than second
    False -- if second is a better play than first

    Assumptions:
    -- Assumes parameters are lists
    -- Assumes first and second are sorted
    -- Assumes the cards are not 5 cards long (yet)
    '''

    length_of_play = len(first)

    if length_of_play != 5:
        if length_of_play != len(second):
            return False
        elif RANK_SCORE[first[-1][0]] > RANK_SCORE[second[-1][0]]:
            return True
        elif RANK_SCORE[first[-1][0]] < RANK_SCORE[second[-1][0]]:
            return False
        else:
            if SUIT_SCORE[first[-1][1]] > SUIT_SCORE[second[-1][1]]:
                return True
            else:
                return False

def sort(singles):
    '''
    Returns a sorted list of singles.

    The function differs from sort_cards in that the input is a list of strings (single cards) hence has the format [card1, card2, card3].

    Keyword arguement:
    singles -- list of strings

    Return type:
    list of strings
    '''

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        counter = 1
        length_of_cards = len(singles)
        for i in range(length_of_cards - counter):
            if is_better_play([singles[i]], [singles[i+1]]):
                # Swap
                singles[i], singles[i+1] = singles[i+1], singles[i]
                is_sorted = False
        counter += 1
    return singles

def sort_cards(cards):
    '''
    Returns a sorted list of pairs or triples.

    The function accepts a list of cards (pairs or triples) of the format [[cards_1], [cards_2]] and sorts and returns the list. The sorting algorithm uses a bubble sort.

    Keyword arguements:
    cards -- a list of lists

    Return type:
    list of lists -- returns the sorted list
    '''

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        counter = 1
        length_of_cards = len(cards)
        for i in range(length_of_cards - counter):
            if is_better_play(cards[i], cards[i+1]):
                # Swap
                cards[i], cards[i+1] = cards[i+1], cards[i]
                is_sorted = False
        counter += 1
    return cards

def highest(hand, round_history):
    '''
    Returns a list of all the highest cards in the game from hand.

    The function loops through the round_history removes all cards from a list of the entire deck of cards. Then the functions looks to see if the highest remaining cards in the game are in the player's hand

    Keyword arguements:
    hand -- a sorted list of all the cards in the players hand
    round_history -- a list of all the plays in the current round, organised into trick lists which contain play lists. A play list is a list with the player number and card played by that player.

    Return type:
    list -- stores all the highest cards in the game in the given hand

    Function assumptions:
    -- the function assumes hand is sorted
    '''

    deck = ['3D', '3C', '3H', '3S', '4D', '4C', '4H', '4S', '5D', '5C', '5H', '5S', '6D', '6C', '6H', '6S', '7D', '7C', '7H', '7S', '8D', '8C', '8H', '8S', '9D', '9C', '9H', '9S', '0D', '0C', '0H', '0S', 'JD', 'JC', 'JH', 'JS', 'QD', 'QC', 'QH', 'QS', 'KD', 'KC', 'KH', 'KS', 'AD', 'AC', 'AH', 'AS', '2D', '2C', '2H', '2S']

    # Removes all cards from deck that have already been played
    for trick_history in round_history:
        for play in trick_history:
            card = play[1]
            if len(card) == 0:
                pass
            elif card[0] in deck:
                deck.remove(card[0])

    highest_cards = []
    while deck[-1] in hand:
        highest_cards.append(deck.pop(-1))
    
    return sort(highest_cards)

# Functions relating to pairs of cards

def is_pair(card1, card2):
    '''
    Compares two cards to see if they form a pair or not.

    Takes two cards and compares the ranks to see if they match. If they do True is returned, if not False. 

    Keyword arguements:
    card1 -- string
    card2 -- string

    Return Type:
    -- Boolean (True/False)
    '''

    if (card1[0] == card2[0]):
        return True
    else:
        return False

def all_pairs(hand):
    '''
    Returns a list of all possible pairs from a given hand.

    Given a list of cards, the program will go through every combination of cards, check that they are a valid pair then add them to a list which is returned.

    Keyword arguements:
    hand -- list of cards

    Return type:
    -- a sorted list of all possible pairs from the given hand
    '''

    pairs = []
    for pair in itertools.combinations(hand, 2):
        if is_pair(pair[0], pair[1]):
            pair = sort(list(pair))
            pairs.append(pair)
    return sort_cards(pairs)

# Functions relating to triple cards

def is_triple(card1, card2, card3):
    '''
    Compares three cards to see if they form a triple or not.

    Takes three cards and compares the ranks (number value) to see if they match. If they do True is returned, if not False. 

    Keyword arguements:
    card1 -- string
    card2 -- string
    card3 -- string

    Return Type:
    -- Boolean (True/False)

    '''

    if (card1[0] == card2[0] == card3[0]):
        return True
    else:
        return False

def all_triples(hand):
    '''
    Returns a list of all possible triples from a given hand.

    Given a list of cards, the program will go through every combination of a group of three cards, check that they are a valid triple then add them to a list which is returned.

    Keyword arguements:
    hand -- list of cards

    Return type:
    -- list of all possible triples from the given hand
    '''

    triples = []
    for triple in itertools.combinations(hand, 3):
        if is_triple(triple[0], triple[1], triple[2]):
            triple = sort(list(triple))
            triples.append(list(triple))
    return sort_cards(triples)

# Functions relating to all three card variations

def playable(hand, play_to_beat):
    '''
    Returns a list of all the cards in the hand greater than the card to beat.

    The function takes in two parameters, hand and play_to_beat. Depending on the size of the play_to_beat (i.e. is it a 2 card play) the function will return a list of all possible card plays.

    For example if play_to_beat is a card pair, then the function will return a list of all possible playable pairs. Similarily for a triple card play. For a single card the function will return a list of card strings that are playable.
    
    The function will return an empty list if no cards in hand are greater than the play_to_beat.

    Keyword arguements:
    hand -- a list of single cards
    play_to_beat -- a list containing a card play (i.e. [card] or [[pair]] or [[triple]])

    Return type:
    playable_cards -- a list, or a list of lists, of all the card combinations that will beat the play_to_beat card depending on its length.

    Function assumptions:
    -- play_to_beat is a list with card play
    -- the hand is sorted
    '''

    size_of_play = len(play_to_beat)
    # If starting trick or round
    if size_of_play == 0:
        return hand
    # If play_to_beat is a single card
    elif size_of_play == 1:
        for card in hand:
            if is_better_play([card], play_to_beat):
                index = hand.index(card)
                return hand[index:]
    # If play_to_beat is a pair
    elif size_of_play == 2:
        pairs = all_pairs(hand)
        for pair in pairs:
            if is_better_play(pair, play_to_beat):
                index = pairs.index(pair)
                return pairs[index:]
    # If play_to_beat is a triple
    elif size_of_play == 3:
        triples = all_triples(hand)
        for triple in triples:
            if is_better_play(triple, play_to_beat):
                index = triples.index(triple)
                return triples[index:]

    return []

def not_in_pair(card, pairs):
    '''
    Determines whether card is in a list of pairs.

    The function takes a card value and goes through the pairs list to see if the card forms part of a pair or pairs. If it does then it returns False, if not the return True.

    Keyword arguements:
    card -- string
    pairs -- a list of lists (a list of pairs)

    Return value:
    True -- the card is not in the pairs list
    False -- the card is in the pairs list
    '''

    for pair in pairs:
        if card in pair:
            return False
    
    return True

def not_in_triple(pair, triples):
    '''
    Determines whether a pair is part of a triple.

    The function loops through a list of triples to see if a card from the pair list is used as part of a triple. If it is then the pair cannot be played because it is part of a higher value combination.

    Keyword arguements:
    pair -- a list of two cards
    triples -- a list of lists (a list of triples)

    Return value:
    True -- the pair is not used in the list
    False -- the pair is used in the list
    '''
    
    card = pair[0]
    for triple in triples:
        if card in triple:
            return False
    
    return True

