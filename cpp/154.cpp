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
typedef long long ll;

const int N = int(2E5);

int v2[N+1];
int v5[N+1];

int main() {
    int v2N, v5N;
    REP(i,N+1) {
        v2[i]=0;
        v5[i]=0;
        int t;
        int p2=2;
        int p5=5;
        while (t=i/p2) {
            v2[i] += t;
            p2*=2;
        }
        while (t=i/p5) {
            v5[i] += t;
            p5*=5;
        }
    }
    v2N=v2[N];
    v5N=v5[N];
    ll ans = 0;
    REP(i,N+1) {
        if (N-i<i) break;
        int t2 = v2N-v2[i];
        int t5 = v5N-v5[i];
        if (t2<12 || t5<12) continue;
        FOR(j,i,N+1-i) {
            int k = N-i-j;
            if (k<i||k<j) break;
            int tt2 = t2-v2[j]-v2[k];
            int tt5 = t5-v5[j]-v5[k];
            if (tt2 < 12 || tt5 < 12) continue;
            int s = (i==j)+(j==k)+(i==k);
            if (s==3) ans++;
            else if (s==1) ans+=3;
            else ans+=6;
        }
    }
    cout << ans << endl;
    return 0;
}
