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

const int p = 1009;
const int q = 3643;
const int phi = (p-1)*(q-1);
const int n = p*q;
const int lam = 611856;

int unconcealed[phi] = {0};
int freq[phi] = {0};
VE divs;

int modpow(ll a, int k) {
    ll ret=1;
    while (k>0) {
        if (k&1) ret = (ret*a)%n;
        k >>= 1;
        a = (a*a)%n;
    }
    return ret;
}
//int order[n] = {-1};

//int findroot(int m) {
//    if (m==1) return 0;
//    int &ret = root[m];
//    if (ret!=-1) return ret;
//    return ret=1+findroot(
//}

int order(int m) {
    int t=1;
    int exp=0;
    REP(i,divs.SZ) {
        t = t*modpow(m,divs[i]-exp)%n;
        exp=divs[i];
        if (t==1) return exp;
    }
    return -1;
}

int gcd(int x, int y) {
    while (y!=0) {
        int t=x;
        x = y;
        y = t%y;
    }
    return x;
}

int main() {
    FOR(d,1,lam+1) if (!(lam%d)) {
        divs.PB(d);
    }
    REP(m,n) {
        if (!(m%10000)) cout << m << endl;
        if (!(m%p) || !(m%q)) continue;
        freq[order(m)]++;
    }
    REP(i,phi) {
        if (freq[i]==0) continue;
        for (int e=i+1; e<phi; e+=i)
            unconcealed[e] += freq[i];
    }
    ll total=0;
    int small = 1<<30;
    FOR(e,2,phi) {
        if (gcd(e,phi)>1) continue;
        int u = unconcealed[e];
        if (u==small) total+=e;
        if (u<small) {
            small = u;
            total = e;
        }
    }
    cout << total << endl;
    return 0;
}
