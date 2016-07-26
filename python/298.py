#!/usr/bin/env python
from collections import defaultdict
from functools import wraps

# basic idea is to get the distribution of L-R at each turn
# by computing it in terms of the distribution at the next turn.
# (we compute it given larry/robin memory state, and then sum over these)
# we use some tricks to reduce the state space of each player's memory...
# namely, we pretend like larry's memory always has [0,1,2,...] so that we
# only need to track robin's. Next, for things shared between larry and robin,
# we care about the order, but for things in robin's but not larry's, the order
# of these things may as well be in sequence and starting from 5. this brings
# the total size of the state we need to track down to 438 things, which is easy.

def memoize(f):
    _f={}
    @wraps(f)
    def mem_f(*args):
        if args in _f:
            return _f[args]
        ret = f(*args)
        _f[args] = ret
        return ret
    return mem_f

MAX_STATE_SIZE=5
allseen = set()

@memoize
def transform(state, choice):
    robinstate = list(state)
    larry=0
    robin=0
    larrystate = range(len(robinstate))
    if choice in robinstate:
        robin = 1
    else:
        robinstate = [choice] + robinstate[:MAX_STATE_SIZE-1]

    if choice < len(larrystate):
        larry = 1
        larrystate = [larrystate[choice]] + larrystate[:choice] + larrystate[choice+1:]
    else:
        larrystate = [choice] + larrystate[:MAX_STATE_SIZE-1]
    mapping = {}
    for i, item in enumerate(larrystate):
        mapping[item] = i
    newstate = []
    nextind = len(larrystate)
    for item in robinstate:
        if item in mapping:
            newstate.append(mapping[item])
        else:
            newstate.append(nextind)
            nextind += 1
    newstate = tuple(newstate)
    allseen.add(newstate)
    return newstate, larry-robin

N=50
CHOICES=10

@memoize
def dist(turns_left, state):
    if turns_left==0:
        ret = defaultdict(lambda: 0.)
        ret[0] = 1.
        return ret
    statedist = defaultdict(lambda: 0.)
    for i in xrange(CHOICES):
        nextstate, turndiff = transform(state, i)
        nextdist = dist(turns_left-1, nextstate)
        # small optimization... with turns_left remaining,
        # difference can't possibly be outside [-turns_left, turns_left]
        for diff in xrange(-turns_left-1, turns_left+1):
            statedist[turndiff + diff] += nextdist[diff] / CHOICES
    return statedist


ans = 0.
for diff, prob in dist(N, ()).iteritems():
    ans += float(prob) * abs(diff)
print 'total memory states observed: ', len(allseen)
print 'answer: %.8f' % ans
