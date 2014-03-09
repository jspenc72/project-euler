#!/usr/bin/env python

# needs bigint, built into python

print sum(map(int, (d for d in str(reduce(lambda x,y:x*y, xrange(2,101))))))
