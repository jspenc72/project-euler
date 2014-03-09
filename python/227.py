#!/usr/bin/env python

import scipy.linalg as linalg
import numpy as np

# nothing to it, just solve the linear system

A = np.zeros((50,50))
b = -np.ones(50)
for i in xrange(2,48):
    A[i][i] = .5 - 1.
    A[i][i+1] = A[i][i-1] = 2./9
    A[i][i+2] = A[i][i-2] = 1./36
    
# it would have been nice to automate these...

A[49][49] = 18./36 - 1.
A[49][48] = 16./36
A[49][47] = 2./36

A[48][46] = 1./36
A[48][47] = 8./36
A[48][48] = 19./36 - 1
A[48][49] = 8./36

A[1][0] = 8./36
A[1][1] = 18./36 - 1
A[1][2] = 8./36
A[1][3] = 1./36

A[0][0] = 19./36 - 1
A[0][1] = 8./36
A[0][2] = 1./36

ans = linalg.solve(A,b)[49]
print round(ans,10-int(np.log10(ans))) # 6 significant digits
