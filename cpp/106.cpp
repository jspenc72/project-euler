#include <cstdio>

int fact(int n) {
    if (n<=1) return 1;
    return n*fact(n-1);
}
int combin(int n, int k) {
    return fact(n)/(fact(k)*fact(n-k));
}
int main() {
    int n, k, ms;
    n=12;
    ms = 0;
    for( k=2 ; k<=n/2 ; k++ )
        ms += combin(n,2*k)*combin(2*k-1, k+1);
    printf("%2d: %10d\n", n, ms);
    return 0;
}
