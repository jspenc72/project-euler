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
typedef vector<ull> VE;

const int N = 64000000;
VE divsum(N,1);

bool psquare(ull n) {
    ull root = round(sqrt(n));
    return root*root==n;
}

int main() {
    for (ull i=2; i<N; i++) {
        for (int j=i; j<N; j+=i) {
            ull old = divsum[j];
            divsum[j] += i*i;
        }
    }
    ull total = 0;
    FOR(i,1,N) if (psquare(divsum[i])) total += i;
    cout << total << endl;
    return 0;
}
