#include <iostream>

using namespace std;

// algorithm: for each triangle number,
// use prime multiplicity to compute
// number of divisors. break when this
// is greater than 500.

int main() {
    for (int i=1; ; i++) {
        int n = i*(i+1)/2;
        int t=n;
        int divs=1;
        for (int d=2; t>1; d++) {
            int j;
            for (j=0; !(t%d); j++) {
                t/=d;
            }
            divs *= (j+1);
        }
        if (divs>500) {
            cout << n << endl;
            break;
        }
    }
    return 0;
}
