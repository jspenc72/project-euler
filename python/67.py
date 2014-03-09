#!/usr/bin/env python

# requires redirecting triangles.txt to stdin
# simple dp

arr = []
while True:
    try: arr.append(map(int, raw_input().strip().split()))
    except EOFError: break
for i in xrange(1,len(arr)):
    for j in xrange(len(arr[i])):
        arr[i][j] += max(arr[i-1][j] if j<i else 0, arr[i-1][j-1] if j>0 else 0)
print max(arr[len(arr)-1])
