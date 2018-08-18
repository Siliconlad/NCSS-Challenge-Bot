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
        card1_suit_rank = rank_score[card1[0]]
        card2_suit_rank = rank_score[card2[0]]

        return True if card1_suit_rank > card2_suit_rank else False