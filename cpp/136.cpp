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
const int N = 50000000;
//const int N = 100;

bool test(int n) {
    int d;
    int c = 0;
    for (int i = 1; (d=n/i) >= i; i++) {
       if (i*d==n && (i+d)%4 == 0) {
           c++;
           if (i != d && 3*i > d) return false;
       }
       if (c > 1) return false;
    }
    return c==1;
}

int main() {
    int total = 0;
    for (int i = 1; i < N; i++) {
        if (!(i%10000)) cout << i << endl;
        if (test(i)) total++;
    }
    cout << total << endl;
}
