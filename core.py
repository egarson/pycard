from nose.tools import *

SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def test_define_deck():
    cards = [(rank,suit) for rank in RANKS for suit in SUITS]
    eq_(52, len(set(cards))) # kill 2 birds: assert len && ensure no dupes
