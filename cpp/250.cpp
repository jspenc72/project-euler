#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
typedef unsigned long long ull;
typedef long long ll;
const ull mod = pow(10,16);
const int D = 250;
const int M = 250250;
ll mem[2][D];
int arr[M];

int modpow(int n, int p, int m) {
    int t;
    if (p==0) return 1;
    if (p&1) {
        t = modpow(n, (p-1)/2, m);
        return t*t%m*n%m;
    }
    else {
        t = modpow(n, p/2, m);
        return t*t%m;
    }
}

int main() {
    REP(i,M) arr[i] = modpow(i+1,i+1,D);
    memset(mem,0,sizeof(mem));
    mem[0][0]=1;
    for (int i = M-1; i>=0; i--)
        REP(j,D) mem[i%2][j]=(mem[(i+1)%2][j]+mem[(i+1)%2][(j+arr[i])%D])%mod;
    cout << mem[0][0]-1 << endl;
    return 0;
}
