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
typedef unsigned long long ull;


//const int N = 50000001;
const int N = 10001;
const int M = 71000000;

int main() {
    vector<bool> prime(M,true);
    vector<bool> tprime(N,true);
    VE parr;
    prime[0]=prime[1]=false;
    tprime[0]=tprime[1]=false;
    for (int i = 2; i*i<M; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j < M; j+=i) prime[j]=false;
    }
    REP(i,M) if (prime[i]) parr.PB(i);
    for (ull i = 0; i < N; i++) {
        if (!(i%10000)) cout << i << endl;
        if (!tprime[i]) continue;
//        int p = 2*i*i-1;
        ull p = 2*i*i-1;
        for (int j = 0; j < parr.SZ; j++) {
            int tp = parr[j];
            if (tp*tp > p) break;
            if (p % tp == 0) {
//                cout << i << " " << p << " " << parr[j] << endl;
                p = tp;
                tprime[i] = false;
                break;
            }
        }
        long long a = p-2*i;
        while (a<0) a+=p;
//        int b = p+i;
        long long b = 2*(p-i-a);
        while (b<0) b+=p;
//        cout << i << " " << p << " " << a << " " << b << endl;
        bool par = true;
        for (ull j = i+a; j < N; j += (par ? a : b)) {
            par = !par;
            if (j >= N || j < 0) cout << j << endl;
            tprime[j] = false;
        }
    }
    int total = 0;
    REP(i,N) if (tprime[i]) total++;
    cout << total << endl;
    return 0;
}
