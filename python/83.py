#!/usr/bin/python

def smallest(arr, considered):
    least = float('infinity')
    leastp = (0, 0)
    for p in considered:
        num = arr[p[0]][p[1]][1]
        if num <= least:
            least = num
            leastp = p
    if len(considered) == 0:
        print arr[79][79][1]
    return leastp

if __name__ == '__main__':
    arr = []
    with open('input/matrix.txt') as f:
        for line in f:
            seq = line.split(',')
            for i in xrange(len(seq)):
                seq[i] = [int(seq[i]), float('infinity'), True]
            arr.append(seq)
    outcount = 0
    total = len(arr)*len(arr[0])
    arr[0][0][1] = arr[0][0][0]
    considered = set([(0, 0)])
    while outcount < total:
        least = smallest(arr, considered)
        y = least[0]
        x = least[1]
        considered.remove(least)
        arr[y][x][2] = False
        outcount += 1
        for c in xrange(4):
            i = y
            j = x
            if c == 0:
                i = y-1
            if c == 1:
                i = y+1
            if c == 2:
                j = x-1
            if c == 3:
                j = x+1
            if i >= 0 and j >= 0 and i < len(arr) and j < len(arr[0]) and arr[i][j][2]:
                considered.add((i, j))
                arr[i][j][1] = min(arr[i][j][1], arr[y][x][1] + arr[i][j][0])
    print arr[len(arr)-1][len(arr[0])-1][1]
