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
const ull M = 100000002;
const ull N = M-1;

int main() {
    vector<bool> prime(M,true);
    vector<bool> good(N,true);
    prime[0]=prime[1]=false;
    for (int i = 0; i*i < M; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j < M; j += i) prime[j] = false;
    }
    FOR(i,1,N) {
        for (int j = i; j < N; j += i) {
            if (!good[j]) continue;
            int test = i+j/i;
            if (prime[test]) continue;
            //cout << j << " " << i << " " << test << endl;
            good[j] = false;
        }
    }
    ull total=0;
    FOR(i,1,N) if (good[i]) total += i;
    cout << total << endl;
    return 0;
}
