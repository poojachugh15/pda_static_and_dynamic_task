import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.ace = Card("hearts", 1)
        self.card1 = Card("hearts", 5)
        self.card2 = Card("hearts", 6)
        self.cards = [self.ace, self.card1, self.card2]
        self.game  = CardGame()
            
    def test_check_for_Ace(self):
        self.assertTrue(self.game.check_for_ace(self.ace))
        self.assertFalse(self.game.check_for_ace(self.card1))
        
    def test_highest_card(self):
        self.highest_card = self.game.highest_card(self.card1, self.card2)
        self.assertEqual(self.highest_card.value, 6)
        
        self.hightest_card = self.game.highest_card(self.card2, self.card1)
        self.assertEqual(self.hightest_card.value, 6)
        
    def test_cards_total(self):
        self.assertEqual(self.game.cards_total(self.cards),"You have a total of 12")
