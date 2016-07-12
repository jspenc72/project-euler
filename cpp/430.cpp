#include <cstdio>
#include <cmath>

// for probability disk at position k is white after M moves:
// ref: http://mathoverflow.net/questions/16187/binomial-distribution-parity

typedef long long ll;
typedef long double ld;

ld E(ll N, ll M, bool approx=false) {
    ld ans = .5 * N;
    for (ll k=1; k <= (approx ? N/100 : N); k++) {
        ld pwhite = (2.*k*(N-k+1) - 1.) / N / N;
        ld t = pow(1. - 2.*pwhite, M);
        ans += approx ? t : .5*t;
    }
    return ans;
}

int main() {
//    printf("%.2Lf\n", E(100, 10));
    printf("%.2Lf\n", E(10000000000LL, 4000, true));
    return 0;
}
