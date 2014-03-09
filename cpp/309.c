#include <stdio.h>

double N = 1000000.0;
double mem[20000][10000];
double f(int,int);

int main() {
    int i,j;
    for (i=0; i<20000; i++)
        for (j=0; j<10000; j++)
            mem[i][j]=2.0;
    printf("%.11f\n", 1.0-f(0,0));
}

double f(int b, int c) {
    if (b+2*c>20000) return 0.0;
    if (b+2*c==20000) return 1.0;
    if (mem[b][c] != 2.0) return mem[b][c];
    double ans = (N-b-c)/N*f(b+1,c);
    if (b>0) ans+=b/N*f(b-1,c+1);
    mem[b][c]=ans;
    return ans;
}
