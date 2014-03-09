#!/usr/bin/env python

# simple use of inclusion-exclusion
n=999
m3 = n//3
m5 = n//5
m15 = n//15
print 3*m3*(m3+1)/2 + 5*m5*(m5+1)/2 - 15*m15*(m15+1)/2
