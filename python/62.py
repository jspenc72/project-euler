#! /usr/bin/python

# pretty much brute force
# runs in about 1:30, would be faster in C

def digitize(n):
    l = []
    total = 0
    for i in xrange(10):
        l.append(0)
    while n != 0:
        l[n%10] += 1
        n /= 10
    s = set([])
    for i in xrange(len(l)):
        d = l[i]
        if d != 0:
            s.add((i, d))
            total += d
    return (s, total)

i = 1
perms = 1
while perms < 5:
    perms = 1
    s = digitize(i**3)
    d = s[1]
    j = i+1
    while True:
        t = digitize(j**3)
        if t[1] > s[1]:
            break
        if s[0] == t[0]:
            perms += 1
        j += 1
    i += 1

print (i-1)**3
