#!/usr/bin/env python

from copy import deepcopy

def minlen(arr2):
    m = float('inf')
    for arr1 in arr2:
        for arr in arr1:
            m = min(len(arr), m)
    return m

def maxlen(arr2):
    m = 0
    for arr1 in arr2:
        for arr in arr1:
            m = max(len(arr), m)
    return m

def quad(y,x):
    return (y/3,x/3)

def cleanpuz(puzzle):
    while True:
        changed = False
        for i in xrange(9):
            for j in xrange(9):
                if len(puzzle[i][j]) <= 1: continue
                val = puzzle[i][j][0]
                for k in xrange(9):
                    for l in xrange(9):
                        if i==k and j==l: continue
                        if i==k or j==l or quad(k,l)==quad(i,j):
                            try:
                                puzzle[k][l].remove(val)
                                changed = True
                            except ValueError: pass
        if not changed: break
    return puzzle

def trysud(puzzle,y,x,val):
    p2 = deepcopy(puzzle)
    p2[y][x] = [val]
    while True:
        changed = False
        for i in xrange(9):
            for j in xrange(9):
                if len(p2[i][j]) != 1: continue
                v = p2[i][j][0]
                for k in xrange(9):
                    for l in xrange(9):
                        if i==k and j==l: continue
                        if i==k or j==l or quad(k,l)==quad(i,j):
                            try:
                                p2[k][l].remove(v)
                                changed = True
                            except ValueError: pass
        if not changed: break
    #p2 = cleanpuz(p2)
    if minlen(p2) == 0: return False,
    if maxlen(p2) == 1: return (True,p2)
    for i in xrange(9):
        for j in xrange(9):
            if len(p2[i][j]) == 1: continue
            for psol in (trysud(p2,i,j,poss) for poss in p2[i][j]):
                if psol[0]: return psol
            return False,

def solvesud(puzzle):
    #puzzle = cleanpuz(puzzle)
    while True:
        changed = False
        for i in xrange(9):
            for j in xrange(9):
                if len(puzzle[i][j]) != 1: continue
                val = puzzle[i][j][0]
                for k in xrange(9):
                    for l in xrange(9):
                        if i==k and j==l: continue
                        if i==k or j==l or quad(k,l)==quad(i,j):
                            try:
                                puzzle[k][l].remove(val)
                                changed = True
                            except ValueError: pass
        if not changed: break
    if minlen(puzzle) == 0: return False,
    if maxlen(puzzle) == 1: return puzzle
    for i in xrange(9):
        for j in xrange(9):
            if len(puzzle[i][j]) == 1: continue
            for psol in (trysud(puzzle,i,j,poss) for poss in puzzle[i][j]):
                if psol[0]: return psol[1]
            return False,

puzzles = []

curpuz = []
place = 0
with open('input/sudoku.txt') as f:
    for line in f:
        if line[0]=='': continue
        if place%10==0:
            if curpuz != []: puzzles.append(curpuz)
            curpuz = []
            place += 1
            continue
        curpuz.append([])
        curline = place%10-1
        for i in xrange(9):
            if line[i]=='': continue
            if line[i]=='0': curpuz[curline].append(range(1,10))
            else: curpuz[curline].append([int(line[i])])
        place += 1
puzzles.append(curpuz)

total = 0
ind=0
for puz in puzzles:
    solved = solvesud(puz)
    plus = int(str(solved[0][0][0])+str(solved[0][1][0])+str(solved[0][2][0]))
    #print ind
    total += plus
    ind += 1
print total
