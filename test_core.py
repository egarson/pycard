#!/usr/bin/env python
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
    eq_((ACE,CLUBS), (deck.top_card().rank, deck.top_card().suit))
    eq_('King of Spades', str(deck[len(deck)-1])) # highest card accessors
    eq_((KING,SPADES), (deck[len(deck)-1].rank, deck[len(deck)-1].suit))
    eq_((KING,SPADES), (deck.bottom_card().rank, deck.bottom_card().suit))

def test_card_basics():
    c = Card('2', 'Diamonds')
    eq_(2, c.rank)
    eq_(DIAMONDS, c.suit)

def test_card_rank_low():
    c = Card('Ace', 'Clubs')
    eq_(ACE, c.rank)
    eq_(CLUBS, c.suit)

def test_card_rank_high():
    c = Card('♚', '♠')
    eq_(KING, c.rank)
    eq_(SPADES, c.suit)

def test_card_shortcut_constructor():
    c = Card('J♦')
    eq_(JACK, c.rank)
    eq_(DIAMONDS, c.suit)

@raises(CardException)
def test_card_bad_rank():
    Card('blah', 'Spades')

@raises(CardException)
def test_card_bad_rank_char():
    Card('♥', 'blah')

@raises(CardException)
def test_card_bad_suit():
    Card('Ace', 'rubbish')

@raises(CardException)
def test_card_bad_suit_char():
    Card('A', 'X')

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

def test_shuffle():
    d1,d2 = Deck(),Deck()
    is_zero = lambda x: True if x == 0 else False
    compare = lambda card,other: cmp(card,other)
    # Expected: a 52-element array of zeros [0,0,0...] when doing a
    # pair-wise comparison of d1 with d2 prior to shuffle
    eq_(52, len(filter(is_zero, map(compare, d1.cards, d2.cards))))
    d1.shuffle()
    # d1.shuffle will return same order 1 in 8*10^67 test runs (source:
    # http://en.wikipedia.org/wiki/Shuffling) - lol, i can live with this
    ok_(52 != len(filter(is_zero, map(compare, d1.cards, d2.cards))))

def test_take_one():
    d = Deck()
    top_card = d.top_card()
    taken = d.take(1)
    ok_(51, len(d.cards))
    eq_(top_card, taken[0])

def test_take_two():
    d = Deck()
    top_card = d.top_card()
    taken = d.take(2)
    ok_(50, len(d.cards))
    eq_(top_card, taken[0])

def test_deal():
    d = Deck()
    original_cards = list(d.cards)
    hands = d.deal(hands=5,cards=5)
    ok_(len(hands) == 5)
    eq_(52 - 5 * 5, len(d.cards))

def test_deal_no_shuffle():
    d = Deck()
    [hand] = d.deal(1,1,shuffle=False)
    eq_(hand[0], Card('Ace','Clubs'))
    eq_(d.top_card(), Card('Ace', 'Diamonds'))

def test_hand_str():
    d = Deck()
    [hand] = d.deal(1,4,shuffle=False)
    eq_(str(hand), "[AC AD AH AS]")

def test_hand_unicode():
    d = Deck()
    [hand] = d.deal(1,4,shuffle=False)
    u1 = unicode(hand)
    u2 = u"[A♣, A♦, A♥, A♠]"
    eq_(u1, u2)

def test_hand_len():
    d = Deck()
    [hand] = d.deal(1,4,shuffle=False)
    eq_(4, len(hand))

def test_hand_ranking():
    winning_hand = Hand([Card('Ace', 'Spades'), Card('Ace', 'Hearts')])
    losing_hand =  Hand([Card('Ace', 'Diamonds'), Card('2', 'Spades')])
    ok_(winning_hand > losing_hand)

