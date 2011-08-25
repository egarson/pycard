# -*- coding: utf-8 -*-
from core import *

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

def test_card_basics():
    c = Card(rank='2', suit='Diamonds')
    eq_(2, c.rank)
    eq_(SUITS[DIAMONDS], c.suit)

def test_card_char_constructor():
    c = Card(rank='J', suit='♦') # Jack of Diamonds
    eq_(JACK, RANKS[c.rank])

@raises(CardException)
def test_card_bad_rank():
    Card('blah', 'Spades')

@raises(CardException)
def test_card_bad_suit():
    Card('Ace', 'rubbish')

def test_card_kwargs():
    Card(suit='Spades', rank='Ace')
    Card(rank='Jack', suit='Clubs')

