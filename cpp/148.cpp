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

const long long ROWS = pow(10,9);

long long smallerfit(long mod) {
    long long smaller = (mod-1)*(mod-2)/2;
    return smaller*7*6/2;
}

int main() {
    long long div=0;
    int count;
    int mult=1;
    int mod=7;
    while (mod<ROWS) {
        count=mod-1;
        FOR(r,mod+1,ROWS+1) {
        for (int r=mod+1; r<ROWS+1;) {
            if (!(r%1000000)) cout << r << endl;
            div += mult*count;
            count = (count-1+mod)%mod;
            if (!count) mult++;
            r += mod;
        }
        mod *= 7;
    }
    long long entries = ROWS*(ROWS+1)/2;
    cout << entries-div << endl;
    return 0;
}
