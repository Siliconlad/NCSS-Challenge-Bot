def is_higher(card1, card2):
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

        return False if card1_suit_rank < card2_suit_rank else True