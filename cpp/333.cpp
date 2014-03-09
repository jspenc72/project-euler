#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

const int N = int(1E6);

char F[N][20][13][2];

char f(int n, int xp, int yp, int x, int y, bool p) {
    if (n==0) return 1;
    if (n<x or y==0) return 0;
    if (n<x*y) {
        if (p) return 0;
        else return f(n,xp,yp-1,x,y/3,false);
    }
    char &ret = F[n][xp][yp][p];
    if (ret!=-1) return ret;
    ret = f(n-x*y,xp+1,yp-1,2*x,y/3,false) + f(n,xp+1,yp,2*x,y,true);
    if (!p) ret += f(n,xp,yp-1,x,y/3,false);
    if (ret>1 || ret<0) ret=-10;
    return ret;
}

int main() {
    memset(F,-1,sizeof(F));
    bool prime[N];
    memset(prime,true,sizeof(prime));
    prime[0]=prime[1]=false;
    for (int i=2; i*i<N; i++) {
        if (!prime[i]) continue;
        for (int j=i*i; j<N; j+=i)
            prime[j]=false;
    }
    int ans=0;
    for (int i=0; i<N; i++) {
        if (!prime[i]) continue;
        int y=3, yp=1;
        while (y<=i) {
            y*=3; yp++;
        }
        yp--; y/=3;
        if (f(i,0,yp,1,y,false)==1) ans+=i;
    }
    cout << ans << endl;
    return 0;
}
