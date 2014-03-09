#!/usr/bin/env python

def printans(l):
    small = 10
    index = 0
    for i in xrange(0, len(l), 3):
        if l[i] < small:
            small = l[i]
            index = i
    s = ''
    for i in xrange(index, len(l)):
        s += str(l[i])
    for i in xrange(0, index):
        s += str(l[i])
    return s

if __name__ == "__main__":
    largest = 0
    a=10
    for b in xrange(1, 10):
        for c in xrange(1, 10):
            if c in [b]:
                continue
            for d in xrange(1, 10):
                if d in [b,c]:
                    continue
                for e in xrange(1, 10):
                    if e in [b,c,d] or a+b != d+e:
                        continue
                    for f in xrange(1, 10):
                        if f in [b,c,d,e]:
                            continue
                        for g in xrange(1, 10):
                            if g in [b,c,d,e,f] or d+c != f+g:
                                continue
                            for h in xrange(1, 10):
                                if h in [b,c,d,e,f,g]:
                                    continue
                                for i in xrange(1, 10):
                                    if i in [b,c,d,e,f,g,h] or f+e != h+i:
                                        continue
                                    for j in xrange(1, 10):
                                        if j in [b,c,d,e,f,g,h,i] or h+g != j+b:
                                            continue
                                        s=printans([a,b,c,d,c,e,f,e,g,h,g,i,j,i,b])
                                        if len(s)==16:
                                            largest = max(largest, int(s))
    print largest
