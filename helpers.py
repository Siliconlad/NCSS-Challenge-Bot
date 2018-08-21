def is_higher(card1, card2):
    '''
    The function compares two cards to see which is ranked higher.

    The function compares two valid cards and returns true if card1 is ranked higher and false if it does not. Does not assume that the cards must be from the same deck. If two equivalent cards are passed then the function will return False because a card is not ranked higher than itself.

    Keywords arguements:
    card1 -- first card of type string (required)
    card2 -- second card of type string (required)

    Return type:
    True -- when card1 is ranked higher than card2
    False -- when card1 is ranked lower than card2

    Function assumptions:
    -- Valid card format e.g. '3D'
    -- Valid card e.g. NOT '9Y'
    '''

    suit_score = {"D": 0, "C": 1, "H": 2, "S": 3}
    rank_score = {"3":0, "4":1, "5":2, "6":3, "7":4, "8":5, "9":6, "0":7, "J":8, "Q":9, "K":10, "A":11, "2":12}

    card1_num_rank = rank_score[card1[0]]
    card2_num_rank = rank_score[card2[0]]

    # Compare card number
    if card1_num_rank < card2_num_rank:
        return False
    elif card1_num_rank > card2_num_rank:
        return True
    # Compare suits if ranks are equal
    else:
        card1_suit_rank = suit_score[card1[1]]
        card2_suit_rank = suit_score[card2[1]]

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
    play_to_beat = a list containing one card

    Return type:
    playable_cards -- a list of all the cards that will beat the play_to_beat card

    Function assumptions:
    -- play_to_beat is a list with one card
    -- the hand is sorted
    '''
    card_to_beat = play_to_beat[0]
    for card in hand:
        if is_higher(card, card_to_beat):
            index = hand.index(card)
            return hand[index:]

    return []