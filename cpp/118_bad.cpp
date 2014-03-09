#include <boost/dynamic_bitset.hpp>
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
const int N = 1000000000;

using namespace std;
using namespace boost;

typedef vector<int> VE;
typedef dynamic_bitset<> SET;

vector<bool> prime(N,false);
VE mem1(1<<10,-1);
VE mem2(1<<10,-1);

int numways(SET &s);

bool good(int n) {
    int mod;
    SET s(0);
    while (n != 0) {
        mod = n%10;
        n /= 10;
        if (mod==0) return false;
        if (s[mod]) return false;
        s[mod] = true;
    }
    return true;
}

int possible(SET &s) {
    unsigned long test = s.to_ulong();
    if (mem1[test] != -1) return mem1[test];
    VE perms;
    int total = 0;
    REP(i,s.SZ) if (s[i]) perms.PB(i);
    do {
        int num = 0;
        REP (i,perms.SZ) num = num*10 + perms[i];
        if (prime[num]) total++;
    } while (next_permutation(perms.begin(),perms.end()));
//    cout << s << " " << total << endl;
    return mem1[test] = total;
}

int allsubs(SET &start, SET &cur, int i) {
    if (i == 10) {
        int poss = possible(cur);
        if (poss > 0) {
            SET diff = start-cur;
            int ret = poss*numways(diff);
//            cout << diff << " " << poss << " " << ret << endl;
            return ret;
        }
        return 0;
    }
    if (!cur[i]) return allsubs(start,cur,i+1);
    int tot = 0;
    cur[i] = 0;
    tot += allsubs(start,cur,i+1);
    cur[i] = 1;
    tot += allsubs(start,cur,i+1);
    return tot;
}

int numways(SET &s) {
    unsigned long test = s.to_ulong();
    if (test == 4 || test == 8 || test == 32 || test == 128) return 1;
    if (mem2[test] != -1) return mem2[test];
    SET scpy = s;
    return mem2[test] = allsubs(s,scpy,0)/2;
}

SET makeset(int p) {
    SET s(10,0);
    while (p != 0) {
        s[p%10] = true;
        p /= 10;
    }
    return s;
}

int main() {
    int n;
//    prime[0] = prime[1] = false;
//    for (int i = 2; i*i <= N; i++) {
//        if (!prime[i]) continue;
//        for (int j = i<<1; j < N; j += i) prime[j] = false;
//    }
//    int count = 0;
//    REP(i,N) if (prime[i] && good(i)) {
//        cout << i << endl;
//        count++;
//    }
//    cout << count << endl;
    VE parr;
    while (cin >> n) {
        parr.PB(n);
    }
    vector<SET> arr;
    SET digits(10,(1<<10)-2);
//    SET next(10,0);
    //next[6] = next[3] = next[1] = true;
//    next[1] = next[2] = next[3] = next[5] = true;
//    cout << numways(next) << endl;
//    cout << numways(digits) << endl;
    SET empty(10,0);
    arr.PB(digits);
    cout << parr.SZ << endl;
    int total = 0;
    REP(i,parr.SZ) {
        cout << i << endl;
        SET test = makeset(parr[i]);
        int cursz = arr.SZ;
        REP(j,cursz) {
            if (test.is_subset_of(arr[j])) {
                SET diff = arr[j]-test;
                if (diff == empty) total++;
                else arr.PB(diff);
            }
        }
    }
    cout << total << endl;
    return 0;
}
