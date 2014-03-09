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

const int M = 1000000;
const int N = 1<<24;

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

int main() {
    vector<bool> prime(N,true);
    prime[0]=prime[1]=false;
    for (int i = 2; i*i<N; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j<N; j+=i) prime[j]=false;
    }
    cout << "phase 1" << endl;
    int cnt=0;
    int total=0;
    FOR(i,2,N) {
        if (prime[i] || i%2==0 || i%5==0) continue;
        int j;
        for (j=1; j<=i; j++) {
            if (modpow(10,j,9*i)==1) break;
        }
        if ((i-1)%j==0) {
            cnt++;
            //cout << i << " " << cnt << endl;
            total += i;
        }
        if (cnt==25) break;
    }
    cout << total << endl;
    return 0;
}
