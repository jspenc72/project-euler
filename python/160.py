#!/usr/bin/env python

# constants
n = 10**12
mod2, mod5 = 2**5, 5**5
phi5 = mod5-mod5//5

# get multiplicity 5 in n! (aka v_5(n!))
mul5 = 0
x=5
while x<=n:
    mul5 += n//x
    x*=5

# calculate product of k <= n where 5 does not divide k
# (for all n up to (and including) 5^5-1)
fact5 = [1]
for i in xrange(1,mod5):
    if not i%5: fact5.append(fact5[-1])
    else: fact5.append(fact5[-1]*i%mod5)

# general purpose function to find n!/v_p(n!) mod m, where m=p^k
# note: fact[-1] == (m-1) (or p^k - 1), trivial generalization of Wilson's theorem
def f(x,m,p,fact):
    if x==0: return 1
    return pow(fact[-1],x//m,m)*fact[x%m]%m*f(x//p,m,p,fact)%m

# calculate factorial divided through by 5^v_5(n!) (v_p is multiplicity of p)
# additionally, we remove an equal number of factors of two
r5 = f(n,mod5,5,fact5)*pow(2,(phi5-1)*mul5,mod5)%mod5

# previous number mod 2^5
# (I am assuming that mul2 >= mul5+5 here)
r2 = 0
#CRA2
s = r2 + (r5-r2)*pow(mod2,phi5-1,mod5)%mod5*mod2
print s
