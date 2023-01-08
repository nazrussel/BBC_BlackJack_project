from deck import Deck


class Hand:
    """Represents the cards held by the player or the dealer"""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.list_of_card_values =[]
        self.aces = 0  # keep track of aces for values (1 or 10)
        self.deck = Deck()

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += self.deck.ranks_value_sets()[card.rank]
        self.list_of_card_values.append(self.deck.ranks_value_sets()[card.rank])
        if card.rank == "A":
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces: # if the player's card values >21 and any Ace exist then decrease value and remove Ace
            self.value -= 10
            self.aces -= 1


# playerHand = Hand()
# newDeck = Deck()
# newDeck.shuffle()
# playerHand.add_card(newDeck.draw_card())
# playerHand.add_card(newDeck.draw_card())
# playerHand.add_card(newDeck.draw_card())
# playerHand.adjust_for_aces()
# print(playerHand.cards[0])