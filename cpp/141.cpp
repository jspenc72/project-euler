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
#define MP make_pair
#define SZ size()
#define PB push_back

using namespace std;
typedef long long ll;
const ll n = 1000000;
//const ll n = 317;
typedef pair<int,int> PI;
typedef vector<PI> VP;

// here is the basic idea: for each square, loop through its
// divisors. since q^2, d^2, >= n^2, we can be sure that we're
// not missing anything. now, assume we are looking at d^2:
// then we loop through divisors r < d, and we divide d^2 by
// r to obtain q (we have d^2=r*q or q^2=r*d). if d*q+r is a
// square < 10^12, we mark it as progressive.
// the same logic as above holds for q^2=r*d, so we don't need to
// do anything extra for this case.

bool progressive[n];

ll root(ll m) {
    return ll(round(sqrt(m)));
}

void divisors(VP &fact, ll m, ll r, int k) {
    if (r > m) return;
    ll d = m*m/r;
    ll test = m*d+r;
    ll sqr = root(test);
    if (test < n*n && sqr*sqr==test) {
        progressive[sqr] = true;
        return;
    }
    FOR(i,k,fact.SZ) {
        ll p=1;
        REP(j, 2*fact[i].second+1) {
            divisors(fact, m, r*p, i+1);
            p *= fact[i].first;
        }
    }
}

int main() {
    vector<VP> factor(n, VP());
    memset(progressive, false, sizeof(progressive));
    FOR(i,2,n) {
        if (factor[i].SZ > 0) continue;
        for (int j=i; j<n; j+=i) {
            int k=j;
            int m=0;
            while (k%i==0) {
                k /= i;
                m++;
            }
            factor[j].PB(PI(i,m));
        }
    }
    FOR(i,2,n) divisors(factor[i], i, 1, 0);
    ll total = 0;
    for (ll i=0; i<n; i++)  if (progressive[i]) {
        total += i*i;
    }
    cout << total << endl;
    return 0;
}      
