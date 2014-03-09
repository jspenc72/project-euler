#include <algorithm>
#include <iostream>
#include <cmath>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SZ size()
#define PB push_back

//the key insight here is that, given a+bi with d=gcd(a,b),
//the first natural number this divides is (a^2+b^2)/d

//furthermore, (a^2+b^2)/d == ((a'd)^2+(b'd)^2)/d where
//gcd(a',b') == 1. This is simply (a'^2+b'^2)*d, so everything
//can be expressed as a product of these "primitive" Gaussian
//integers multiplied by some constant factor.

using namespace std;
typedef long long ll;
const int n = pow(10,8);

int main() {
    ll total = 0, first;
    //get sum of all real divisors
    for (int r=1; r<=n; r++) {
        total += (n/r)*r;
    }

    //now iterate over gaussian integers with
    //coprime compenents, where a is the larger
    //of the two components
    for (int a=1; a*a<=n; a++) {
        for (int b=1; b<=a; b++) {
            if (__gcd(a,b) > 1) continue;
            int c = a*a+b*b, first;
            int add = (a==b?2*a:2*(a+b));
            for (int i=1; (first=i*c)<=n; i++) {
                total += (n/(first))*i*add;
            }
        }
    }
    cout << total << endl;
    return 0;
}
