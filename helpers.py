import itertools

SUIT_SCORE = {"D":0, "C":1, "H":2, "S":3}
RANK_SCORE = {"3":0, "4":1, "5":2, "6":3, "7":4, "8":5, "9":6, "0": 7, "J":8, "Q":9, "K":10, "A":11, "2":12}

# Functions relating to single cards

def is_higher(card1, card2):
    '''
    The function compares two cards to see which is ranked higher.

    The function compares two valid cards and returns true if card1 is ranked higher and false if it does not. Does not assume that the cards must be from the same deck. If two equivalent cards are passed then the function will return False because a card is not ranked higher than itself.

    Keywords arguements:
    card1 -- first card of type string (required), cannot be empty
    card2 -- second card of type string (required), cannot be empty

    Return type:
    True -- when card1 is ranked higher than card2
    False -- when card1 is ranked lower than card2

    Function assumptions:
    -- Valid card format e.g. '3D'
    -- Valid card e.g. NOT '9Y'
    '''

    card1_num_rank = RANK_SCORE[card1[0]]
    card2_num_rank = RANK_SCORE[card2[0]]

    # Compare card number
    if card1_num_rank < card2_num_rank:
        return False
    elif card1_num_rank > card2_num_rank:
        return True
    # Compare suits if ranks are equal
    else:
        card1_suit_rank = SUIT_SCORE[card1[1]]
        card2_suit_rank = SUIT_SCORE[card2[1]]

        return True if card1_suit_rank > card2_suit_rank else False

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

def sort(hand):
    '''
    The function returns a sorted list of cards.

    The function sorts a list of single cards and returns them in ascending order. The parameter of the function must be a list of strings. It should not contain any lists or other data structures.

    Keyword arguements:
    hand -- a list of single cards

    Return type:
    sorted_list -- a list of sorted cards in ascending order

    Function assumptions:
    -- The hand is a list of strings
    '''

    # Implements a bubble sort algorithm for sorting the hand
    is_sorted = False
    while not is_sorted:
        # Assume list is sorted
        is_sorted = True
        for index in range(0, len(hand) - 1):
            if is_higher(hand[index], hand[index + 1]):
                temp = hand[index]
                hand[index] = hand[index+1]
                hand[index+1] = temp
                is_sorted = False

    return hand

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

def is_higher_pair(pair1, pair2):
    '''
    Compares a pair of pairs to find which pair is ranked higher.

    The function compares pair1 and pair2. If pair1 is ranked higher then the function returns True if not then False. Order of the parameters matter when comparing two pairs.

    Keyword arguements:
    pair1, pair2 -- list of two cards i.e. ['3D', '3S']

    Return type:
    -- Boolean (True/False)

    Assumptions:
    -- Assumes pair1 and pair2 are valid pairs
    '''

    # Sort the pairs
    pair1 = sort(pair1)
    pair2 = sort(pair2)

    pair1_rank_score = RANK_SCORE[pair1[1][0]]
    pair2_rank_score = RANK_SCORE[pair2[1][0]]

    if pair1_rank_score < pair2_rank_score:
        return False
    elif pair1_rank_score > pair2_rank_score:
        return True
    else:
        pair1_highest_suit_score = SUIT_SCORE[pair1[1][1]]
        pair2_highest_suit_score = SUIT_SCORE[pair2[1][1]]

        if pair1_highest_suit_score > pair2_highest_suit_score:
            return True
        elif pair1_highest_suit_score < pair2_highest_suit_score:
            return False
        # If they both have the same highest card, possible when finding all 
        # possible pairs in a given hand
        else:
            pair1_lowest_suit_score = SUIT_SCORE[pair1[0][1]]
            pair2_lowest_suit_score = SUIT_SCORE[pair2[0][1]]

            if pair1_lowest_suit_score > pair2_lowest_suit_score:
                return True
            elif pair1_lowest_suit_score < pair2_lowest_suit_score:
                return False
            else:
                return False


def sort_pairs(pairs):
    '''
    Returns a sorted list of pairs.

    The function accepts a list of pairs of the format [[pair_1], [pair_2]] and sorts the pairs and returns the list. The sorting algorithm uses a bubble sort.

    Keyword Arguements:
    pairs -- a list of pairs

    Return type:
    list of lists -- returns a list of all pairs in pairs but sorted

    '''

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        counter = 1
        size_of_pairs = len(pairs)
        for i in range(size_of_pairs - counter):
            if is_higher_pair(pairs[i], pairs[i+1]):
                # Swap
                pairs[i], pairs[i+1] = pairs[i+1], pairs[i]
                is_sorted = False
        counter += 1
    return pairs

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
            pairs.append(list(pair))
    return sort_pairs(pairs)

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

def is_higher_triple(triple1, triple2):
    '''
    Compares a pair of triples to find which triple is ranked higher.

    The function compares triple1 and triple2. If triple1 is ranked higher then the function returns True if not then False. Order of the parameters matter when comparing the two triples.

    Keyword arguements:
    triple1, triple2, triple3 -- list of three cards i.e. ['3D', '3C', '3S']

    Return type:
    -- Boolean (True/False)

    Assumptions:
    -- Assumes pair1 and pair2 are valid triples
    '''

    # Sort the pairs
    triple1 = sort(triple1)
    triple2 = sort(triple2)

    triple1_rank = triple1[2][0]
    triple2_rank = triple2[2][0]
    triple1_highest_suit = triple1[2][1]
    triple2_highest_suit = triple2[2][1]

    if RANK_SCORE[triple1_rank] < RANK_SCORE[triple2_rank]:
        return False
    elif RANK_SCORE[triple1_rank] > RANK_SCORE[triple2_rank]:
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
            triples.append(list(triple))
    return triples

def sort_triples(triples):
    '''
    Returns a sorted list of triples.

    The function accepts a list of triples of the format [[triple_1], [triple_2]] and sorts the triples and returns the list. The sorting algorithm uses a bubble sort.

    Keyword Arguements:
    triples -- a list of triples

    Return type:
    list of lists -- returns a list of all triples but sorted

    '''

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        counter = 1
        size_of_triples = len(triples)
        for i in range(size_of_triples - counter):
            if is_higher_triple(triples[i], triples[i+1]):
                # Swap
                triples[i], triples[i+1] = triples[i+1], triples[i]
                is_sorted = False
        counter += 1
    return triples

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
        card_to_beat = play_to_beat[0]
        for card in hand:
            if is_higher(card, card_to_beat):
                index = hand.index(card)
                return hand[index:]
    # If play_to_beat is a pair
    elif size_of_play == 2:
        pairs = all_pairs(hand)
        for pair in pairs:
            if is_higher_pair(pair, play_to_beat):
                index = pairs.index(pair)
                return pairs[index:]
    # If play_to_beat is a triple
    elif size_of_play == 3:
        triples = all_triples(hand)
        for triple in triples:
            if is_higher_triple(triple, play_to_beat):
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