#!/usr/bin/env python
import re

# for each digit d:
# index of containing string is 1st m such that 100*F_m >= n
# index within containing string is ceil(d/100)
# suppose index is k (within F_m)
# k > F_{m-2} ==> index is k-F_{m-2} within F_{m-1}
#            else index is k within F_{m-2}

mem={}
def fib(n):
    if n<=2: return 1
    if n in mem: return mem[n]
    ret = mem[n] = fib(n-1)+fib(n-2)
    return ret

A="""
14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679
""".strip()
B="""
82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196
""".strip()
A = re.sub('\n','',A)
B = re.sub('\n','',B)

ans = 0
for i in xrange(18):
    d = (127+19*i)*7**i
    m = 1
    while 100*fib(m) < d: m+=1
    k = (d+99)/100
    while m>2:
        if k>fib(m-2):
            k-=fib(m-2)
            m-=1
        else: m-=2
    ans += 10**i * int(A[(d-1)%100] if m==1 else B[(d-1)%100])
print ans
