#!/usr/bin/env python
import numpy as np
from scipy import linalg

import sys
sys.setrecursionlimit(10**6)


N=5
offsets = [(0,1),(0,-1),(-1,0),(1,0)]

def valid(r,c):
    return r>=0 and r<N and c>=0 and c<N

def illegal(taken,r,c):
    if not valid(r,c): return True
    if r==0 and c in taken: return True
    return False

def getStates(config,dest):
    ret = set()
    for i in xrange(N):
        if i==dest: continue
        if (config>>i)&1: ret.add(i)
    return ret

def getSubmatrixIndices(taken):
    ret=[]
    prev=0
    for s in taken:
        ret.extend(range(prev,s))
        prev = s+1
    ret.extend(range(prev,N*N))
    return ret

def convert(r,c):
    return N*r+c

def reflect(config):
    states = getStates(config,-1)
    return sum(1<<(N-1-s) for s in states)

def bc(n):
    r=0
    while n:
        r+=1
        n&=(n-1)
    return r

Expect={}
def expect_prob_sols(config, dest):
    if (config,dest) in Expect: return Expect[config,dest]
    A_expect = np.zeros((N*N,N*N))
    A_prob = np.zeros((N*N,N*N))
    b_expect = np.zeros(N*N)
    taken = getStates(config,dest)
    submatrix = getSubmatrixIndices(taken)
    for r1 in xrange(N):
        for c1 in xrange(N):
            A_expect[N*r1+c1][N*r1+c1]=1.0
            A_prob[N*r1+c1][N*r1+c1]=1.0
            if illegal(taken,r1,c1): continue
            if r1==0 and c1==dest: continue
            b_expect[r1*N+c1]=1.0
            places=[]
            for oR,oC in offsets:
                r2,c2 = r1+oR, c1+oC
                places.append((r2,c2))
            bad_expect=0
            bad_prob=0
            for r2,c2 in places:
                #if illegal(taken,r2,c2): bad_expect+=1
                if not valid(r2,c2): bad_prob+=1
                if not valid(r2,c2): bad_expect+=1 # no fucking way
            assert bad_expect < 4, "can't border 4 bad_expect slots"
            assert bad_prob <= 2, "can't border 3+ bad_prob slots"
            p_expect = 1.0/float(4-bad_expect)
            p_prob = 1.0/float(4-bad_prob)
            for r2,c2 in places:
                if not illegal(taken,r2,c2):
                    A_expect[N*r1+c1,N*r2+c2]=-p_expect
                    A_prob[N*r1+c1,N*r2+c2]=-p_prob
    A_expect = A_expect[submatrix,:][:,submatrix]
    A_prob = A_prob[submatrix,:][:,submatrix]
    b_expect = b_expect[submatrix]
    b_prob = np.ones(len(b_expect)) - b_expect
    sol_expect = linalg.solve(A_expect,b_expect)
    sol_prob = linalg.solve(A_prob,b_prob)
    Expect[config,dest] = (sol_expect,sol_prob)
    return (sol_expect,sol_prob)

Steps={}
def steps(start_config, dest_config, start):
    if start_config==0 and dest_config==0: return 0
    # exploit some symmetry
    if dest_config > reflect(dest_config):
        start_config, dest_config = reflect(start_config), reflect(dest_config)
        start = start - start%N + (N-1-start%N)
    assert bc(dest_config) > 0
    start -= (bc(dest_config)-1)
    if (start_config, dest_config, start) in Steps:
        return Steps[start_config,dest_config, start]
    dest_states = getStates(dest_config,-1)
    assert len(dest_states) == bc(dest_config)
    total = 0.
    for dest in dest_states:
        expect, prob = expect_prob_sols(dest_config,dest)
        new_start = convert(N-1,dest)
        assert bc(dest_config^(1<<dest)) == bc(dest_config)-1
        total += prob[start]*(expect[start] + steps(dest_config^(1<<dest), start_config, new_start))
    Steps[start_config,dest_config,start] = total
    return total

start = convert(N//2, N//2)
print round(steps((1<<N)-1,(1<<N)-1,start),6)
