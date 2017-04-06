#!/usr/bin/env python

"""
Basic idea: s(n) depends on s(i) for i<n in a fairly straightforward way.
"""

def mem(f):
    _mem_f = {}
    def _f(*args):
        if args in _mem_f:
            return _mem_f[args]
        else:
            ans = f(*args)
            _mem_f[args] = ans
            return ans
    return _f

_fact = [1]
def fact(n):
    while n>=len(_fact):
        _fact.append(_fact[-1]*len(_fact))
    return _fact[n]

def c(n,k):
    return fact(n) // fact(k) // fact(n-k)

@mem
def number_of_permutations_with_no_internal_ordering(n):
    if n==1: return 1
    ways = 0
    num_n_perms = fact(n)
    for i in xrange(1,n):
        num_possible_i_contig_chunks = c(n-1,i-1)
        num_ways_to_group = number_of_permutations_with_no_internal_ordering(i)
        total_perms_with_i_chunks = num_ways_to_group * num_possible_i_contig_chunks
        ways += total_perms_with_i_chunks
    return num_n_perms - ways

@mem
def s(n):
    if n==1: return 0
    ans = 0.
    ways = 0
    num_n_perms = fact(n)
    for i in xrange(1,n):
        num_possible_i_contig_chunks = c(n-1,i-1)
        num_ways_to_group = number_of_permutations_with_no_internal_ordering(i)
        total_perms_with_i_chunks = num_ways_to_group * num_possible_i_contig_chunks
        ways += total_perms_with_i_chunks
        if i>1:
            weight = float(total_perms_with_i_chunks) / num_n_perms
            ans += weight * (1. + s(i))
    p_sn = float(num_n_perms - ways) / num_n_perms
    ans = (p_sn + ans) / (1. - p_sn)
    return ans

if __name__=="__main__":
    print '%.8f' % s(52)
