#!/usr/bin/env python
from utils import memoize

"""
Basic idea: encode state of the crossings as an integer. E.g. '0' means:

--|--
--|--
  |  
  |  

We have two states '4' and '5' which both encode this crossing:

--|--
--|--
--|--
--|--

This is because the way the path can be "closed off" to the right depends on
whether it was "closed off" at the center on the left. E.g. we can't have this:
________
  ____
 [____]
________

Similarly, regardless of whether it's closed off on top or bottom on left side,
it can only be closed off in the center on the right side, else we can't make a
valid path.

I already showed 0, 5, and 6. The rest of the states or given for the sake of completeness:

1:
  |  
  |  
--|--
--|--

2:
  |  
--|--
--|--
  |  

3:
--|--
  |  
  |  
--|--

Note that states like this are not possible:
  |  
--|--
  |  
--|--
since they can't result in a valid path.

A valid path starts in state 3 and ends in either state 3 or state 5. If it ends in state
5, it is because state 5 is the only state that can be closed off on the right like this:
____
____]
____
____]

Actually calculating the number of paths is thus just a matter of state-mindful divide-and-conquer.
"""

valid = set([(0,3),(3,0),(1,3),(3,1),(2,3),(3,2),(0,4),(1,4),(4,4),(4,3),(3,5),(5,5),(5,0),(5,1)])

mod = 10**8

@memoize
def T(begin, end, n):
    if n==1: return (begin, end) in valid
    ret = 0
    for i in xrange(6):
        ret += T(begin, i, n//2)*T(i,end,(n+1)//2)%mod
    return ret%mod

N=10**12
print (T(3,3,N-1) + T(3,5,N-1))%mod # N squares in length means N-1 crossings
