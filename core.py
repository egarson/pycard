# -*- coding: utf-8 -*-
from nose.tools import *

CLUBS, DIAMONDS, HEARTS, SPADES = 0, 1, 2, 3
SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]
Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits_chars = ['♣', '♦', '♥', '♠']

ACE, JACK, QUEEN, KING = 1, 11, 12, 13 # sic
RANKS = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]
Ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack','Queen', 'King']
ranks_chars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', '♛', '♚']

def test_define_deck():
    deck = Deck()
    eq_(52, len(set(deck.cards))) # usage of set ensures no dupes
    eq_(52, len(deck)) # tests __len__() - not the same as above
    # check that we have 13 per suit & 4 per rank
    map(lambda suit: eq_(13, len(filter(lambda card: card.suit == suit, deck.cards))), SUITS)
    map(lambda rank: eq_(4, len(filter(lambda card: card.rank == rank, deck.cards))), RANKS)

def test_deck_order():
    deck = Deck()
    eq_('Ace of Clubs', str(deck.cards[0])) # lowest card tests
    eq_((0,1), (deck.cards[0].suit, deck.cards[0].rank)) # yuk
    eq_((0,1), (deck.first_card.suit, deck.first_card.rank)) # ok, better
    eq_('King of Spades', str(deck.cards[len(deck)-1])) # highest card tests
    eq_((3,13), (deck.cards[len(deck)-1].suit, deck.cards[len(deck)-1].rank))
    eq_((3,13), (deck.last_card.suit, deck.last_card.rank))

class Card():
    def __init__(self,suit,rank):
        self.suit, self.rank = suit, rank

    def __str__(self):
        return '%s of %s' % (Ranks[self.rank-1],Suits[self.suit])

class Deck():
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        self.__dict__['first_card'] = self.cards[0]
        self.__dict__['last_card'] = self.cards[len(self)-1]

    def __len__(self):
        return len(self.cards)

