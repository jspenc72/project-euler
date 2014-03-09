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
typedef unsigned long long ull;
const int oo = INT_MAX>>1;

int phi[] = { 1475789056, 632481024, 180708864, 51631104,
              14751744, 4214784, 1204224, 344064, 98304,
              32768, 16384, 8192, 4096, 2048, 1024, 512,
              256, 128, 64, 32, 16, 8, 4, 2, 1 };

ull modpow(int a, int n, int mod) {
    if (n==0) return 1;
    ull temp;
    if (n&1) {
        temp = modpow(a,(n-1)/2,mod);
        return temp*temp%mod*a%mod;
    }
    temp = modpow(a,n/2,mod);
    return temp*temp%mod;
}

ull tet(int a, int b, int m) {
    if (b==1) return a%phi[m];
    if (phi[m]==1) return 1;
    return modpow(a, tet(a,b-1,m+1), phi[m]);
}

typedef vector<int> VE;

int main() {
    ull total = (11+((int)pow(2,6)-3)%phi[0]+(tet(2,7,0)-3)%phi[0])%phi[0];
    FOR(i,5,7) total = (total+tet(2,100,0)-3)%phi[0];
    cout << total << endl;
    return 0;
}
