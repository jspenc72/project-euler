#include <stdio.h>

int nimSum(unsigned int* heaps) {
    return heaps[0] ^ heaps[1] ^ heaps[2];
}

int main() {
    int i;
    unsigned int heaps[] = {1,2,3};
    unsigned int limit = 1<<30;
    int numLosses = 0;
    for (i=0; i<limit; i++) {
        numLosses += nimSum(heaps)==0;
        heaps[0] += 1;
        heaps[1] += 2;
        heaps[2] += 3;
    }
    printf("%d\n", numLosses);
    return 0;
}
