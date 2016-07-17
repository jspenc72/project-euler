#include <cstdio>
#include <map>

typedef long long ll;

std::map<ll,double> mem;

#define N 10000000000LL

// not much to say here. both of these fall directly out of recurrences.
// takes ~100s as of this writing

double b(ll n) {
    if (n==0) return 0.;
    if (n==1) return 1.;
    if (mem.find(n) != mem.end()) return mem[n];
    ll guess = (n+1)/2;
    double ans = 1. + double(guess-1)/n * b(guess-1) + double(n-guess)/n * b(n-guess);
    return (mem[n] = ans);
}

// see forum for how to express this n terms of nth harmonic number H_n
// H_n can be calculated quickly with asymptotic expansion
double r(ll n) {
    double x=0.;
    double s=0.;
    for (ll i=1; i<=n; i++) {
        x = 1. + 2./i * s/i;
        s += i*x;
    }
    return x;
}


int main() {
    printf("%.8f", r(N) - b(N));
    return 0;
}
