import unittest
from hand import *
from card import Card


class HandTestCase(unittest.TestCase):
    """Unit tests for Hand class"""

    def setUp(self):
        self.hand = Hand()
        self.deck = Deck()

    def test_a_card_get_added(self):
        """Does a new card dealt to the hand?"""
        card = Card("♠", "4")
        num_before = len(self.hand.cards)
        self.hand.add_card(card)
        num_after = len(self.hand.cards)
        self.assertEqual(num_after, num_before + 1)
        self.assertIs(self.hand.cards[-1], card)

    def test_calculate_added_card_values(self):
        """Does the value of the hand calculate correctly"""
        card_one = Card("♦", "5")
        card_two = Card("♣", "A")
        self.hand.add_card(card_one)
        self.hand.add_card(card_two)
        self.assertEqual(self.hand.value, 16)
        card_three = Card("♠", "A")
        self.hand.add_card(card_three)
        self.assertEqual(self.hand.value, 27)

    def test_count_card_for_a_hand(self):
        """is correct number of cards distributed"""
        card_one = Card("♦", "5")
        card_two = Card("♣", "A")
        self.hand.add_card(card_one)
        self.hand.add_card(card_two)
        self.assertEqual(len(self.hand.list_of_card_values), 2)

    def test_count_aces(self):
        """Does the number of aces correctly tracked?"""
        card_one = Card("♣", "A")
        card_two = Card("♠", "A")
        self.hand.add_card(card_one)
        self.hand.add_card(card_two)
        self.assertEqual(self.hand.aces, 2)
        self.assertTrue(self.hand.aces, True)

    def test_total_values_greater_than_twenty_one(self):
        """does the dealt card total values exceed 21?"""
        card_one = Card("♣", "A")
        card_two = Card("♠", "A")
        self.hand.add_card(card_one)
        self.hand.add_card(card_two)
        self.assertGreater(self.hand.value, 21)

    def test_reduce_value_of_ace(self):
        """does the value of ace replace 1 with 11?"""
        card_one = Card("♣", "K")
        card_two = Card("♠", "A")
        card_three = Card("♠", "2")
        self.hand.add_card(card_one)
        self.hand.add_card(card_two)
        self.hand.add_card(card_three)
        self.hand.adjust_for_aces()
        self.assertEqual(self.hand.value, 13)

    def tearDown(self):
        """set the object card to None."""
        self.hand = None
