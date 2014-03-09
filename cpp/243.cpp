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

const ull N = ull(1E7);
const ull num=15499;
const ull den=94744;
//const ull N = 100;
//const ull num=4;
//const ull den=10;

VE smallprime(N,0);

int totient(int n) {
    int ret = n;
    while (n!=1) {
        int p = smallprime[n];
        while (p==smallprime[n]) n/=p;
        ret = ret/p*(p-1);
    }
    return ret;
}

//int totient(int n) {
//    int ret=n;
//    int start=1;
//    while (n!=1) {
//        if (n<N) {
//            int p=smallprime[n];
//            while (p==smallprime[n]) n/=p;
//            ret = ret/p*(p-1);
//            continue;
//        }
//        for (int p=start+1; p*p<=n; p++) {
//            if (n%p==0) { //p is smallprime[n]
//                while (!(n%p)) n/=p;
//                ret = ret/p*(p-1);
//                start=p;
//                goto skip;
//            }
//        }
//        //else: (n is prime)
//            ret = ret/n*(n-1);
//            n=1;
//        skip: continue;
//    }
//    return ret;
//}

int main() {
    FOR(i,2,N) {
        if (!(i%10000000)) cout << i << endl;
        if (smallprime[i]) continue;
        for (int j = i; j < N; j+=i)
            if (!smallprime[j]) smallprime[j]=i;
    }
    int d=1;
    FOR(d,2,N) {
        if (!(d%10000000)) cout << d << endl;
        int t = totient(d);
        if (t*den < (d-1)*num) {
            cout << d << endl;
            break;
        }
    }
    return 0;
}
