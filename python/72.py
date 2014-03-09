#!/usr/bin/python

def combsHelper(l, m, i, p, n):
    if m == 0:
        return n/p-1
    total = 0
    for j in xrange(i, len(l)-m+1):
        total += combsHelper(l, m-1, j+1, l[j]*p, n)
    return total

def combs(l, m, n):
    return combsHelper(l, m, 0, 1, n)

if __name__ == '__main__':
    isPrime = []
    for i in xrange(1000001):
        isPrime.append(True)
    isPrime[0] = False
    isPrime[1] = False

    for i in xrange(2, len(isPrime)):
        if isPrime[i]:
            for j in xrange(i << 1, len(isPrime), i):
                isPrime[j] = False

    def factor(n):
        primes = []
        i = 2
        while i*i <= n:
            if isPrime[n]:
                primes.append((n, 1))
                return primes
            if isPrime[i] and n % i == 0:
                count = 0
                while n % i == 0:
                    n /= i
                    count += 1
                primes.append((i, count))
            i += 1
        if isPrime[n]:
            primes.append((n, 1))
        return primes

    total = 0
    pfactors = [[], []]
    
    for i in xrange(2, len(isPrime)):
        pfactors.append(factor(i))

    for i in xrange(2, len(pfactors)):
        primes = []
        count = 0
        for j in xrange(len(pfactors[i])):
            primes.append(pfactors[i][j][0])
        include = True
        for j in xrange(len(primes)):
            num = combs(primes, j+1, i)
            if include:
                count += num
            else:
                count -= num
            include = not include
        total += count

    print 999999*500000 - total
