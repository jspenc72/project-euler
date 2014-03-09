#include <stdio.h>
#include <stdlib.h>
#define N 50000000
#define X 100000000

char isPrime[N];

int main(void) {
    unsigned int *primes;
    unsigned int i,j,total=0,num=0;
    for (i=0; i<N; i++) isPrime[i]=1;
    isPrime[0]=isPrime[1]=0;
    for (i=2; i<N; i++) {
        if (!isPrime[i]) continue;
        for (j=i<<1; j<N; j+=i) isPrime[j]=0;
    }
    for (i=2; i<N; i++) if (isPrime[i]) num++;
    primes = (unsigned int*)malloc(num*sizeof(unsigned int));
    j=0;
    for (i=0; i<N; i++) {
        if (isPrime[i]) {
            primes[j++]=i;
        }
    }
    j=num-1;
    for (i=0; i<num; i++) {
        while (primes[i]*primes[j] > X) j--;
        if (i>j) break;
        total += (j-i+1);
    }
    free(primes);
    printf("%u\n", total);
}
