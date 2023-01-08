SUITS = ["♥", "♠", "♣", "♦"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    """Represents an individual playing card"""

    def __init__(self, suit, rank):
        assert suit in SUITS
        self.suit = suit
        assert rank in RANKS
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# myCards = Card("♥",6)
# result = myCards.show_cards()
# print(result[0])
