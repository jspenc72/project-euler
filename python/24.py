#!/usr/bin/env python

digits = range(10)
fact = [1] + range(1,10)
for i in xrange(1,10): fact[i]*=fact[i-1]
rem = 10**6
ans = ''
for i in xrange(9,-1,-1):
    j = (rem+fact[i]-1)//fact[i]
    ans = ans + str(digits[j-1])
    digits = digits[:j-1] + digits[j:]
    rem -= (j-1)*fact[i]
print ans
