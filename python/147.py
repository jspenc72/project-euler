#!/usr/bin/env python

# I hated this one to be honest. No clever stuff,
# just lots of simple, error-prone calculation.

# Perhaps one clever fact: the number of
# subrectangles in an m by n rectangle is equal to
# m*(m+1)/2 * n*(n+1)/2

M=43
N=47

cross_hatched = [[0]*(N+1) for i in xrange(M+1)]

# number of cross hatched rectangles making use of the square between
# (0,j) and (1,j) in an m by n rectangle
def nch1(m,n,j):
    h = min(2*j+1,2*(m-1)) # min going right or down
    w = min(2*(n-j-1)+1, 2*m-h-1) # min going right from top or down from bottom
    b = min(h-1,2*(n-j-1)+1-w) # amount we can "inch upward" to make use of bottom squares
    return h*w + h*(h-1)/2 - (h-b-1)*(h-b)/2

# number of cross hatched rectangles making use of the square between
# (0,j) and (0,j+1) in an m by n rectangle
def nch2(m,n,j):
    h = min(2*(j+1),2*m-1)
    w = min(2*(n-j-1), 2*m-h)
    b = min(h-1,2*(n-j-1)-w)
    return h*w + h*(h-1)/2 - (h-b-1)*(h-b)/2

ans_non_hatched=0
for n in xrange(1,N+1):
    for m in xrange(1,min(M,n)+1):
        non_cross_hatched = m*(m+1)/2*n*(n+1)/2
        ans_non_hatched += non_cross_hatched
        if m==1: cross_hatched[m][n] = n-1
        else:
            total = cross_hatched[m-1][n]
            for j in xrange(n-1):
                total += nch1(m,n,j) + nch2(m,n,j)
            total += nch1(m,n,n-1)
            cross_hatched[m][n] = total
        if m<=N and n<=M and m!=n:
            cross_hatched[n][m] = cross_hatched[m][n]
            ans_non_hatched += non_cross_hatched

print ans_non_hatched + sum(sum(cross_hatched[i]) for i in xrange(1,M+1))
