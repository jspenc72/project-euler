#!/usr/bin/env python
import numpy as np
import sys

a, b = 3, 1
N = 10**6 # this turned out to be enough precision
b = 1

xs = np.linspace(0, b, N) # a smarter solution would be to increase the number of points close to 'b'
ys = a*(1 - (xs/b)**2)**.5
gradx = xs / b**2 # (not worrying about constants since they get normalized out...)
grady = ys / a**2
gradmag = (gradx**2 + grady**2)**.5
gradx /= gradmag
grady /= gradmag

xs += gradx
ys += grady

xL, xR = xs[:-1], xs[1:]
yL, yR = ys[:-1], ys[1:]

# volume formula of conic cross section of width w and heights h1 and h2:
# pi*w / (2*(h2-h1)) * (h2**3 - h1**3)

total_vol = 2* np.pi / 3. * np.sum((xR-xL)/(yR-yL) * (yR**3 - yL**3))
choco_vol = total_vol - 4./3.*a**2*b*np.pi

print '%.8f' % choco_vol
