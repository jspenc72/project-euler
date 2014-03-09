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

const int N = int(1E6)+50;
const int last = 999983;
const ull M = 999966663333;
bool prime[N];

int main() {
    VE parr;
    memset(prime,true,N);
    prime[0]=prime[1]=false;
    for (int i=2; i*i < N; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<N; j+=i) prime[j] = false;
    }
    FOR(i,2,N) if(prime[i]) parr.PB(i);
    ull total=0;
    ull next;
    ull p1, p2;
    REP(i,parr.SZ) {
        p1 = parr[i];
        p2 = parr[i+1];
        ull x = (p1*p1 + p2-1)/p2;
        ull y = p2*p2/p1;
        total += p2*((p2-1)*p2/2 - (x-1)*x/2);
        total += p1*(y*(y+1)/2 - p1*(p1+1)/2);
        if (p1!=last) total -= 2*p1*p2;
        if (p2==last) {
            p1 = p2;
            p2 = parr[i+2];
            break;
        }
    }
    /* next section not actually necessary for given parameters */
    ull x = (p1*p1 + p2-1)/p2;
    for (ull i=x; i*p2 < M; i++) {
        if (i==p1) continue;
        total += p2*i;
    }
    ull y = p2*p2/p1;
    for (ull i=p1+1; i<y; i++) {
        if (i==p2) continue;
        if (p1*i >= M) break;
        total += p1*i;
    }
    cout << total << endl;
    return 0;
}
