#!/usr/bin/env python
import numpy as np
from utils import fact, c, multinomial, partitions, permutations

"""
Basic idea: compress state space by representing permutations as products of
cycles.  It's not the permutation itself that matters; it's just the
out-of-order # of elements in each cycle. This is isomorphic with # ways to
partition 11 things = 56, small enough to do linear algebra and solve for the
expected # steps to terminate for each state in the Markov chain (involves
inverting a 56 x 56 matrix). From here, it's just a bunch of messy counting.
"""

N=11
nways_to_choose_swap = c(N,3)*fact(3)

def canon(part):
    return tuple(sorted(part))

def same_ns(part):
    ret = [1]
    cur_i = 0
    for i in xrange(1,len(part)):
        if part[i] == part[cur_i]:
            ret[-1] += 1
        else:
            ret.append(1)
            cur_i = i
    return ret

def nperms_with_part(part):
    ret = multinomial(part)
    for p in part:
        ret *= fact(p-1)
    for n in same_ns(part):
        ret //= fact(n)
    return ret

def expand(part):
    pi = [0]*N
    start = 0
    for p in part:
        for i in xrange(p):
            pi[start+i] = start + (i+1)%p
        start += p
    return pi

def contract(pi):
    part = []
    seen = set()
    for i in xrange(N):
        if i in seen:
            continue
        part.append(0)
        j = i
        while j not in seen:
            seen.add(j)
            part[-1] += 1
            j = pi[j]
    return canon(part)

_index={}
def index(part):
    if part in _index:
        return _index[part]
    ret = len(_index)
    _index[part] = ret
    return ret

def gather(A, part):
    if len(part)==N:
        return
    m = index(part)
    pi = expand(part)
    for i in xrange(N):
        for j in xrange(i+1, N):
            for k in xrange(j+1,N):
                for ii, jj, kk in permutations([i,j,k]):
                    pic = list(pi)
                    pic[i], pic[j], pic[k] = pic[ii], pic[jj], pic[kk]
                    A[m,index(contract(pic))] += 1./nways_to_choose_swap

nparts = sum(1 for part in partitions(N))
# use longdouble to accumlate stuff
A = np.zeros((nparts, nparts), dtype=np.longdouble)
for part in partitions(N):
    gather(A, part)
# cast down to float since required by np.linalg
A = np.array(A, dtype=float)
b = np.ones(nparts)
b[index(tuple([1]*N))] = 0.
x = np.linalg.solve(A - np.diag(np.ones(nparts)), -b)
ans = 0.
for part in partitions(N):
    ans += float(nperms_with_part(part)) / fact(N) * x[index(part)]
print int(round(ans))
