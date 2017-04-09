import functools

def memoize(f):
    _f={}
    @functools.wraps(f)
    def mem_f(*args):
        if args in _f:
            return _f[args]
        else:
            ret = f(*args)
            _f[args] = ret
            return ret
    return mem_f

def sieve(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False
    for i in xrange(2,N+1):
        if i*i>N: break
        if not prime[i]: continue
        for j in xrange(i*i,N+1,i):
            prime[j] = False
    return prime

_fact=[1]
def fact(n, mod=None):
    while len(_fact)<=n:
        _fact.append(_fact[-1]*len(_fact))
        if mod: _fact[-1] %= mod
    return _fact[n]

def c(n,k, mod=None):
    if n<0 or k<0: return 0
    if mod:
        return fact(n,mod) * pow(fact(k,mod),mod-2,mod) * pow(fact(n-k,mod),mod-2,mod) % mod
    else:
        return fact(n) // fact(k) // fact(n-k)
