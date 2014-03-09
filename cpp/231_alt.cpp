#include <iostream>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
typedef unsigned long long lint;

const int M = 15000001;
const int N = 20000001;
const int P = N-M+1;

lint nfactors(int n, int p) {
    lint ret = 0;
    while (n) ret += (n/=p);
    return ret;
}

int main() {
    vector<bool> prime(N,true);
    prime[0] = prime[1] = false;
    for (int i = 2; i*i < N; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j < N; j += i)
            prime[j] = false;
    }
    lint total=0;
    REP(i,N) if (prime[i])
        total += i*(nfactors(N-1,i) - nfactors(M-1,i) - nfactors(P-1,i));
    cout << total << endl;
    return 0;
}
