#!/usr/bin/python

def path(arr, x, y):
    total = arr[y][x][1]
    for i in xrange(y, -1, -1):
        total += arr[i][x+1][0]
        arr[i][x+1][1] = min(arr[i][x+1][1], total)
    total = arr[y][x][1] + arr[y][x+1][0]
    for i in xrange(y+1, len(arr)):
        total += arr[i][x+1][0]
        arr[i][x+1][1] = min(arr[i][x+1][1], total)

if __name__=='__main__':
    arr = []
    oo = float("infinity")
    with open('input/matrix.txt') as f:
        for line in f:
            seq = line.split(',')
            for i in xrange(len(seq)):
                seq[i] = int(seq[i])
                if i == 0:
                    seq[i] = [seq[i], seq[i]]
                else:
                    seq[i] = [seq[i], oo]
            arr.append(seq)

    for j in xrange(len(arr[0]) - 1):
        for i in xrange(len(arr)):
            path(arr, j, i)

    smallest = arr[0][len(arr[0])-1][1]
    for i in xrange(1, len(arr)):
        smallest = min(smallest, arr[i][len(arr[i]) - 1][1])

    print smallest
