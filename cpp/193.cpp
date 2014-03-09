#include <iostream>
#include <climits>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SZ size()
#define PB push_back

using namespace std;

typedef long long ll;
typedef vector<ll> VE;

const ll M = (1ll<<50)-1;
const ll N = 1ll<<25;

int main() {
    VE div(N,0);
    for (ll i = 2; i < N; i++) {
        if (div[i] != 0) continue;
        for (ll j = i*i; j < N; j += i*i) div[j]=-1;
        for (ll j = i; j < N; j += i) if (div[j]!=-1) div[j]++;
    }
    ll total=0;
    for (ll i=2; i<N; i++) {
        if (div[i]==-1) continue;
        ll test = M/(i*i);
        if (div[i]&1) total += test;
        else total -= test;
    }
    cout << M-total << endl;
    return 0;
}
