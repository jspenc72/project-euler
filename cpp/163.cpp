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

// Basic idea is to generate all segments (by end points)
// and then find all triangles by looking at all triples
// and seeing if they (1) mutually intersect and (2) don't
// share common endpoints. Then we have to subtract off triples
// that don't share endpoints but still intersect at a point.
// (Should be number of building block triangles.)
// Hard part will be generating segments.

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}
