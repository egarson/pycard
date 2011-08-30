#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nose.tools import *
from random import shuffle

ACE, JACK, QUEEN, KING = 1, 11, 12, 13 # sic
RANKS = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]
Ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack','Queen', 'King']
ranks_chars = [u'A', u'2', u'3', u'4', u'5', u'6',
               u'7', u'8', u'9', u'10', u'J', u'♛', u'♚']

CLUBS, DIAMONDS, HEARTS, SPADES = 0, 1, 2, 3
SUITS = [CLUBS, DIAMONDS, HEARTS, SPADES]
Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits_symbols = [u'♣', u'♦', u'♥', u'♠']

class CardException(Exception): pass

class Card():
    def __init__(self,rank,suit):
        if rank in Ranks:
            rank = RANKS[Ranks.index(rank)] # eg 'King'
        elif rank in ranks_chars:
            rank = RANKS[ranks_chars.index(rank)] # eg u'♚'
        else:
            raise CardException('Bad rank "%s"' % rank)

        if suit in Suits:
            suit = SUITS[Suits.index(suit)] # eg 'Clubs'
        elif suit in suits_symbols:
            suit = SUITS[suits_symbols.index(suit)] # eg u'♣'
        else:
            raise CardException('Bad suit "%s"' % suit)

        self.rank, self.suit = rank, suit

    def __str__(self):
        return '%s of %s' % (Ranks[self.rank-1], Suits[self.suit])

    def __unicode__(self):
        return u"%s%s" % (ranks_chars[self.rank-1], suits_symbols[self.suit])

    def __hash__(self):
        return 19 * self.rank + 17 * self.suit

    def __cmp__(self, other):
        if self.suit > other.suit:
            return 1
        elif self.suit < other.suit:
            return -1
        elif self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            return 0 # rank and suit are same

class Hand():
    def __init__(self, cards):
        self.cards = cards

    def __getitem__(self,index):
        return self.cards[index]

    def __str__(self):
        card_str = lambda c: '%s%s' % (Ranks[c.rank-1][:1], Suits[c.suit][:1])
        return '[%s]' % " ".join(card_str(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)

    def __unicode__(self):
        # had to hit irc up for this one...
        return u"[%s]" % u", ".join(unicode(card) for card in self.cards)

    def __cmp__(self, other):
        return -1

class Deck():
    def __init__(self):
        self.cards = [Card(rank,suit) for rank in Ranks for suit in Suits]

    def top_card(self):
        return self.cards[0]

    def bottom_card(self):
        return self.cards[len(self)-1]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self,index):
        return self.cards[index]

    def take(self, count):
        result = self.cards[:count]
        self.cards[:count] = []
        return result

    def deal(self, hands, cards, shuffle=True):
        self.shuffle() if shuffle else False # don't burden clients
        return [Hand(self.take(cards)) for r in range(hands)]

    def shuffle(self):
        shuffle(self.cards)
