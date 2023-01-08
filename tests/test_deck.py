import unittest
from deck import *


class DeckTestCase(unittest.TestCase):
    """Unit tests for Deck class"""

    def setUp(self):
        self.deck = Deck()

    def test_size_of_deck(self):
        """Are there 52 cards in the deck?"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle_deck(self):
        """Does the deck get shuffled?"""
        deck_one = Deck()
        deck_one.shuffle()
        deck_two = Deck()
        deck_two.shuffle()
        self.assertNotEqual(str(deck_one), str(deck_two))

    def test_deck_removes_a_card(self):
        """Does a draw_card() removes a card from the deck?"""
        num_before = len(self.deck.cards)
        self.deck.draw_card()
        num_after = len(self.deck.cards)
        self.assertEqual(num_before, num_after + 1)

    def test_deck_return_a_card(self):
        """Does calling draw_card() return a card?"""
        self.assertIsInstance(self.deck.draw_card(), Card)

    def test_empty_deck_refills(self):
        """Does an empty deck get refilled?"""
        newDeck = Deck()
        newDeck.cards = []
        newDeck.draw_card()
        self.assertEqual(len(newDeck.cards), 51)

    def tearDown(self):
        """set the object card to None."""
        self.deck = None
