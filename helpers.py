SUIT_SCORE = {"D":0, "C":1, "H":2, "S":3}
RANK_SCORE = {"3":0, "4":1, "5":2, "6":3, "7":4, "8":5, "9":6, "0": 7, "J":8, "Q":9, "K":10, "A":11, "2":12}

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

def playable(hand, play_to_beat):
    '''
    Returns a list of all the cards in the hand greater than the card to beat.

    The function takes in two parameters, hand and play_to_beat. The function then returns all the cards greater than the play_to_beat in the hand of the player in a list. The function will return an empty list if no cards in hand are greater than the play_to_beat.

    Keyword arguements:
    hand -- a list of single cards
    play_to_beat -- a list containing one card

    Return type:
    playable_cards -- a list of all the cards that will beat the play_to_beat card

    Function assumptions:
    -- play_to_beat is a list with one card
    -- the hand is sorted
    '''
    if len(play_to_beat) == 0:
        return hand
    
    card_to_beat = play_to_beat[0]
    for card in hand:
        if is_higher(card, card_to_beat):
            index = hand.index(card)
            return hand[index:]

    return []

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
    -- Assumes pair1 and pair2 sorted from least to greatest i.e. ['3D', '3S'] and NOT ['3S', '3D']
    '''

    pair1_rank = pair1[1][0]
    pair2_rank = pair2[1][0]
    pair1_highest_suit = pair1[1][1]
    pair2_highest_suit = pair2[1][1]

    if RANK_SCORE[pair1_rank] < RANK_SCORE[pair2_rank]:
        return False
    elif RANK_SCORE[pair1_rank] > RANK_SCORE[pair2_rank]:
        return True
    else:
        if SUIT_SCORE[pair1_highest_suit] == 3:
            return True
        elif SUIT_SCORE[pair2_highest_suit] == 3:
            return False

def all_pairs(hand):
    '''
    Returns a list of all possible pairs from a given hand.

    Given a list of cards, the program will go through every combination of cards, check that they are a valid pair then add them to a list which is returned.

    Keyword arguements:
    hand -- list of cards

    Return type:
    -- list of all possible pairs from the given hand
    '''

    pairs = []
    for pair in itertools.combinations(hand, 2):
        if is_pair(pair[0], pair[1]):
            pairs.append(list(pair))
    return pairs

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