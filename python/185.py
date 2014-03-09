#!/usr/bin/env python
from copy import deepcopy
from itertools import combinations as cmb

guess=[
('5616185650518293', 2),
('3847439647293047', 1),
('5855462940810587', 3),
('9742855507068353', 3),
('4296849643607543', 3),
('3174248439465858', 1),
('4513559094146117', 2),
('7890971548908067', 3),
('8157356344118483', 1),
('2615250744386899', 2),
('8690095851526254', 3),
('6375711915077050', 1),
('6913859173121360', 1),
('6442889055042768', 2),
('2326509471271448', 2),
('5251583379644322', 2),
('1748270476758276', 3),
('4895722652190306', 1),
('3041631117224635', 3),
('1841236454324589', 3),
('2659862637316867', 2)]
guess.sort(key=lambda x:x[1]) # most constraining first (sort of)

s='2321386104303845' # 0 correct so we remove these possibilities
m=len(s)
vald=[range(10) for i in xrange(m)]
correctd=[range(m) for i in xrange(len(guess))]
for i in xrange(m):
    vald[i].remove(int(s[i]))

def ac3(vd,cd):
    for i in xrange(len(guess)):
        mod=False
        for j in xrange(len(vd)):
            if int(guess[i][0][j]) not in vd[j]:
                if j in cd[i]:
                    cd[i].remove(j)
                    mod=True
        if len(cd[i]) < guess[i][1]: return False
        if mod and len(cd[i]) == guess[i][1]:
            for j in xrange(len(vd)):
                v = int(guess[i][0][j])
                if j in cd[i]:
                    if v not in vd[j]: return False
                    vd[j] = [v]
                elif v in vd[j]:
                    vd[j].remove(v)
                    if not vd[j]: return False
            return ac3(vd,cd)
    return True

def solve(vd,cd,i):
    if i==len(guess): return vd
    for correct in cmb(cd[i], guess[i][1]):
        vd_c = deepcopy(vd)
        cd_c = deepcopy(cd)
        cd_c[i] = [y for y in correct]
        for j in xrange(len(vd)):
            v = int(guess[i][0][j])
            if j in correct:
                if v not in vd[j]: break
                vd_c[j] = [v]
            else:
                if v in vd_c[j]:
                    vd_c[j].remove(v)
                    if not vd_c[j]: break
        else:
            if not ac3(vd_c,cd_c): continue
            t = solve(vd_c,cd_c,i+1)
            if t: return t
    return False

print reduce(lambda x,y:x+y, map(lambda s:str(s[0]),solve(vald,correctd,0)))
