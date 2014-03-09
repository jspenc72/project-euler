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
#include <unordered_set>
#include <unordered_map>

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

typedef unordered_set<string> uset;

//void allsubs(string &base, string &add, uset &s, int i) {
//    if (i==base.length()) {
//        s.insert(add);
//        return;
//    }
//    FOR(j,1,base[i]+1) {
//        add[i]=j;
//        allsubs(base,add,s,i+1);
//    }
//}

int dilworth(string &base, string &add, uset &s, int i, int m) {
    if (s.SZ==m) return 1;
    if (i==base.length())
    int ret=oo;
    int old=add[i];
    FOR(j,add[i]+1,base[i]+1) {
        add[i]=j;
        if (s.find(add)!=s.end()) continue;
        s.insert(add);
        ret = dilworth(base, add, s, 0, m);
        add[i]=j;
        s.erase(add);
        break;
    }
    add[i]=old;
}

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}
