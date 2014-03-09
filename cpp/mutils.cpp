#include "cstdlib"
#include "mutils.h"

unsigned int lg(unsigned int v) {
    register unsigned int r = 0; //result of log2(v) will go here
    for (int i = 4; i >= 0; i--) { //unroll for speed...
        if (v & b[i]) {
            v >>= S[i];
            r |= S[i];
        }
    }
    return r;
}

int randnorm() {
    int sum = 0;
    int sign;
    for (int i = 0; i < 10; i++) {
        sign = (rand()&1) ? 1 : -1;
        sum += sign*(rand()%1000);
    }
    return sum + 5000;
}
