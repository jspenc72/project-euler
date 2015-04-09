#include <iostream>
#include <cmath>

using namespace std;

const int N = 100;
int gcds[N+1][N+1];

int gcd(int x, int y) {
    int t;
    while (y!=0) {
        t = x;
        x = y;
        y = t%y;
    }
    return x;
}

bool square(int x) {
    int r = (int)round(sqrt(x));
    return r*r == x;
}

inline int valid(int a, int b, int c, int d) {
    int ab = gcds[a][b]-1;
    int bc = gcds[b][c]-1;
    int cd = gcds[c][d]-1;
    int da = gcds[d][a]-1;
    int twoA = a*b + b*c + c*d + d*a;
    int i = (twoA - ab - bc - cd - da - 2)/2;
    return square(i) ? 1 : 0;
}

// strategy: brute force, then use pick's thm + symmetry
int main() {
    for (int i=1; i<=N; i++) {
        for (int j=i; j<=N; j++) {
            gcds[i][j] = gcds[j][i] = gcd(i,j);
        }
    }

    int total=0;

    for (int a=1; a<=N; a++) {
        for (int b=a; b<=N; b++) {
            for (int c=1; c<=N; c++) {
                for (int d=c; d<=N; d++) {
                    //abcd
                    total += valid(a,b,c,d);
                    //bacd
                    if (b!=a) total += valid(b,a,c,d);
                    //abdc
                    if (c!=d) total += valid(a,b,d,c);
                    //badc
                    if (a!=b && c!=d) total += valid(b,a,d,c);
                }
            }
        }
    }
    cout << total << endl;
    return 0;
}
