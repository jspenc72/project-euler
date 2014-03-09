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

using namespace std;
typedef vector<int> VE;
typedef long long ll;

const int N = 1E6+1;
int prime[N];

set<int> divisors(int n) {
    set<int> ret;
    ret.insert(1);
    if (n==1) return ret;
    int p = prime[n];
    set<int> div = divisors(n/p);
    for (set<int>::iterator it=div.begin(); it!=div.end(); ++it) {
        ret.insert(*it);
        ret.insert(p* (*it));
    }
    return ret;
}

bool good(ll d1, ll d2, int c) {
    ll a = (d2+d1)/2;
    ll b = (d2-d1)/2;
    return a*a-b*b==c;
}

int divsEven(int n) {
    //number of even divisors of d of n with d^2 < n, O(sqrt(n))
    int ret=0;
    for (int d=2; d*d<n; ret+=(n%(2*d)==0), d+=2);
    return ret;
}

int main() {
    memset(prime,0,sizeof prime);
    prime[0]=prime[1]=1;
    VE parr;
    for (int i=2; i<N; i++) {
        if (prime[i]) continue;
        prime[i]=i;
        for (int j=i<<1; j<N; j+=i) prime[j] = i;
    }
    int total=0;
    for (int i=4; i<N; i+=4) {
//        if (!(i%1000)) cout << i << endl;
//        set<int> div = divisors(i);
        int num=0;
//        for (set<int>::iterator it=div.begin(); it!=div.end(); ++it) {
//            int d1 = *it;
//            int d2 = i/d1;
//            if (d1 >= d2) break;
//            if (!(d1&1 || d2&1)) num++;
//        }
        num = divsEven(i);
        if (1<=num && num<=10) total++;
    }
    cout << total << endl;
    return 0;
}
