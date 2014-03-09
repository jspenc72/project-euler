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
#define MIM(a,b) ((a)<(b)?(a):(b))
#define MIM3(a,b,c) MIM(MIM(a,b),c)
#define MIM4(a,b,c,d) MIM(MIM3(a,b,c),d)
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
typedef long long ll;

const int M = 5000;
const ll N = 1E18;
const ll K = 1E9;

pair<int, pair<int, int> > extendedEuclid(int a, int b) {
	int x = 1, y = 0;
	int xLast = 0, yLast = 1;
	int q, r, m, n;
	while(a != 0) {
		q = b / a;
		r = b % a;
		m = xLast - q * x;
		n = yLast - q * y;
		xLast = x, yLast = y;
		x = m, y = n;
		b = a, a = r;
	}
	return make_pair(b, make_pair(xLast, yLast));
}

int modInverse(int a, int m) {
    return (extendedEuclid(a,m).second.first + m) % m;
}

int choose(int n, int k, int p) {
    int ans=1;
    FOR(i,k+1,n+1) ans = (ans*i)%p;
    int den=1;
    FOR(i,2,n-k+1) den = (den*i)%p;
    ans = (ans*modInverse(den,p))%p;
    return ans;
}

int lucas(ll n, ll k, int p) {
    int ans=1;
    while (n!=0) {
        int num = n%p;
        int den = k%p;
        if (num<den) return 0;
        n/=p; k/=p;
        ans = (ans*choose(num,den,p))%p;
    }
    return ans;
}

ll cra(ll r1, ll r2, ll m1, ll m2) {
    ll c = modInverse(m1,m2);
    ll s = c*(r2-r1+m2)%m2;
    return r1+s*m1;
}

int main() {
    bool prime[M];
    int C[M];
    memset(prime,true,sizeof prime);
    prime[0]=prime[1]=false;
    for (int i=2; i*i<M; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<M; j+=i) prime[j]=false;
    }
    VE parr;
    FOR(i,1001,M) if (prime[i]) parr.PB(i);
    REP(i,parr.SZ) {
        C[parr[i]] = lucas(N,K,parr[i]);
    }
    ll total=0;
    REP(i,parr.SZ) {
        int p = parr[i];
        FOR(j,i+1,parr.SZ) {
            int q = parr[j];
            ll pq = cra(C[p],C[q],p,q);
            FOR(k,j+1,parr.SZ) {
                int r = parr[k];
                ll pqr = cra(C[r],pq,r,p*q);
                total += pqr;
            }
        }
    }
    cout << total << endl;
    return 0;
}
