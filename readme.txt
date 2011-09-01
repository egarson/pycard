utf-8 ok
aces_high method
would have prefered adding a method to e.g. SPADES (a scalar) but python won't let me ('immutable type')
core has two distinct interfaces, one for computers (i.e. processing), and one for humans (i.e. reasoning): ints for the former, chars for the latter
Yes, there is some overlap in *_chars decls, but it is coincidental, and besides: I'm lazy
no need to protect Deck constructor, but need to protect Card, so Card only accepts that which can be checked (i.e. strs)
RANKS is 1-based, because 'A,2,3...' has no '1'; this way, we are contiguous at the expense of having to -1 in places
Hmmm, would like to offer "...J,Q,K" in ranks_chars in addition to pretty symbols
deal() calls shuffle() so clients don't have to (or even to know that they 'must')
deal() cheats in terms of actual dealing convention/etiquette/rules, but i allow it
clients can dynamically rebind evaluate to adjust for game semantics; PokerEvaluator can also be subclassed
hit up irc for unicode printing annoyance
