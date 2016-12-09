#include <algorithm>
#include <iostream>
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

const int oo = INT_MAX>>1;

const double TOL=1e-12;

using namespace std;

typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> pii;

typedef long long ll;

inline double s(double x) {
    return min(x-floor(x), ceil(x)-x);
}

double h(double x, double tol=TOL) {
    double ret = 0.;
    for (int n=0; ; n++) {
        double p = pow(2., n);
        double r = s(p*x)/p;
        ret += r;
        if (r < tol) break;
    }
    return ret;
}

double hc(double x, double hb) {
    double delta = sqrt(pow(.25,2) - pow(x-.25,2));
    return .5 + delta < hb ? .5 + delta : .5 - delta;
}

inline double sqdist(double px1, double py1, double px2, double py2) {
    return pow(px2-px1,2.) + pow(py2-py1,2.);
}

double getleft(double tol=TOL, double eps=TOL) {
    double cx = .25;
    double cy = .5;
    double left = 0.;
    double right = 0.25;
    while (fabs(right-left) > eps) {
        double mid = .5*(left+right);
        double hm = h(mid, tol);
        double dm = sqdist(cx, cy, mid, hm);
        if (dm > pow(.25,2)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return .5*(left+right);
}

double area(int n, double left, double right, double tol=TOL) {
    double step = (right-left)/n;
    double x1 = left;
    double yb = h(x1, tol);
    double yc = hc(x1, yb);
    double ret = 0.;
    for (int i=0; i<n; i++) {
        double x2 = x1 + step;
        double yb2 = h(x2, tol);
        double yc2 = hc(x2, yb2);
        ret += .5*step*(yb-yc + yb2-yc2);
        x1 = x2;
        yb = yb2;
        yc = yc2;
    }
    return ret;
}

double adaptive(double left, double hl, double right, double hr, double tol=TOL) {
    double mid = .5*(left+right);
    double hmb = h(mid, tol);
    double hmc = hc(mid, hmb);
    double hm = hmb - hmc;
    double a1 = .5*(right-left)*(hl + hr);
    double a2 = .5*(mid-left)*(hl + hm) + .5*(right-mid)*(hm + hr);
    if (fabs(a2-a1) > tol) {
        return adaptive(left, hl, mid, hm, tol) + adaptive(mid, hm, right, hr, tol);
    } else {
        return a2;
    }
}

// it turns out that simple trapezoid integration is fine,
// no fancy adaptive stuff necessary
// for some reason, my adaptive method is slightly more
// well-behaved in that it doesn't get NaN like the non-adaptive
// for small numbers of rectangles. Also, slightly faster
int main() {
    // we don't actually have to get the left intersection
    // if we just add trapezoids which have circle underneath >_<
    double left = getleft();
    double right = .5;
    double hlb = h(left);
    double hlc = hc(left, hlb);
    double hl = hlb - hlc;
    double hrb = h(right);
    double hrc = hc(right, hrb);
    double hr = hrb-hrc;
    printf("%.8f\n", adaptive(left, hl, right, hr));
//    printf("%.8f\n", area(1<<19, left, right));
    return 0;
}
