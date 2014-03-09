#include <algorithm>
#include <iostream>
#include <climits>
#include <cmath>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;
typedef unsigned long long ull;

const int D = 10;
const int M = pow(10,D-1);
const int N = pow(10,D/2+(D&1));
vector<bool> prime(N,true);
VE parr;

bool isprime(ull n) {
    REP(i,parr.SZ) {
        ull p = parr[i];
        if (p*p > n) break;
        if (n%p==0) return false;
    }
    return true;
}

ull allpossible(VE &digits, int i, int j, int n, int d) {
    if (j==n) {
        ull num = 0;
        REP(k,digits.SZ) num = num*10+digits[k];
        if (num >= M && isprime(num)) return num;
        return 0;
    }
    int k = i;
    while (digits[++k] != -1);
    ull ret = 0;
    REP(h,10) {
        if (h==d || (h==0 && k==0)) continue;
        digits[k]=h;
        ret += allpossible(digits, k, j+1, n, d);
    }
    digits[k]=-1;
    return ret;
}

ull findsum(int n, int d) {
    VE digits(D,d);
    REP(i,D-n) digits[i]=-1;
    ull ret=0;
    do {
        if (digits[0]==0) continue;
        ret += allpossible(digits, -1, 0, D-n, d);
    } while(next_permutation(digits.begin(),digits.end()));
    return ret;
}

int main() {
    prime[0]=prime[1]=false;
    for (int i = 2; i*i < N; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j < N; j += i) prime[j] = false;
    }
    for (int i = 0; i < N; i++) if (prime[i]) parr.PB(i);
    ull total=0;
    REP(d,10) {
        int n = D-1;
        ull s = 0;
        do {
            s = findsum(n,d);
            n--;
        } while (s==0);
        total += s;
    }
    cout << total << endl;
    return 0;
}
