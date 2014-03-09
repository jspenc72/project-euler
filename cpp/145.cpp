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

int N = 1000000000;

bool reversible(int n) {
    if (!(n%10)) return false;
    int m = n;
    int r = 0;
    while (m != 0) {
        r = r*10 + m%10;
        m /= 10;
    }
    m = r+n;
    while (m != 0) {
        r = m%10;
        if (!(r&1)) return false;
        m /= 10;
    }
    return true;
}

int main() {
    int total=0;
    REP(i,N) {
        if (!(i%100000000)) cout << i << endl;
        if (reversible(i)) total++;
    }
    cout << total << endl;
    return 0;
}
