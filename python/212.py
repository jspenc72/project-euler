#!/usr/bin/env python
from itertools import count

# pretty horribly heuristicy...
# we use an octree to partition the domain under consideration.
# a given octree node holds up to MAX_NODE_SIZE cuboids before spilling into its children
# We try a few settings of MAX_NODE_SIZE to determine how many octree nodes
# we end up creating (held in 'visited') variable, and estimate the cost of
# the algorithm as visited * 2^MAX_NODE_SIZE since we have to do inclusion-exclusion
# on the set of cuboids occupying a node. So we just vary MAX_NODE_SIZE until we
# get a reasonably small number (the larger MAX_NODE_SIZE, the smaller 'visited' will
# be, and 6 seems to be good enough)

visited = 0

N=50000
MAX_NODE_SIZE = 6

def volume(cube):
    vol=1
    for c in cube:
        vol *= (c[1]-c[0])
    return vol

def intersection(box1, box2):
    newbox = []
    for b1, b2 in zip(box1, box2):
        newbox.append((max(b1[0], b2[0]), min(b1[1], b2[1])))
    return tuple(newbox)

def overlaps(box1, box2):
    for b1, b2 in zip(box1, box2):
        if not ((b2[0] <= b1[0] and b1[0] < b2[1]) or (b1[0] <= b2[0] and b2[0] < b1[1])):
            return False
    return True

def degenerate(bounds):
    for b in bounds:
        if b[0]>=b[1]:
            return True
    return False

def allsubsets(stuff, i=0):
    if i < len(stuff):
        maybe = stuff[i]
        yield maybe, 1
        for subint, num in allsubsets(stuff, i+1):
            yield intersection(subint, maybe), num+1
            yield subint, num

def inexvol(cubes):
    total = 0
    for subint, card in allsubsets(cubes):
        if degenerate(subint):
            continue
        subvol = volume(subint)
        if card&1:
            total += subvol
        else:
            total -= subvol
    return total

class octree(object):
    def __init__(self, xb, yb, zb):
        self.xb = xb
        self.yb = yb
        self.zb = zb
        self.filled = False
        self.children = [None]*8
        self.occupying = []
        self.spilled = False

    @staticmethod
    def _midpoint(bounds):
        return (bounds[0] + bounds[1])//2

    @property
    def bounds(self):
        return (self.xb, self.yb, self.zb)

    @property
    def volume(self):
        vol = 1
        for b in [self.xb, self.yb, self.zb]:
            vol *= (b[1]-b[0])
        return vol

    def filled_volume(self):
        global visited
        visited += 1
        if self.filled:
            return self.volume
        elif self.occupying:
            assert not self.spilled
            return inexvol(self.occupying)
        else:
            vol = 0
            for child in filter(lambda c: c, self.children):
                vol += child.filled_volume()
            return vol

    def children_with_bounds(self):
        for i, xbounds in enumerate([(self.xb[0], self._midpoint(self.xb)), (self._midpoint(self.xb), self.xb[1])]):
            for j, ybounds in enumerate([(self.yb[0], self._midpoint(self.yb)), (self._midpoint(self.yb), self.yb[1])]):
                for k, zbounds in enumerate([(self.zb[0], self._midpoint(self.zb)), (self._midpoint(self.zb), self.zb[1])]):
                    yield self.children[i*4 + j*2 + k], (xbounds, ybounds, zbounds)

    def insert_box(self, box):
        global visited
        visited += 1
        if self.filled:
            return
        intersect = intersection(self.bounds, box)
        if intersect == self.bounds:
            self.filled = True
            return
        if not self.spilled and len(self.occupying) < MAX_NODE_SIZE:
            self.occupying.append(intersect)
        else:
            self.spilled = True
            for cuboid in [intersect] +  self.occupying:
                for i, (child, cbounds) in enumerate(self.children_with_bounds()):
                    if overlaps(cuboid, cbounds) and not degenerate(cbounds):
                        if child is None:
                            child = octree(*cbounds)
                            self.children[i] = child
                        child.insert_box(cuboid)
            self.occupying = []

_S = {}
def S(k):
    if 1<=k and k<=55:
        return (100003 - 200003*k + 300007*k**3) % 1000000
    elif k in _S:
        return _S[k]
    else:
        _S[k] = (S(k-24) + S(k-55))%1000000
        return _S[k]

def S_gen():
    for k in count(1):
        yield S(k)

def cubes():
    gen = S_gen()
    while True:
        x0 = gen.next() % 10000
        y0 = gen.next() % 10000
        z0 = gen.next() % 10000
        dx = 1 + gen.next() % 399
        dy = 1 + gen.next() % 399
        dz = 1 + gen.next() % 399
        yield ((x0, x0+dx), (y0, y0+dy), (z0, z0+dz))

box = [(0, 10400) for i in xrange(3)]

tree = octree(*box)
for i, cube in enumerate(cubes()):
    if i>=N:
        break
    tree.insert_box(cube)

visited = 0
#print tree.filled_volume(), visited
print tree.filled_volume()
