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
const float e = 2.718281828;
const int N=1E4+1;

int best(int n, int m) {
    return (m+1)*log(m+1)>log(n)+m*log(m)?m:m+1;
}

bool nonrepeat(int m) {
    while (!(m&1)) m/=2;
    while (!(m%5)) m/=5;
    return m==1;
}

int gcd(int x, int y) {
    int t;
    while (y!=0) {
        t=x;
        x=y;
        y=t%y;
    }
    return x;
}

int main() {
    int total=0;
    FOR(i,5,N) {
        int m = best(i, int(i/e));
        total += (nonrepeat(m/gcd(i,m))?-i:i);
    }
    cout << total << endl;
}
