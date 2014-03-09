#include <iostream>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MAX3(a,b,c) MAX(MAX(a,b),c)
#define MIN(a,b) ((a)<(b)?(a):(b))

//simple brute force w/ semi-intelligent backtracking

using namespace std;

int main() {
    int s, total=0;
    REP(a11,10) REP(a12,10) REP(a13,10) REP(a14,10) {
        s = a11+a12+a13+a14;
        REP(a21,MIN(9,s-a11)+1) REP(a22,MIN(9,s-MAX3(a11,a12,a21))+1) REP(a23,MIN(9,s-MAX3(a13,a14,a21+a22))+1) {
            int a24 = s-a21-a22-a23;
            if (a24>9) continue;
            REP(a31,MIN(9,s-a11-a21)+1) REP(a32,MIN(9,s-MAX3(a12+a22,a14+a23,a31))+1) REP(a33,MIN(9,s-MAX3(a11+a22,a13+a23,a31+a32))+1) {
                int a34 = s-a31-a32-a33;
                if (a34>9) continue;
                int a41, a42, a43, a44;
                if ((a41=s-a11-a21-a31)!=s-a14-a23-a32 || a41>9) continue;
                if ((a44=s-a14-a24-a34)!=s-a11-a22-a33 || a44>9) continue;
                a42 = s-a12-a22-a32;
                if (a42>9) continue;
                a43 = s-a13-a23-a33;
                if (a43>9) continue;
                total += (a41+a42+a43+a44==s);
            }
        }
    }
    cout << total << endl;
    return 0;
}
