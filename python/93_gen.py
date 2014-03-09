#!/usr/bin/env python

def opcombs():
    for i in xrange(4):
        for j in xrange(4):
            for k in xrange(4):
                yield [i,j,k]

oparr = []
for opcomb in opcombs():
    optup = []
    for i in xrange(3):
        if opcomb[i] == 0: optup.append('+')
        elif opcomb[i] == 1: optup.append('-')
        elif opcomb[i] == 2: optup.append('*')
        elif opcomb[i] == 3: optup.append('/')
    oparr.append(tuple(optup))

for optup in oparr:
    print 'funcarr.append(lambda a,b,c,d: a %s (b %s (c %s d)))' % optup
    print 'funcarr.append(lambda a,b,c,d: a %s ((b %s c) %s d))' % optup
    print 'funcarr.append(lambda a,b,c,d: (a %s b) %s (c %s d))' % optup
    print 'funcarr.append(lambda a,b,c,d: ((a %s b) %s c) %s d)' % optup
