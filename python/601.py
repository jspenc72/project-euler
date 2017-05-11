#!/usr/bin/env python
from utils import lcm

"""
It's easier to just write out the following than explain it:

'00000000000"0000000000000000000000000000000000000000000000
1'10101010101"101010101010101010101010101010101010101010101
12'12012012012"12012012012012012012012012012012012012012012
123'12301230123"1230123012301230123012301230123012301230123
1234'123401234012340123401234012340123401234012340123401234

We are looking for diagonals of 0s that are interrupted after
a duration -- e.g. for P(3,N) the double quotes represent a
diagonal of 0s that are interrupted after a streak of 3. These
happen every lcm(1,2,3) entries, but the interruption will NOT
happen at multiples of lcm(1,2,3,4), so we need to be sure to
subtract this off.
"""

def P(s,N):
    g=1
    for i in xrange(2,s+1):
        g = lcm(g,i)
    gp = lcm(g,s+1)
    return (N+g-2)//g - (N+gp-2)//gp

print sum(P(i,4**i) for i in xrange(1,32))
