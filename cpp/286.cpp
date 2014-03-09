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

const double eps = 1E-12;
const double prob = 0.02;

int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

double F[50][21];
double f(double q, int x, int pts) {
    if (pts > 20) return 0.0;
    if (x==50) {
        if (pts==20) return 1.0;
        return 0.0;
    }
    double &ret = F[x][pts];
    if (ret >= 0) return ret;
    double p = (1.0-(x+1)/q);
    return (ret = p*f(q,x+1,pts+1) + (1.0-p)*f(q,x+1,pts));
}

int main() {
    double left = 50.0;
    double right = 10000.0; //sufficiently large right endpoint, verified in python
    double est;
    double q = 1.0;
    while (fabs(est-prob) > eps) {
        fill((double*)F,(double*)F+(50*21),-1.0);
        q = (left+right)/2.0;
        est = f(q, 0, 0);
        if (est < prob) right = q;
        else left = q;
    }
    cout << "use last digit to round:" << endl;
    printf("%.11lf\n", q);
    return 0;
}
