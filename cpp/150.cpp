#include <iostream>
#include <cstring>
#include <climits>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

// no ingenuity here, just brute force
// sum(i*(1001-i) for i in xrange(1,1001)) < 10^9
// main idea is to store prefix sums in rows

const int oo = INT_MAX>>1;
using namespace std;
typedef long long ll;

const int N = 1000;
int tri[N+1][N+1];

int main() {
    int r=1, c=1;
    ll t=0;
    ll best = oo;
    memset(tri,0,sizeof(tri));
    REP(i,500500) {
        if (c>r) r+=(c=1);
        t = (615949*t + 797807)%(1<<20);
        tri[r][c] = tri[r][c-1] + (t-(1<<19));
        c++;
    }
    r=c=1;
    REP(i,500500) {
        if (c>r) r+=(c=1);
        ll cur=0;
        REP(h,1001-r) {
            cur += tri[r+h][c+h] - tri[r+h][c-1];
            best = MIN(cur,best);
        }
        c++;
    }
    cout << best << endl;
    return 0;
}
