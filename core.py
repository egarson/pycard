from nose.tools import *

SUITS = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def test_define_deck():
    deck = Deck()
    eq_(52, len(set(deck.cards))) # kill 2 birds: assert len && ensure no dupes

class Deck():
    def __init__(self):
        self.cards = [(rank,suit) for rank in RANKS for suit in SUITS]

