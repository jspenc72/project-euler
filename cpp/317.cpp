#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MAX3(a,b,c) MAX(MAX(a,b),c)
#define MAX4(a,b,c,d) MAX(MAX3(a,b,c),d)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MIN3(a,b,c) MIN(MIN(a,b),c)
#define MIN4(a,b,c,d) MIN(MIN3(a,b,c),d)
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
const double pi = 3.14159265358979;
const double y = 100.0;
const double g = 9.81;
const double v0 = 20.0;
const double eps = 1E-5;

//not used but saved here for reference
double sgn(double x) {
    return (x>0) - (x<0);
}

double r(double h) {
    //see wikipedia article for range
    double theta=acos(sqrt((2*g*(y-h)+v0*v0)/(2*g*(y-h)+2*v0*v0)));
    double s = sin(theta);
    double t = (v0*s+sqrt(v0*v0*s*s-2*g*(h-y)))/g;
    double ret = v0*cos(theta)*t;
    if (ret!=ret) return 0.0f;
    return ret;
}

//adaptive quadrature
double integrate(double a, double b, double fa, double fb, double lrarea) {
    double mid = (a+b)/2;
    double fmid = pow(r(mid),2); //r^2
    double larea = 0.5*(mid-a)*(fa+fmid);
    double rarea = 0.5*(b-mid)*(fmid+fb);
    if (fabs(larea+rarea-lrarea)<eps) return larea+rarea;
    return integrate(a,mid,fa,fmid,larea)+integrate(mid,b,fmid,fb,rarea);
}

int main() {
    double a = 0.0, b=y+20.38735983690112;
    double fa = pow(r(a),2), fb = pow(r(b),2);
    double lrarea = 0.5*(b-a)*(fa+fb);
    printf("%.4f\n",pi*integrate(a,b,fa,fb,lrarea));
    return 0;
}
