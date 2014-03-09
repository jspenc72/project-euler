#include <algorithm>
#include <iostream>
#include <cstdio>
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

double mem[100][100];

// technique: top-down dp
// prob(i,j) is the probability
// that p2 wins with optimal play
// after p1 has $i and p2 has $j,
// with p2 going next (needed to
// calculate strategy for p2).
double prob(int i, int j) {
    if (j >= 100) return 1.;
    if (i >= 100) return 0.;
    double &ret = mem[i][j];
    if (ret != -1.) return ret;
    for (int t=1; t<=8; t++) {
        double win = pow(2.,-t);
        int reward = 1<<(t-1);
        ret = max(ret, (.5*win*prob(i,j+reward) + .5*win*prob(i+1,j+reward) + .5*(1-win)*prob(i+1,j))/(1-.5*(1-win)));
    }
    return ret;
}

int main() {
    REP(i,100) REP(j,100) mem[i][j]=-1.;
    printf("%.9f\n", .5*(prob(0,0) + prob(1,0)));
    return 0;
}
