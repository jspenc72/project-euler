#!/usr/bin/env python
import numpy as np
import cvxpy as cvx

x = cvx.Variable(6)
deltas = cvx.Variable(7,2)
b = np.arange(6, dtype=float)
b = .5*(100. - 50.*2**.5) + b*10*2**.5
speeds = np.arange(5)
speeds = 9 - speeds
obj = cvx.Minimize(cvx.norm2(deltas[0,:])/10. + cvx.norm2(deltas[6,:])/10. + \
                sum(cvx.norm2(deltas[i,:])/speeds[i-1] for i in xrange(1,6)))
constraints = [deltas[0,0] == x[0], deltas[0,1] == x[0]-b[0]]
for i in xrange(1,6):
    constraints.append(deltas[i,0] == x[i]-x[i-1])
    constraints.append(deltas[i,1] == x[i]-x[i-1]-b[i]+b[i-1])
constraints.append(deltas[6,0] == 100.-x[5])
constraints.append(deltas[6,1] == x[5]-b[5])

prob = cvx.Problem(obj, constraints)

print '%.10f' % prob.solve(solver=cvx.SCS, eps=1e-11)
