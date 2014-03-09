#!/usr/bin/env python

# just keep dividing n by
# successively larger primes.
# the thing that remains is the answer

n = 600851475143
p = 2
while p<n:
    while not n%p:
        n //= p
    p += 1
print n
