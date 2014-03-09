#!/usr/bin/env python

def strans(arr, sides):
    small = 10
    index = 0
    l = []
    for i in sides:
        l.append(arr[i])
    for i in xrange(0, len(l), 3):
        if l[i] < small:
            small = l[i]
            index = i
    s = ''
    for i in xrange(index, len(l)):
        s += str(l[i])
    for i in xrange(0, index):
        s += str(l[i])
    return s

def search(l, index):
    if index == 10:
        global largest
        global sides
        s=strans(l, sides)
        largest = max(largest, int(s))
        return
    for i in xrange(1, 11):
        if i not in l and constraint[index](l+[i]):
            search(l+[i], index+1)

if __name__=="__main__":
    largest = 0
    sides = [0,1,2,3,2,4,5,4,6,7,6,8,9,8,1]
    constraint = [lambda l: True]*10
    constraint[0] = lambda l: l[0] == 10
    constraint[4] = lambda l: l[0] + l[1] == l[3] + l[4]
    constraint[6] = lambda l: l[2] + l[3] == l[5] + l[6]
    constraint[8] = lambda l: l[4] + l[5] == l[7] + l[8]
    constraint[9] = lambda l: l[6] + l[7] == l[1] + l[9]
    search([], 0)
    print largest
