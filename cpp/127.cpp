#include <iostream>
#include <climits>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SZ size()
#define PB push_back

const int oo = INT_MAX>>1;
using namespace std;
typedef vector<int> VE;
typedef vector<bool> VB;
typedef unsigned long long ull;
const int N = 120000;

int gcd(int x, int y) {
    int t;
    while (y!=0) {
        t = y;
        y = x%y;
        x = t;
    }
    return x;
}

int main() {
    vector<ull> rad(N,1);
    VB prime(N,true);
    vector<VE> hasrad(N, VE(0));
    prime[0]=prime[1]=false;
    REP(i,N) {
        if (!prime[i]) continue;
        rad[i] = i;
        for (int j = i<<1; j < N; j+=i) {
            prime[j] = false;
            rad[j] *= i;
        }
    }
    FOR(i,1,N) hasrad[rad[i]].PB(i);
    ull total = 0;
    bool found;
    FOR(c,3,N) {
        int upper = c/rad[c]+1;
        found = false;
        FOR(rb,2,upper) {
            REP(i,hasrad[rb].SZ) {
                int b = hasrad[rb][i];
                if (b >= c || 2*b <= c || gcd(c,b)>1) continue;
                int a = c-b;
                if (gcd(b,a)>1 || rad[a]*rad[b]*rad[c]>=c) continue;
                total += c;
            }
        }
    }
    cout << total << endl;
    return 0;
}
