#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <cassert>
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

const long long oo = LLONG_MAX>>1ll;

using namespace std;

typedef vector<int> vi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<ll,int> pii;

const int N = int(pow(10ll,7.8));
const ll STOP = ll(pow(10ll,15));

vb prime;
vi primes;

vector<pii> factor(ll n) {
    vector<pii> ret;
    FOREACH(p,primes) {
        if (n% *p > 0) continue;
        int vp=0;
        while (n%*p == 0) {
            n /= *p;
            vp++;
        }
        ret.PB(pii(*p,vp));
        if (n>1) continue;
        break;
    }
    assert(n==1 || n < ll(N-1)*ll(N-1)); // make sure we have enough primes
    if (n>1) ret.PB(pii(n,1));
    return ret;
}

ll gcd(ll x, ll y) {
    ll t;
    while (y) {
        t = x;
        x = y;
        y = t%y;
    }
    return x;
}

int main() {
    prime = vb(N, true);
    prime[0]=prime[1] = false;
    for (int i=0; i*i<N; i++) {
        if (!prime[i]) continue;
        for (int j=i*i; j<N; j+=i) prime[j] = false;
    }
    REP(i,N) if (prime[i]) primes.PB(i);

    ll cur=100; // keeping track of where we are

    ll n=5;
    ll gn=13;
    while (true) {
        ll g = gcd(n,gn);
        if (n==cur+1) {
            cout << gn << endl;
            if (cur==STOP) break;
            cur *= 10;
        } else if (g > 1) {
            n++;
            gn += g;
        } else {
            if (n > STOP) assert(false);
            ll diff = gn-n;
            vector<pii> factors = factor(diff);
            ll leap = oo;
            FOREACH(it,factors) {
                leap = min(leap, it->first - gn%it->first);
            }
            if (n + leap > cur) {
                cout << gn + (cur-n) + 1 << endl;
                if (cur==STOP) break;
                cur *= 10;
            }
            n+=leap;
            gn+=leap;
        }
    }
    return 0;
}
