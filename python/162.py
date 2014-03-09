#!/usr/bin/env python

d={}
def counthex(x,y,prev):
    if x==16:
        if y==7: return 1
        return 0
    if (x,y,prev) in d: return d[x,y,prev]
    total = 13*counthex(x+1,y,True)
    if prev: total += counthex(x+1,y|1,True)
    else: total += counthex(x+1,y,False)
    total += counthex(x+1,y|2,True) + counthex(x+1,y|4,True)
    d[x,y,prev] = total
    return total

print hex(counthex(0,0,False))[2:].upper()
