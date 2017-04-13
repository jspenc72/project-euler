#!/usr/bin/env python
import itertools

"""
Simple enough idea: since doesn't matter in what order the moves are executed
as it will be the same # of moves every time (exercise: prove this!), we can
always pick the leftmost slot with >=2 beans. We can collapse multiple moves
into one by moving "holes" to the right instead of moving beans to the left.
Just need some bookkeeping to keep track of the holes and beans, as well as the
number of moves needed to move a hole to the right a given number of times.
"""

fromleft = 0
N=1500
tprev = 123456
def getamount(i, fromleft=0):
    global tprev
    ret = fromleft
    if i<=N:
        if tprev&1:
            tprev = (tprev//2) ^ 926252
        else:
            tprev //= 2
        ret += (tprev % 2**11)+1
    return ret

ans=0
fromleft=0
holes=[0]
for i in itertools.count(1):
    bi = getamount(i, fromleft)
    if bi <= 1: break
    fromleft=0
    holes = map(lambda x:x+1, holes)
    while bi > 1:
        if len(holes)==1:
            holes.append(holes[0]+1)
        if holes[0]==bi:
            # interestingly enough, this never happens, but I think we would need
            # this special case for correctness if it did happen. otherwise, maybe
            # we could end with a negative final amount in this slot.
            tmove = bi-1
        else:
            tomove = min(holes[0], bi)
        fromleft += tomove
        bi -= tomove
        upper = holes[0]
        lower = holes[0]-tomove
        ans += upper*(upper+1)//2 - lower*(lower+1)//2
        holes[0] -= tomove
        if holes[0] == 0:
            bi -= 1
            holes = holes[1:]
    if bi==0:
        holes = [0] + holes

print ans
