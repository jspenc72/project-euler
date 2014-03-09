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
typedef bitset<26> SET;

struct node {
    int s;
    int r;
    bool c;
    int n;
    node(int ss, int rr, bool cc, int nn) {
        s = ss; r = rr; c = cc; n = nn;
    }
    bool operator<(const node &comp) const {
        if (c && !comp.c) return true;
        else if (!c && comp.c) return false;
        else {
            if (s < comp.s) return true;
            else if (comp.s < s) return false;
            else {
                if (r < comp.r) return true;
                else if (comp.r < r) return false;
                else return n < comp.n;
            }
        }
    }
};

typedef map<node,int> MEM;
MEM mem;

int ways(int used, int prev, bool consec, int n) {
    if (n==26) {
        if (consec) return 1;
        else return 0;
    }
    node lookup(used, prev, consec, n);
    if (mem.find(lookup) != mem.end()) return mem[lookup];
    int total = 0;
    int r = consec ? prev : 26;
    REP(i,r) {
        int test = 1<<i;
        if (used&test) continue;
        if (i>prev || consec) total += ways(used, i, true, n+1);
        else {
            total += ways(used|test, i, false, n+1);
        }
    }
    return mem[lookup]=total;
}

int main() {
    cout << ways(0,26,false,20) << endl;
    return 0;
}
