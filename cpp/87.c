#include <stdio.h>
#include <stdlib.h>
#define LIMIT 50000000

int main() {
    int i,j,k,count;
    int p1,p2,p3;
    unsigned int combo;
    int *primes;
    char isPrime[7080];
    char *able;
    able = (char*)malloc(LIMIT*sizeof(char));
    for (i=0; i<LIMIT; i++) able[i]=0;
    for (i=2; i<7080; i++) isPrime[i] = 1;
    for (i=2; i<7080; i++) {
        if (!isPrime[i]) continue;
        for (j=2*i; j<7080; j+=i) isPrime[j]=0;
    }
    count = 0;
    for (i=2; i<7080; i++)
        if (isPrime[i]) count++;
    primes = (int*)malloc(count*sizeof(int));
    j=0;
    for (i=0; i<7080; i++) {
        if (isPrime[i]) {
            primes[j]=i;
            j++;
        }
    }
    for (i=0; i<count; i++) {
        for (j=0; j<count; j++) {
            for (k=0; k<count; k++) {
                p1 = primes[i];
                p2 = primes[j];
                p3 = primes[k];
                combo = p1*p1 + p2*p2*p2 + p3*p3*p3*p3;
                /*if (combo==13) printf("%d %d %d\n", p1, p2, p3);*/
                /*printf("%d %d %d %u\n", p1, p2, p3, combo);*/
                if (p1 < 7072 && p2 < 369 && p3 < 85 && combo < LIMIT && combo > p1 && combo > p2 && combo > p3) able[combo] = 1;
            }
        }
    }
    count=0;
    for (i=0; i<LIMIT; i++)
        if (able[i]) { 
            count++;
            /*printf("%d\n", i);*/
        }
    printf("%d\n", count);
    return 0;
}
