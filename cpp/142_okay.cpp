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
using namespace std;
typedef vector<int> VE;
const float eps = pow(10, -8);

bool issquare(int n) {
    int r = int(round(sqrt(n)));
    return r*r==n;
}

int getsqr(int n) {
    float r = sqrt(n);
    if (r-int(r) < eps) return int(r);
    else return int(r)+1;
}

int main() {
    int x, y, z;
    for (int n=6; ; ++n) {
//        if (!(n%1000)) cout << n << endl;
        int xpr = getsqr((2*n+3+1)/3);
        int xpy, ypz;
        for (int xpyr=xpr; (xpy=xpyr*xpyr)<n; xpyr++) {
            z = n-xpy;
            int zpr = getsqr(z);
            for (int zpyr=zpr; zpyr<xpyr; zpyr++) {
                ypz = zpyr*zpyr;
                y = ypz-z;
                x = xpy-y;
                if (x>y && y>z && issquare(x+z) && issquare(x-y) && issquare(y-z) && issquare(x-z)) {
//                    cout << x << " " << y << " " << z << " " << x+y+z << " " << n << endl;
                    cout << x+y+z << endl;
                    goto end;
                }
            }
        }
    }
    end:
    return 0;
}
