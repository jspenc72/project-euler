#!/usr/bin/env python

def verify(x,y):
    z=0
    for i in xrange(1,x+1):
        j=i
        while j:
            z += ((j%10)==y)
            j //= 10
    print z==x

# derivation...
# q(n) == 9*q(n-1) + p(n-1)
# p(n) == 10^n + 9*q(n-1) + p(n-1)
# q(n) == p(n) - 10^n
# p(n) == 10^n + 9*q(n-1) + p(n-1)
#      == 10^n + 10*p(n-1) - 9*10^(n-1)
#      == 2*10^n + 100*p(n-1) - 2*9*10^(n-1)
#      .
#      .
#      .
#      == 10^n + n*(10^n - 9*10^(n-1))
#      == 10^n + n*10^(n-1)

ans = 0
def f(i, n, m, c, v, start):
    global ans
    if i<0:
        if n-1==m: ans += m
        return

    # TODO (smacke): verify these bounds
    if m-n > 10**(i+1): return
    if n-m > 10**(i+1)*c + 10**(i+1) + (i+1)*10**i: return

    # without this we will keep add the same value
    # more than once
    if not start: f(i-1, n, m, c, v, False)

    for j in xrange(1,10):
        n += 10**i
        m += c*10**i + i*10**(max(0,i-1))
        if j-1==v: m += 10**i

        if j==v:
            f(i-1, n, m, c+1, v, False)
        else:
            f(i-1, n, m, c, v, False)

for i in xrange(0, 20): # 1, 20
    for j in xrange(1, 10):
        f(i,0,0,0,j, True)

print ans
