# -*- coding: utf-8 -*-
from nose.tools import *

CLUBS,DIAMONDS,HEARTS,SPADES = 0,1,2,3
SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]
Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits_chars = ['♣', '♦', '♥', '♠']

ACE, JACK, QUEEN, KING = 1,11,12,13 # sic
RANKS = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]
Ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack','Queen', 'King']
ranks_chars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', '♛', '♚']

def test_define_deck():
    deck = Deck()
    eq_(52, len(set(deck.cards))) # usage of set ensures no dupes
    eq_(13, len(filter(lambda card: card.suit == DIAMONDS, deck.cards))) # sanity checks
    eq_(13, len(filter(lambda card: card.suit == CLUBS, deck.cards)))
    eq_(13, len(filter(lambda card: card.suit == SPADES, deck.cards)))
    eq_(13, len(filter(lambda card: card.suit == HEARTS, deck.cards)))
    eq_('Ace of Clubs', str(deck.cards[0])) # lowest card
    eq_('King of Spades', str(deck.cards[len(deck)-1])) # highest card

class Card():
    def __init__(self,suit,rank):
        self.suit, self.rank = suit, rank

    def __str__(self):
        return '%s of %s' % (Ranks[self.rank-1],Suits[self.suit])

class Deck():
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]

    def __len__(self):
        return len(self.cards)
