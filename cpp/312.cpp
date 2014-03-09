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
typedef unsigned long long ull;

ull phi[] = { 815730721, 752982204, 231686832,
 71288256, 21934848, 6749184, 2076672,
  638976, 196608, 65536 };

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

ull c(int ord, int n, int m) {
    if (ord==0) return n%phi[m];
    ull cnext = c(ord-1, n, m+2);
    ull temp = modpow(3, cnext-2, phi[m+1]);
    return modpow(2, temp, phi[m]) * modpow(3, (temp-3)/2, phi[m]) % phi[m];
}

int main() {
    cout << c(3, 10000, 0) << endl;
    return 0;
}
