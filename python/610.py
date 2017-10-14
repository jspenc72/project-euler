#!/usr/bin/env python
import re

# number of M's in front is a geometric random variable,
# then just simulate the process (normalizing appropriately)

def minimize(num):
    num=re.sub('IIII', 'IV', num)
    num=re.sub('VV', 'X', num)
    num=re.sub('VIV', 'IX', num)
    num=re.sub('XXXX', 'XL', num)
    num=re.sub('LL', 'C', num)
    num=re.sub('LXL', 'XC', num)
    num=re.sub('CCCC', 'CD', num)
    num=re.sub('DD', 'M', num)
    num=re.sub('DCD', 'CM', num)
    return num

def convert(i):
    if i>=500:
        return 'D' + convert(i-500)
    elif i>=100:
        return 'C' + convert(i-100)
    elif i>=50:
        return 'L' + convert(i-50)
    elif i>=10:
        return 'X' + convert(i-10)
    elif i>=5:
        return 'V' + convert(i-5)
    elif i>=1:
        return 'I' + convert(i-1)
    else:
        return ''

p = .14
_prob = {
    'I': p,
    'V': p,
    'X': p,
    'L': p,
    'C': p,
    'D': p,
    'M': p,
    '#': 1.-7*p
}

value = {}
valid = set()

def prob(num):
    if len(num)==1:
        return _prob[num]
    prev_prob = prob(num[:-1])
    total = 0.
    for char in _prob:
        if (num[:-1] + char) in valid:
            total += _prob[char]
    return prev_prob*_prob[num[-1]]/total

for i in xrange(1000):
    num = minimize(convert(i))
    value[i] = num + '#'
    valid.add(num)
    valid.add(num + '#')

ans = 0.
total = sum(prob(value[i]) for i in xrange(1000))
#print total # should be 1.-p
for i in xrange(1,1000):
    ans += i*prob(value[i]) / total
print '%.8f' % (p / (1.-p) * 1000 + ans)
