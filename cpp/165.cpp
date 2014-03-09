#include <iostream>

#define REP(i,a) for(int i=0;i<(a);i++)

using namespace std;
typedef long long ll;

//Note: this program is broken since there are some duplicate intersections.
//see 165.py
//One speedup would be to use this code to calculate intersecting segments,
//then use python to calculate intersections and remove duplicates.
//Or I could not be lazy and just do it in C.

const int mod=50515093;
const int N=5000;
int p[N][4];

inline int sgn(int x) {
    return (x>0)-(x<0);
}

inline bool intersects(int i, int j) {
    int xi1=p[i][0],yi1=p[i][1],xi2=p[i][2],yi2=p[i][3];
    int xj1=p[j][0],yj1=p[j][1],xj2=p[j][2],yj2=p[j][3];
    //straddle each other
    if (sgn(sgn((xj1-xi1)*(yi2-yi1)-(xi2-xi1)*(yj1-yi1)) * sgn((xj2-xi1)*(yi2-yi1)-(xi2-xi1)*(yj2-yi1))) >= 0) return false;
    //straddle each other
    if (sgn(sgn((xi1-xj1)*(yj2-yj1)-(xj2-xj1)*(yi1-yj1)) * sgn((xi2-xj1)*(yj2-yj1)-(xj2-xj1)*(yi2-yj1))) >= 0) return false;
    return true;
}

int main() {
    int total=0;
    ll s=290797;
    REP(i,N) {
        REP(j,4) {
            s=s*s%mod;
            p[i][j]=s%500;
        }
    }
    REP(i,N) REP(j,i) if (intersects(i,j)) {
        total++;
    }
    cout << total << endl;
    return 0;
}
