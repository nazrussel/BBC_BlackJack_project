import unittest
from card import Card


class CardTestCase(unittest.TestCase):
    """Unit test for Card class"""

    def setUp(self):
        self.card = Card("♥", "3")

    def test_card_validity(self):
        """only valid card can be created"""
        with self.assertRaises(AssertionError):
            self.card = Card("♥", "13")
        with self.assertRaises(AssertionError):
            self.card = Card("x", "13")

    def test_card_toString(self):
        """Is card console representation correct?"""
        self.assertEqual(str(self.card), "3 of ♥")

    def tearDown(self):
        """set the object card to None."""
        self.card = None


if __name__ == '__main__':
    unittest.main()
