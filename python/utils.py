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

def _partitions(n,k):
    if n==0:
        yield []
    else:
        for i in xrange(1,min(k,n)+1):
            for p in _partitions(n-i,i):
                yield p + [i]

def partitions(n):
    for p in _partitions(n,n):
        yield tuple(p)

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

def _permutations(arr, i):
    if i==len(arr):
        yield arr
    else:
        for j in xrange(i,len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            for p in _permutations(arr,i+1):
                yield p
            arr[i], arr[j] = arr[j], arr[i]

def permutations(arr):
    if type(arr) == int:
        arr = range(arr)
    for p in _permutations(arr,0):
        yield p

def multinomial(ns, mod=None):
    ret = fact(sum(ns), mod)
    if mod:
        for n in ns:
            ret *= pow(fact(n,mod),mod-2,mod)
            ret %= mod
    else:
        for n in ns:
            ret //= fact(n)
    return ret

def lucas(n,k,p):
    if n<k: return 0
    ret=1
    while n>0:
        ret = (ret*c(n%p,k%p,mod=p))%p
        n//=p
        k//=p
    return ret

def gcd(x,y):
    while y>0:
        x,y = y,x%y
    return x

def lcm(x,y):
    return x//gcd(x,y)*y
