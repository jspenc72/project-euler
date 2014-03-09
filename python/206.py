#!/usr/bin/env python

for g in xrange(0,10):
    c1 = (14*g+4)/10
    for f in xrange(0,10):
        x1 = (c1+14*f+g*g)
        if x1%10 != 8: continue
        #print f,g
        c2 = x1/10
        for e in xrange(0,10):
            c3 = (c2+14*e+2*f*g)/10
            for d in xrange(0,10):
                x2 = (c3+14*d+2*e*g+f*f)
                if x2%10 != 7: continue
                #print d,e,f,g
                c4 = x2/10
                for c in xrange(0,10):
                    c5 = (c4+14*c+2*d*g+2*e*f)/10
                    for b in xrange(0,10):
                        x3 = (c5+14*b+2*c*g+2*d*f+e*e)
                        if x3%10 != 6: continue
                        #print b,c,d,e,f,g
                        c6 = x3/10
                        for a in xrange(0,10):
                            c7 = (c6+14*a+2*b*g+2*c*f+2*d*e)/10
                            x4 = (c7+2*a*g+2*b*f+2*c*e+d*d) + 14
                            if x4%10 != 5: continue
                            #print a,b,c,d,e,f,g
                            c8 = x4/10
                            c9 = (c8+2*g+2*a*f+2*b*e+2*c*d)/10
                            x5 = (c9+2*f+2*a*e+2*b*d+c*c)
                            if x5%10 != 4: continue
                            #print a,b,c,d,e,f,g
                            c10 = x5/10
                            c11 = (c10+2*e+2*a*d+2*b*c)/10
                            x6 = (c11+2*d+2*a*c+b*b)
                            if x6%10 != 3: continue
                            #print a,b,c,d,e,f,g
                            c12 = x6/10
                            c13 = (c12+2*c+2*a*b)/10
                            x7 = (c13+2*b+a*a)
                            if x7%10 != 2: continue
                            #print a,b,c,d,e,f,g
                            c14 = x7/10
                            c15 = (c14+2*a)/10
                            x8 = (c15+1)
                            if x8%10 != 1: continue
                            print '1' + str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g) + '70'
