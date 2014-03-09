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

const int oo = INT_MAX>>1;
const int N = 1000100;

int digits(int n) {
    int d = 1;
    while ((n/=10) != 0) d++;
    return d;
}

int main() {
    vector<bool> prime(N,true);
    prime[0]=prime[1]=false;
    for (int i = 0; i*i<N; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j<N; j+=i) prime[j]=false;
    }
    long long total=0;
    for (int p1 = 5; p1 <= 1000000;) {
        int p2 = p1+2;
        while (!prime[p2]) p2++;
        int m = pow(10,digits(p1));
        long long k = 1;
        while ((k*m+p1) % p2 != 0) k++;
        total += (k*m+p1);
        //cout << p1 << " " << p2 << " " << k*m+p1 << endl;
        do {p1++;} while(!prime[p1]);
    }
    cout << total << endl;
    return 0;
}
