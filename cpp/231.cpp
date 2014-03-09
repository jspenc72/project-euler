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
const int M = 15000001;
const int N = 20000001;
const int P = N-M+1;

using namespace std;

typedef vector<int> VE;

int main() {
    VE smallprime(N,0);
    unsigned long long total=0;
    FOR(i,2,N) {
        if (smallprime[i]!=0) continue;
        for (int j = i; j < N; j += i) {
            if (smallprime[j]!=0) continue;
            smallprime[j] = i;
        }
    }
    FOR(i,MIN(M,P),N) {
        int n = i;
        int p;
        while (n!=1) {
            p = smallprime[n];
            total += p;
            n /= p;
        }
    }
    FOR(i,2,MAX(M,P)) {
        int n = i;
        int p;
        while (n!=1) {
            p = smallprime[n];
            total -= p;
            n /= p;
        }
    }
    cout << total << endl;
    return 0;
}
