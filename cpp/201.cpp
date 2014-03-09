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

// f(x,y,z) = f(x-y*y,y-1,z-1) + f(x,y,z-1)

//const int mod = 12;
//const int K = 3;
//const int M = 6;
const int mod = 10001;
const int K = 50;
const int M = 100;
char f[mod][K+1][M+1];

int test[] = {1,3,6,8,10,11};

int main() {
    memset(f,0,sizeof f);
    int N=0;
    int tarr[M];
    REP(i,M) tarr[i] = (i+1)*(i+1);
    int *arr = tarr;
    REP(i,M) N+=arr[i];
    REP(i,M+1) f[0][0][i]=1;
    int total=0;
    FOR(i,1,N+1) {
        memset(f[i%mod],0,sizeof f[i%mod]); //reset this entry
        FOR(j,1,K+1) {
            FOR(k,1,M+1) {
                char val = f[(i-arr[k-1]+mod)%mod][j-1][k-1] + f[i%mod][j][k-1];
                f[i%mod][j][k] = (val>1?2:val);
            }
        }
        if (f[i%mod][K][M]==1) {
            total += i;
//            cout << i << endl;
        }
    }
    cout << total << endl;
    return 0;
}
