#!/usr/bin/env python
import sys
from collections import defaultdict, Counter

N=int(sys.argv[1])
NPoints = (N+1)*(N+1)
P = 1./(N+1)

def ccw(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def encloses(a,b,c,d):
    return ccw(b,c,a)*ccw(b,c,d) > 0 and ccw(b,a,c)*ccw(b,a,d) > 0

def points(start=(0,-1)):
    for i in xrange(start[0], N+1):
        for j in xrange(start[1]+1 if i==start[0] else 0, N+1):
            yield (i,j)

def get_canonical_line(a,b):
    """
    Returns an interned line containing a --> b
    """
    # TODO: impl me for more cases than N==1
    return tuple(sorted([a,b]))

def collinear(a,b,c):
    """
    Return true iff a, b, and c lie on same line
    """
    # TODO: more efficient way to impl this?
    # return get_canonical_line(a,b) == get_canonical_line(b,c)
    # TODO: is it correct?
    return ccw(a,b,c)==0

p_border = Counter()
p_interior = Counter()
p_border_given_zero_area = Counter()
# p_interior_given_zero_area = 0 :)

lines = defaultdict(set)
lines_through = defaultdict(set)

def gather_collinear():
    for a in points():
        for b in points(a):
            line = get_canonical_line(a,b)
            lines[line].add(a)
            lines[line].add(b)

p_zero_area = (1-P)**NPoints + NPoints*P*(1-P)**(NPoints-1)
for line, pointset in lines.iteritems():
    for point in pointset:
        lines_through[point].add(line)
    # next, count # probability of selecting >=2 two points from each line
    k = len(pointset)
    # all others not picked, at least 2 points on the line picked
    p_line = (1-P)**(NPoints - k) * (1. - k*P*(1-P)**(k-1) - (1-P)**k)
    p_zero_area += p_line

for b in points():
    p_border_given_zero_area[b] = P*(1-P)**(NPoints-1)
    for line in lines_through[b]:
        k = len(lines[line])
        p_border_given_zero_area[b] += P*(1-P)**(NPoints-k) * (1-(1-P)**(k-1))
    p_border_given_zero_area[b] /= p_zero_area

for b in points():
    p_border[b] = P*(1-P)**(NPoints-1)
    for a in points():
        if a==b: continue
        positive = 0
        negative = 0
        zero = 0
        for d in points():
            if d==b or d==a: continue
            direction = ccw(b,a,d)
            if direction < 0: negative += 1
            elif direction > 0: positive += 1
            else: zero += 1
        if positive>0 and negative>0:
            p_border[b] += P**2 * ((1-P)**(negative+zero) + (1-P)**(positive+zero))
            # need to subtract off double counted case of nothing picked
            p_border[b] -= P**2 * (1-P)**(positive+negative+zero)
        else:
            p_border[b] += P**2
        for c in points(a):
            # TODO: handle case (a,b,c) collinear
            if c==b or c==a: continue
            positive = 0
            negative = 0
            for d in points():
                if d==b or d==a or d==c: continue
                if encloses(a,b,c,d): positive += 1
                else: negative += 1
            p_border[b] -= P**3 * (1-P)**negative
    # P*(1 - p_border_given_b_selected) == P*(1 - p_border[b]/P)
    p_interior[b] = P - p_border[b]

#print [p_border[b] for b in points()]
#print [p_interior[b] for b in points()]
#print [p_border_given_zero_area[b] for b in points()]
#print p_zero_area

ans = sum(.5*p_border[b] + p_interior[b] for b in points()) - 1
ans -= (sum(.5*p_border_given_zero_area[b] for b in points()) - 1)*p_zero_area
print '%.5f' % ans

# Conditioning on zero area, denominator is p_zero_area.
# We can then compute the probability that a given point b is a border point
# in the collinear or singleton case by conditioning on each of the lines containing it
# being the only line (as well as the case that it is a singleton). For the first case,
# we can figure this out by noting that if a line goes through k points, then there are
# 2**(k-1) - 1 ways to form a line that contains b (all subsets of the other k-1 points
# excluding the empty subset).
# TODO: code this

# Next, to get pborder for each point, we need to compute:
# \sum_a \sum_c p(border | line with a) * p(line with a) + p(border | line with c) * p(line with c) 
#               - p(border | lines with a and c) * p(lines with a and c)

# Note that the events that b is a border point forming lines with a, and c
# are pairwise disjoint across the set of (a,c), since there's only one border.
# Thus we don't need to expand out the inclusion-exclusion further.

# Also, note that we are conditioning on the point in question being selected in all cases.
# Thus, the conditional on b being selected, the prob that it is an interior point
# will be 1 - pborder. Multiply both by  1./(N+1) to recover unconditional probs.

# Some edge cases:
# 1) How to handle points collinear with b and a (or b and c)? Ans: they must not be picked
#    (forces this event to be disjoint from another event considered where a or c is chosen
#    to be one of said collinear points).
# 2) What if a, b, and c are collinear? In this case, we need to consider both the case that
#    there are only points to the right, as well as points only to the left, similar to the
#    single-edge case of just b and a or just b and c. We (effectively) split into three sets
#    for ccw(a,b,d) for other points d: {positive}, {zero}, and {negative}, then handle both cases.

# Finally, compute the answer as E[.5*\sum_i B_i + \sum_i I_i - 1]
#                              - E[.5*\sum_i B_i - 1 | zero area]*P(zero area)
