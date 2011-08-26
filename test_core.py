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
    eq_('Ace of Clubs', str(deck[0])) # lowest card accessors
    eq_((ACE,CLUBS), (deck[0].rank, deck[0].suit))
    eq_((ACE,CLUBS), (deck.first_card.rank, deck.first_card.suit))
    eq_('King of Spades', str(deck[len(deck)-1])) # highest card accessors
    eq_((KING,SPADES), (deck[len(deck)-1].rank, deck[len(deck)-1].suit))
    eq_((KING,SPADES), (deck.last_card.rank, deck.last_card.suit))

def test_card_rank():
    c = Card(rank='2', suit='Diamonds')
    eq_(2, c.rank)
    eq_(SUITS[DIAMONDS], c.suit)

def test_card_rank_low():
    c = Card(rank='Ace', suit='Clubs')
    eq_(ACE, c.rank)
    eq_(CLUBS, c.suit)

def test_card_rank_high():
    c = Card('♚','♠')
    eq_(KING, c.rank)
    eq_(SPADES, c.suit)

def test_card_char_constructor():
    c = Card(rank='J', suit='♦') # Jack of Diamonds
    eq_(JACK, c.rank)

def test_card_kwargs():
    Card(suit='Spades', rank='Ace')
    Card(rank='Jack', suit='Clubs')

@raises(CardException)
def test_card_bad_rank():
    Card('blah', 'Spades')

@raises(CardException)
def test_card_bad_rank_char():
    Card(suit='♥', rank='blah')

@raises(CardException)
def test_card_bad_suit():
    Card('Ace', 'rubbish')

@raises(CardException)
def test_card_bad_suit_char():
    Card(rank='A', suit='X')

def test_compare_suits_basic():
    # default Spades > Hearts > Diamonds > Clubs
    ace_of_spades = Card('Ace', 'Spades')
    king_of_hearts = Card('King', 'Hearts')
    ok_(ace_of_spades > king_of_hearts) # lowest Spade should be highest Heart...
    ace_of_hearts = Card('Ace', 'Hearts')
    king_of_diamonds = Card('King', 'Diamonds')
    ok_(ace_of_hearts > king_of_diamonds) # ...and so forth
    ace_of_diamonds = Card('Ace', 'Diamonds')
    king_of_clubs = Card('King', 'Clubs')
    ok_(ace_of_diamonds > king_of_clubs)

def test_card_equality_reflexive(): # a == a' -> simplest case; sanity check really
    eq_(Card('5', 'Diamonds'), Card('5', 'Diamonds'))
    five_of_diamonds = Card('5', 'Diamonds')
    eq_(Card('5', 'Diamonds'), five_of_diamonds)
    eq_(five_of_diamonds, Card('5', 'Diamonds'))

def test_cards_not_equal_reflexive(): # a == b -> b == a
    ok_(Card('5', 'Diamonds') != Card('4', 'Diamonds'))
    ok_(Card('4', 'Hearts') != Card('4', 'Diamonds'))
    five_of_diamonds = Card('5', 'Diamonds')
    four_of_diamonds = Card('4', 'Diamonds')
    ok_(five_of_diamonds != four_of_diamonds)
    ok_(four_of_diamonds != five_of_diamonds)

def test_card_equality_transitive(): # a == b and a == c -> b == c
    five_of_diamonds = Card('5', 'Diamonds')
    other_five_of_diamonds = Card('5', 'Diamonds')
    eq_(five_of_diamonds, other_five_of_diamonds)
    eq_(five_of_diamonds, Card('5', 'Diamonds'))
    eq_(Card('5', 'Diamonds'), five_of_diamonds)
    eq_(Card('5', 'Diamonds'), other_five_of_diamonds)

def test_card_cmp():
    five_of_diamonds = Card('5', 'Diamonds')
    four_of_diamonds = Card('4', 'Diamonds')
    eq_(1, cmp(five_of_diamonds, four_of_diamonds))
    eq_(-1, cmp(four_of_diamonds, five_of_diamonds))
    eq_(0, cmp(five_of_diamonds, five_of_diamonds))
    eq_(0, cmp(five_of_diamonds, Card('5', 'Diamonds')))
    five_of_hearts = Card('5', 'Hearts')
    eq_(1, cmp(five_of_hearts, five_of_diamonds)) # Hearts > Diamonds

def test_all_cards_greater_than():
    largest_card = lambda card,other: card if card > other else other
    eq_(Card('King','Spades'), reduce(largest_card, Deck().cards))

def test_all_cards_less_than():
    smallest_card = lambda card,other: card if card < other else other
    eq_(Card('Ace', 'Clubs'), reduce(smallest_card, Deck().cards))


