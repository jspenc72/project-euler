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
#define FOREACH(_i,_a) for (__typeof(_a.begin()) _i=_a.begin();_i!=_a.end();++_i)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MAX3(a,b,c) MAX(MAX(a,b),c)
#define MAX4(a,b,c,d) MAX(MAX3(a,b,c),d)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MIN3(a,b,c) MIN(MIN(a,b),c)
#define MIN4(a,b,c,d) MIN(MIN3(a,b,c),d)
#define SZ size()
#define PB push_back

const int oo = INT_MAX>>1;
const int N = 2E7;

using namespace std;

typedef vector<int> vi;
typedef vector<bool> vb;
typedef pair<int,int> pii;
typedef vector<pii> vp;

typedef long long ll;

/**************************************************
 * Strategy: for each 3 <= n <= 2E7, we want to
 *           find the minimal integer x such that:
 *
 *           x >= 1
 *           (n-1-x)^2 == 1 (mod n)
 *
 *           This is true iff n divides x*(x+2),
 *           details omitted. So we just loop over
 *           x, factorize x*(x+2), and check all
 *           divisors, setting the value of x if
 *           that divisor has not been covered yet.
 */

int I[N+1];
const int M=N; // shouldn't need to factorize anything higher than N
int smallprime[M+1];
int remaining=N-2; // 3<=n<=N

vp factorize(int x) {
    vp factors;
    while (x > 1) {
        int p = smallprime[x];
        pii factor(p,0);
        while (x>1 && smallprime[x] == p) {
            x /= p;
            factor.second++;
        }
        factors.PB(factor);
    }
    return factors;
}

void all_divisors(vp &primes, int i, int cur, int x) { // call with 0, 1 to start
    if (cur > N) return;
    if (cur <= 0) {
        cerr << "Error: multiplication overflow" << endl;
        exit(1);
    }
    if (i >= primes.SZ) {
        if (cur >= 3 && cur-1-x >= 1 && I[cur]==-1) {
            I[cur] = cur-1-x;
            remaining--;
        }
        return;
    }
    ll m = 1;
    int p = primes[i].first;
    all_divisors(primes, i+1, cur, x);
    REP(j,primes[i].second) {
        m *= p;
        if (cur*m > N) break;
        all_divisors(primes, i+1, cur*m, x);
        if (remaining==0) break;
    }
}

void printfactors(int v, vp &x) {
    cout << "factors of " << v << ": ";
    for (int i=0; i<x.SZ; i++) {
        cout << x[i].first << "^" << x[i].second << ",";
    }
    cout << endl;
}

vp agg_factors(vp first, vp second) {
    vp agg;
    int i=0, j=0;
    while (i<first.SZ || j<second.SZ) {
        pii aggf;
        if (j==second.SZ || (i<first.SZ && first[i].first < second[j].first)) {
            aggf.first = first[i].first;
            aggf.second = first[i].second;
            i++;
        } else if (i==first.SZ || (j<second.SZ && first[i].first > second[j].first)) {
            aggf.first = second[j].first;
            aggf.second = second[j].second;
            j++;
        } else { // equal
            aggf.first = first[i].first;
            aggf.second = first[i].second + second[j].second;
            i++;
            j++;
        }
        agg.PB(aggf);
    }
    return agg;
}

int main() {
    memset(smallprime,-1,sizeof smallprime);
    memset(I,-1,sizeof I);
    for (int i=2; i<=M; i++) {
        if (smallprime[i]!=-1) continue;
        for (int j=i; j<=M; j+=i) {
            if (smallprime[j]==-1) smallprime[j]=i;
        }
    }
    for (int x=1; remaining>0; x++) {
        if (x+2>M) {
            cerr << "Error: did not factorize up to " << (x+2) << endl;
            exit(1);
        }
        vp first = factorize(x);
        vp second = factorize(x+2);
        vp factors = agg_factors(factorize(x), factorize(x+2));
        all_divisors(factors, 0, 1, x);
    }
    ll tot=0;
    for (int i=3; i<=N; i++) {
        tot += I[i];
    }
    cout << tot << endl;
    exit(0);
}
