Code Submission
===============
Hello and welcome to my code submission, in which I was asked to implement a set of classes for playing cards in the programming language of my choice.

Evaluation
----------
When evaluating code, it can be a boon to have some visibility into the process by which the programmer arrived at his/her solution, as opposed to only seeing the final result. I thought it would be interesting to provide this level visibility to you, so I employed git, frequently committed code, and didn't rewrite history except for the purpose of correcting speling errors and such ;-).

Controversy
-----------
I view unit tests as the primary means to document implementation code. So, you will find what some might regard a dearth of comments in the code. I believe that good code should be self-documenting, and if it is not then it needs to be refactored. By 'self-documenting', I mean that the nomenclature of the code (e.g. variable and method names) should be sufficiently intuitive so as to readily elicit understanding. That said, I do favor terse code, but not at the expense of readability.

I don't like for loops: each time one is written, God kills a kitten. Kidding aside, I used classes/oo because I was asked to. Without that constraint, I would likely have written this in a more functional style, i.e. using largely side-effect free functions. That approach would also employ much simpler representations of the domain entities, such as using a tuple for Card semantics, and a list thereof for both Hand and Deck semantics. I say 'semantics' because it is helpful in the functional style to forget nouns and to execute "in the kingdom of verbs".

Assumptions
-----------
I assume that the following is acceptable:

* employing utf-8 file encoding to be able to use pretty Card symbols (they sure look cool in a unicode-aware REPL!)
* using google/irc to get help with small issues (as I did to resolve e.g. a unicode-related printing conundrum)

Design Notes
------------
"Programs should be written for people to read, and only incidentally for machines to execute."
  -- Structure and Interpretation of Computer Programs

I conceptualize core.py as having two distinct interfaces: one for computers (processing) and one for humans (interacting). Scalars are used for the former, and chars for the latter. In this regard, core.py really just manipulates sets of numbers. Which is true of many programs, but when you can model the domain that way, it can help to create simple and elegant code.

* I think API usability is important, so I'm happy to absorb a bit of complexity to present an easier-to-use programmatic interface.

* RANKS is 1-based, because the sequence "A, 2, 3,..." has no '1': it's better to be contiguous and suffer having to decrement by 1 in places. If we designed otherwise we might be guilty of a "foolish consistency".

I would/will have added the following at some point:

* an aces_high convenience method to change the value of ACE from 1 to max(RANKS)+1, as this is so common
* Hand.__cmp__()
* turn-based game play

Sundry Comments
---------------
* This code was developed on Ubuntu linux 2.6.38-11 using Python 2.7.1+ and git 1.7.4.1
* I would be grateful to learn ways I might improve on this (albeit small) program should you have any suggestions
* I have left quite a lot out of this short exercise and would be happy to expand further on any aspect thereof

Conclusion
----------
Thank you for considering my submission.

Edward Garson
September 2011
