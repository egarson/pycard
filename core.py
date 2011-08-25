# -*- coding: utf-8 -*-
from nose.tools import *

ACE, JACK, QUEEN, KING = 1, 11, 12, 13 # sic
RANKS = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]
Ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack','Queen', 'King']
ranks_chars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', '♛', '♚']

CLUBS, DIAMONDS, HEARTS, SPADES = 0, 1, 2, 3
SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]
Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits_chars = ['♣', '♦', '♥', '♠']

class CardException(Exception): pass

class Card():
    def __init__(self,rank,suit):
        if not rank in Ranks:
            raise CardException('Bad rank "%s"' % rank)
        if not suit in Suits:
            raise CardException('Bad suit "%s"' % suit)
        self.rank, self.suit = RANKS[Ranks.index(rank)], SUITS[Suits.index(suit)]

    def __str__(self):
        return '%s of %s' % (Ranks[self.rank-1],Suits[self.suit])

class Deck():
    def __init__(self):
        self.cards = [Card(rank,suit) for rank in Ranks for suit in Suits]
        self.__dict__['first_card'] = self.cards[0]
        self.__dict__['last_card'] = self.cards[len(self)-1]

    def __len__(self):
        return len(self.cards)

