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
typedef unsigned long long ull;
typedef vector<ull> VE;
const ull N = 150*pow(10,6);
//const ull N = pow(10,6);
const ull M = N+27;

const int tests[] = { 1, 3, 7, 9, 13, 27 };

bool isprime(ull num, VE &primes) {
    REP(i,primes.SZ) {
        ull p = primes[i];
        if (p*p > num) break;
        if (num%p==0) return false;
    }
    return true;
}

bool consecprimes(ull n, VE &primes) {
    ull square = n*n;
//    vector<bool> found(26, false);
    REP(i,primes.SZ) {
        ull p = primes[i];
        if (p*p > square+27) break;
        int mod = (n%p)*(n%p)%p;
        REP(j,6) if ((mod+tests[j])%p==0) return false;
//        if (!((mod+5)%p)) found[5]=true;
//        if (!((mod+11)%p)) found[11]=true;
//        for (int i=15; i<27; i+=2)
//            if (!((mod+i)%p)) found[i]=true;
    }
    if (isprime(square+5, primes)) return false;
    if (isprime(square+11, primes)) return false;
    for (int i=15; i<27; i+=2)
        if (isprime(square+i, primes)) return false;
//    if (!found[5]) return false;
//    if (!found[11]) return false;
//    for (int i=15; i<27; i+=2)
//        if (!found[i]) return false;
    return true;
}

int main() {
    vector<bool> prime(M, true);
    VE primes;
    prime[0]=prime[1]=false;
    for (int i=2; i*i<M; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<M; j+=i) prime[j]=false;
    }
    REP(i,M) if (prime[i]) primes.PB(i);
//    cout << primes.SZ << endl;
    ull total=0;
    int mod7;
    for (ull i=10; i<N; i+=10) {
//        if (i%10000==0) cout << i << endl;
        if (!(i%3)||(i-3)%7>1||!(i%13)) continue;
        if (consecprimes(i, primes)) total+=i;
    }
    cout << total << endl;
    return 0;
}
