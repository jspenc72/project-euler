#!/usr/bin/env python

def flatten(arr):
    if isinstance(arr,list):
        for x in arr:
            for y in flatten(x): yield y
    else: yield arr

def hf1(arr):
    ret=0
    for x in flatten(arr): ret = 2*ret+(x>0)
    return ret

def pretty(arr):
    for x in arr: print x
    print

m,n = 12,9

mem={}
ss = [[3, 4], [5, 6]] #for debugging
def numways(arr,i,sj):
    #pretty(arr)
    test = hf1(arr)
    if test in mem: return mem[test]
    total=0
    while all(arr[i]): i,sj=i+1,0
    for j in xrange(sj,n):
        if arr[i][j]: continue
        if j<n-2 and not any(arr[i][k] for k in xrange(j,j+3)):
            for k in xrange(j,j+3): arr[i][k]=1
            total += numways(arr, i, j+2)
            for k in xrange(j,j+3): arr[i][k]=0
        if i<m-2 and not any(arr[k][j] for k in xrange(i,i+3)):
            for k in xrange(i,i+3): arr[k][j]=2
            total += numways(arr, i, j)
            for k in xrange(i,i+3): arr[k][j]=0
        if i>=m-1: break #very important!
        for h in xrange(2):
            for k in xrange(2):
                if (h,k)==(0,0): nj=j-1
                else: nj=j
                if nj<0 or nj>=n-1: continue
                if any(arr[x][y] for x in xrange(i,i+2) for y in xrange(nj,nj+2) if (x,y)!=(i+h,nj+k)): continue
                v = ss[h][k]
                for x in xrange(i,i+2):
                    for y in xrange(nj,nj+2):
                        if (x,y)==(i+h,nj+k): continue
                        arr[x][y]=v
                total += numways(arr,i,j)
                for x in xrange(i,i+2):
                    for y in xrange(nj,nj+2):
                        if (x,y)==(i+h,nj+k): continue
                        arr[x][y]=0
        break #very important
    mem[test]=total
    return total

arr = [[0]*n for i in xrange(m)]
mem[2**(m*n)-1]=1
print numways(arr,0,0)
