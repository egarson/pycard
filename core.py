#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nose.tools import *
from random import shuffle
from collections import Counter

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
    def __init__(self, *args):
        if len(args) == 2: # eg Card('Ace', 'Spades')
            [rank, suit] = map(lambda a: unicode(a.strip(), 'utf8'), args)
            self.rank, self.suit = self.parse_rank(rank), self.parse_suit(suit)
        elif len(args) == 1:  # eg Card('A♦')
            uni = unicode(args[0].strip(), 'utf8')
            rank_len = 1 if uni[:2] != '10' else 2 # cater to oddball 2-char rank '10'
            self.rank = self.parse_rank(uni[:rank_len])
            self.suit = self.parse_suit(uni[rank_len:])
        else:
            raise TypeError('Unsupported constructor argument(s): %s' % args)

    def __parse__(self, arg, Arr, ARR, chars):
        if arg in Arr:
            return ARR[Arr.index(arg)] # eg 'King', 'Clubs'
        elif arg in chars:
            return ARR[chars.index(arg)] # eg '♚', '♣'
        else:
            raise CardException('Bad rank or suit: "%s"' % unicode(arg))

    def parse_rank(self, rank):
        return self.__parse__(rank, Ranks, RANKS, ranks_chars)

    def parse_suit(self, suit):
        return self.__parse__(suit, Suits, SUITS, suits_symbols)

    def __str__(self):
        return '%s of %s' % (Ranks[self.rank-1], Suits[self.suit])

    def __unicode__(self):
        return u"%s%s" % (ranks_chars[self.rank-1], suits_symbols[self.suit])

    def __hash__(self):
        return 19 * self.rank + 17 * self.suit

    def __cmp__(self, other):
        if self.suit != other.suit:
            return 1 if self.suit > other.suit else -1
        elif self.rank != other.rank:
            return 1 if self.rank > other.rank else -1
        return 0

HIGH_CARDS, ONE_PAIR, TWO_PAIRS, THREE_OF_KIND, STRAIGHT = 0, 1, 2, 3, 4
FLUSH, FULL_HOUSE, FOUR_OF_KIND, STRAIGHT_FLUSH = 5, 6, 7, 8

class PokerEvaluator():

    @classmethod
    def evaluate(self, hand, other):
        return cmp(self.category(hand), self.category(other))

    @classmethod
    def category(self, hand):
        # eg {ACE:2, 4:1} = Counter([A♠ 4♦ A♥])
        card_count_map = Counter([card.rank for card in hand.cards])
        card_count_map.keys().sort()
        card_with_highest_count = max(card_count_map, key=lambda e: card_count_map[e])
        high_card_count = card_count_map[card_with_highest_count]
        if high_card_count == 1: # can only be HIGH_CARDS, STRAIGHT, FLUSH or STRAIGHT_FLUSH
            # eg [2,2,2,2,2] = [2,3,4,5,6] - [0,1,2,3,4]
            rank_diffs = map(lambda k,r: k-r, card_count_map.keys(), range(0,len(hand)))
            contiguous_values = all(diff == rank_diffs[0] for diff in rank_diffs)
            all_same_suit = all(card.suit == hand[0].suit for card in hand.cards)
            if contiguous_values: # STRAIGHT or STRAIGHT_FLUSH if all same diffs
                return STRAIGHT if not all_same_suit else STRAIGHT_FLUSH
            else:
                return FLUSH if all_same_suit else HIGH_CARDS
        elif high_card_count == 2: # can only be ONE_ or TWO_ pairs
            # automagically return ONE_ or TWO_ pairs as count coincides with category value
            return reduce(lambda x,y: x+1 if y==2 else x, card_count_map.values(), 0)
        elif high_card_count == 3: # can only be THREE_OF_KIND or FULL_HOUSE
            has_no_pair = all(val != 2 for val in card_count_map.values())
            return THREE_OF_KIND if has_no_pair else FULL_HOUSE
        elif high_card_count == 4:
            return FOUR_OF_KIND

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
        return u"[%s]" % u", ".join(unicode(card) for card in self.cards)

    def __cmp__(self, other):
        return PokerEvaluator.evaluate(self, other)

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
