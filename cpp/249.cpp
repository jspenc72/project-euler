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
typedef unsigned long long ull;
ull mod = pow(10,16);
const int M=5000;
ull *mem[M];

inline int modn(int n, int m) {
    return n>=0 ? n%m : (n%m)+m;
}

int main() {
    VE parr;
    vector<bool> prime(M,true);
    prime[0]=prime[1]=false;
    for (int i=2; i*i<M; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<M; j+=i) prime[j]=false;
    }
    REP(i,M) if (prime[i]) parr.PB(i);
    int n = parr.SZ;
    int total=0;
    REP(i,n) total+=parr[i];
    REP(i,M) mem[i] = new ull[n+1];
    prime = vector<bool>(total+1,true);
    prime[0]=prime[1]=false;
    for (int i=2; i*i<=total; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<=total; j+=i) prime[j]=false;
    }
    ull ans = 0;
    fill(mem[0],mem[0]+n+1,1);
    FOR(i,1,M) fill(mem[i],mem[i]+n+1,0);
    FOR(i,2,total+1) {
        int num=i%M;
        mem[num][n]=0;
        for (int j=n-1; j>=0; j--)
            mem[num][j] = (mem[modn(num-parr[j],M)][j+1] + mem[num][j+1])%mod;
        if (prime[i]) ans = (ans+mem[num][0])%mod;
    }
    cout << ans << endl;
    return 0;
}
