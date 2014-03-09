#!/usr/bin/env python
from copy import copy
from gmpy import mpf

D = 30
R = 50

F={}
def f(n):
    if n<=1: return 1
    if n in F: return F[n]
    F[n] = n*f(n-1)
    return F[n]
C={}
def ch(n,k):
    if (n,k) in C: return C[n,k]
    C[n,k] = f(n)/f(k)/f(n-k)
    return C[n,k]

def numadj(i,j):
    return mpf(4 - (i==0 or i==D-1) - (j==0 or j==D-1))

def solve(n):
    grid = [[[[mpf(1.0) if k==1 else mpf(0.0) for k in xrange(n)] for j in xrange(D)] for i in xrange(D)],
            [[[mpf(0.0) for k in xrange(n)] for j in xrange(D)] for i in xrange(D)]]
    sameloc = [[[mpf(0.0) for k in xrange(n)] for j in xrange(D)] for i in xrange(D)]
    adj = [[0,1], [1,0], [0,-1], [-1,0]]
    turn = False
    def prob(i,j,k,m):
        if k==4:
            if m==0: return 1.0
            else: return 0
        else:
            off_i, off_j = adj[k]
            if i+off_i<0 or i+off_i>=D or j+off_j<0 or j+off_j>=D:
                return prob(i,j,k+1,m)
            else:
                ans = 0
                for x in xrange(m+1):
                    ans += prob(i,j,k+1,m-x)*sameloc[i+off_i][j+off_j][x]
                return ans
    for rings in xrange(R):
        # preprocess to figure out samelocability of x fleas moving from (i,j) to same location
#        for i in xrange(D):
#            for j in xrange(D):
#                if D-i-1 < i:
#                    sameloc[i][j] = copy(sameloc[D-i-1][j])
#                    continue
#                if D-j-1 < j:
#                    sameloc[i][j] = copy(sameloc[i][D-j-1])
#                    continue
#                na = numadj(i,j)
#                for x in xrange(n):
#                    sameloc[i][j][x] = mpf(0.0)
#                    for y in xrange(x,n):
#                        g = grid[turn][i][j][y]
#                        if g==0: continue
#                        sameloc[i][j][x] += g*pow(1/na,x)*pow((na-1)/na,y-x)*ch(y,x)
        for i in xrange(D):
            print i
            for j in xrange(D):
                if D-i-1 < i:
                    grid[1-turn][i][j] = copy(grid[1-turn][D-i-1][j])
                    continue
                if D-j-1 < j:
                    grid[1-turn][i][j] = copy(grid[1-turn][i][D-j-1])
                    continue
                grid[1-turn][i][j] = [mpf(0.0) for k in xrange(n)]
                for a in xrange(1 if i==0 else n): #up
                    for upa in xrange(a+1):
                        if i==0: p = mpf(1.0)
                        else:
                            na = numadj(i-1,j)
                            p = grid[turn][i-1][j][a]*pow(1/na,upa)*pow((na-1)/na,a-upa)*ch(a,upa)
                        for b in xrange(1 if i==D-1 else n-a): #down
                            for upb in xrange(b+1):
                                if i==D-1: pb=p
                                else:
                                    na = numadj(i+1,j)
                                    pb=p*grid[turn][i+1][j][b]*pow(1/na,upb)*pow((na-1)/na,b-upb)*ch(b,upb)
                                for c in xrange(1 if j==0 else n-a-b): #left
                                    for upc in xrange(c+1):
                                        if j==0: pc=pb
                                        else:
                                            na = numadj(i,j-1)
                                            pc=pb*grid[turn][i][j-1][c]*pow(1/na,upc)*pow((na-1)/na,c-upc)*ch(c,upc)
                                        for d in xrange(1 if j==D-1 else n-a-b-c): #right
                                            for upd in xrange(d+1):
                                                if j==D-1: pd=pc
                                                else:
                                                    na = numadj(i,j+1)
                                                    pd=pc*grid[turn][i][j+1][d]*pow(1/na,upd)*pow((na-1)/na,d-upd)*ch(d,upd)
                                                    #if pd!=0: print pd
                                                grid[1-turn][i][j][upa+upb+upc+upd] += pd
#                for x in xrange(n):
#                    grid[1-turn][i][j][x] = prob(i,j,0,x)
                den = sum(grid[1-turn][i][j])
                #if den!=0: print den
                for x in xrange(n):
                    grid[1-turn][i][j][x] /= den
        turn = not turn
        #print rings, sum(sum(grid[turn][i][j]) for i in xrange(D) for j in xrange(D))
        #print rings, grid[turn][0][0], sum(grid[turn][0][0]), sum(grid[turn][i][j][0] for i in xrange(D) for j in xrange(D))
        print rings, sum(sum(grid[turn][i][j]) for i in xrange(D) for j in xrange(D)), sum(grid[turn][i][j][0] for i in xrange(D) for j in xrange(D))
        #print rings, sum(grid[turn][0][0]), sum(grid[turn][i][j][0] for i in xrange(D) for j in xrange(D))
    return sum(grid[turn][i][j][0] for i in xrange(D) for j in xrange(D))

eps = 1E-7
n = 9
prev = solve(n-1)
cur = solve(n)
while cur<1 or abs(cur-prev) > eps:
    print cur
    n += 1
    prev, cur = cur, solve(n)
print cur
