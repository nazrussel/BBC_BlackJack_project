from card import Card
import random

SUITS = ["♥", "♠", "♣", "♦"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
RANKS_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for s in range(len(SUITS)):
            for v in range(len(RANKS)):
                self.cards.append(Card(SUITS[s], RANKS[v]))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            self.build_deck()
            self.shuffle()
        single_card = self.cards.pop()
        return single_card

    def suits_set(self):
        suits_list = []
        for suit in SUITS:
            suits_list.append(suit)
        return suits_list

    def ranks_value_sets(self):
        ranks_value_set ={}
        for key,value in RANKS_VALUES.items():
            ranks_value_set[key] = value
        return ranks_value_set

    def __str__(self):
        deck_combination = ""
        for card in self.cards:
            deck_combination += "\n" + card.__str__()
        return deck_combination
#
#newDeck = Deck()
# print(newDeck)
# newDeck.cards =[]
# print("---",newDeck)
# newDeck.draw_card()

#print(newDeck.suits())
#print(newDeck.ranks_value_sets())
#print(newDeck)
# newDeck.shuffle()
# print(newDeck.__str__())
