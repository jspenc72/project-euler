#!/usr/bin/env python

n=10**25
mem={}

def hf(arr,k):
    v=0
    for i in xrange(k,len(arr)):
        v=v*3+arr[i]
    return v

def count(arr,k):
    if k>=len(arr): return 0
    hval = hf(arr,k)
    if (hval,k) in mem: return mem[hval,k]
    total=0
    for i in xrange(k,len(arr)-1):
        if arr[i] and not arr[i+1]:
            total+=1
            arr[i+1]=2
            arr[i]-=1
            total += count(arr,k)
            arr[i+1]=0
            arr[i]+=1
            total += count(arr,i+2)
            break
    mem[hval,k]=total
    return total

arr=[]
while n!=0:
    if n&1: arr.append(1)
    else: arr.append(0)
    n >>= 1
arr.reverse()

print count(arr,0)+1
