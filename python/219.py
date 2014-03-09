#!/usr/bin/env python

# visualize code as a binary tree (binary trie) for prefix-free property.
# to get next code from given tree, split at the least-cost leaf.
# because of this, the differences in cost between any of our strings
# will differ by no more than 5. we then note that we only need
# to keep track of the frequencies at which these costs occur.

# number of iterations of while loop should be O(log(n)).

rem = 10**9-1
base = 0
freq = [1] + [0]*4
i = 0
while rem>0:
    sub = min(freq[i],rem)
    freq[i]-=sub
    rem -= sub
    freq[(i+1)%5]+=sub
    freq[(i+4)%5]+=sub
    if freq[i]==0:
        i = (i+1)%5
        base += 1

total = 0
for j in xrange(5):
    total += (base+j)*freq[(i+j)%5]
print total
