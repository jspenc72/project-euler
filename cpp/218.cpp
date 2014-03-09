#include <iostream>

using namespace std;
typedef long long ll;

const ll N = 100000000;

ll gcd(ll a, ll b) {
    ll t;
    while (b) {
        t = a;
        a = b;
        b = t%b;
    }
    return a;
}

int main() {
//    ll ans = 0;
//    for (ll m=1; m*m<N; m++) {
//        for (ll n=1; n<m; n++) {
//            if (gcd(m,n) > 1 || (m+n)%2==0) continue;
//            if (m*m + n*n > N) break;
//            ll m1 = m*m-n*n;
//            ll n1 = 2*m*n;
//            if ((m1+n1)%2==0) continue;
//            ll a = m1*m1-n1*n1;
//            if (a<0) a*=-1;
//            ll b = 2*m1*n1;
            // it turns out that every perfect triplet
            // ... is also superperfect.
            // Area = 2*m*n*(m^2 - n^2)*(m^4 + n^4 - 6*m^2*n^2),
            // where m, n coprime, opposite parity
            // this is == 0 (mod 6) and == 0 (mod 28)
//        }
//    }
    cout << 0 << endl;
}
