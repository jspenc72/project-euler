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

int issquare(ull n) {
    int rem = n&0xF;
    if (rem==0 || rem==1 || rem==4 || rem==9) {
        ull r = round(sqrt(n));
        if (r*r==n) return r;
    }
    return 0;
}

int main() {
    int k=0;
    ull n=0;
    int r, x;
    while (k<15) {
        n++;
        if (issquare(5*n*n+2*n+1)) {
            k++;
            cout << n << endl;
        }
    }
    cout << n << endl;
    return 0;
}
