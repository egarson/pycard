# Python Code Sample

## Background

I wrote this for a prospective employer as a coding exercise. You may use it for what you will, but don't blame me if it sets your hair on fire.

## Introduction

This is a simple object-oriented Python code sample which uses playing cards as the domain. It could used as the basis to create a card game.

## Functionality

There are Deck, Card and Hand base classes and a PokerEvaluator which can categorize PokerHands. No game play has been implemented.

## Controversy

I view unit tests as the primary means to document implementation code. So there is what some might regard a dearth of comments in the code. Good code should be self-documenting, and if it isn't then it needs to be refactored. By 'self-documenting', I mean that the nomenclature and flow should be sufficiently intuitive so as to readily elicit understanding. I favor terse code, but not at the expense of readability.

I don't like for loops, because each time one is written, God kills a kitten. Kidding aside, I used classes/OO because I was asked to. Without that constraint, I would likely have written this in a more functional style, i.e. using largely side-effect free methods with pass-through data. That approach would also employ simpler representations of the domain entities, such as using a tuple for Card semantics, and a list thereof for both Hand and Deck semantics. I say 'semantics' because it is helpful in the functional style to forget nouns and to execute "in the kingdom of verbs".

## Constraints

* the files are utf-8 encoded to enable using pretty Card symbols (they sure look cool in a unicode-aware REPL!)

## Design Notes

"Programs should be written for people to read, and only incidentally for machines to execute."
  -- Structure and Interpretation of Computer Programs

core.py has two distinct interfaces: one for computers (processing) and one for humans (reasoning and interacting). Scalars are used for the former, and chars/strings for the latter. In this respect, core.py really just manipulates sets of numbers; and while this is true of many programs, when you can explicitly model the domain that way, it can help to create simple and elegant code.

API usability is important to me, so I absorb some complexity in core.py in order to provide an easier-to-use programmatic interface (as in test_core.py).

## Todo

* an aces_high convenience method to change the value of ACE from 1 to max(RANKS)+1, as this is so common in card games
* Hand.__cmp__()
* turn-based game play

## Sundry Comments

* This code was developed on Ubuntu linux 2.6.38-11 using Python 2.7.1+ and git 1.7.4.1
* I would be grateful to learn ways I might improve on this (albeit small) program should you have any suggestions
* I have left quite a lot out of this short exercise and would be happy to expand further on any aspect thereof

## License

Copyright (C) 2011 Edward Garson.

This code is released under the terms of the MIT license as described by the included file MIT-LICENSE.txt.

## Conclusion

Thank you for your interest.

Edward Garson

September 2011
