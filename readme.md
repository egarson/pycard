# Python Code Sample

## Background

I wrote this for a prospective employer as a simple example of object-oriented code. Because I don't publish enough code as it stands, I thought I would push it here. Use it for what you will, but don't blame me if it sets your hair on fire.

## Introduction

Hello and welcome to my Python code sample, in which I implement a set of simple classes that could be used as the basis to create a card game.

## Controversy

I view unit tests as the primary means to document implementation code. So, there is what some might regard a dearth of comments in the code. I believe that good code should be self-documenting, and if it is not then it needs to be refactored. By 'self-documenting', I mean that the nomenclature of the code (e.g. variable and method names) should be sufficiently intuitive so as to readily elicit understanding. That said, I do favor terse code, but not at the expense of readability.

I don't like for loops: each time one is written, God kills a kitten. Kidding aside, I used classes/oo because I was asked to. Without that constraint, I would likely have written this in a more functional style, i.e. using largely side-effect free functions. That approach would also employ much simpler representations of the domain entities, such as using a tuple for Card semantics, and a list thereof for both Hand and Deck semantics. I say 'semantics' because it is helpful in the functional style to forget nouns and to execute "in the kingdom of verbs".

## Constraints

* the files are utf-8 encoded so we can use pretty Card symbols (and, they sure look cool in a unicode-aware REPL!)

## Design Notes

"Programs should be written for people to read, and only incidentally for machines to execute."
  -- Structure and Interpretation of Computer Programs

core.py has two distinct interfaces: one for computers (processing) and one for humans (interacting). Scalars are used for the former, and chars for the latter. In this respect, core.py really just manipulates sets of numbers; and while this is true of many programs, when you can explicitly model the domain that way, it can help to create simple and elegant code.

API usability is important to me, so I absorb some complexity in core.py in order to afford the easier-to-use programmatic interface in test_core.py.

RANKS is 1-based, because the sequence "A, 2, 3,..." has no '1': it's better to be contiguous and suffer having to decrement by 1 in places. If we designed otherwise we might be guilty of a "foolish consistency".

## Todo

* an aces_high convenience method to change the value of ACE from 1 to max(RANKS)+1, as this is so common
* Hand.__cmp__()
* turn-based game play

## Sundry Comments

* This code was developed on Ubuntu linux 2.6.38-11 using Python 2.7.1+ and git 1.7.4.1
* I would be grateful to learn ways I might improve on this (albeit small) program should you have any suggestions
* I have left quite a lot out of this short exercise and would be happy to expand further on any aspect thereof

## Conclusion

Thank you for any vestige of interest you may have!

Edward Garson
September 2011
