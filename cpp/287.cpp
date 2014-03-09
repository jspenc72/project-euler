#include <iostream>

using namespace std;
typedef long long ll;

const int N=24;

bool b(ll x, ll y) {
    return (x-(1ll<<(N-1)))*(x-(1ll<<(N-1)))+(y-(1ll<<(N-1)))*(y-(1ll<<(N-1)))<=(1ll<<(2*N-2));
}

ll f(ll x1, ll y1, ll x2, ll y2, bool lleft, bool uright) {
    int t = b(x1,y1)*8 + b(x2-1,y1)*4 + b(x2-1,y2-1)*2 + b(x1,y2-1);
    if (t==15||t==0) return 2;
    ll xm = (x1+x2)/2, ym=(y1+y2)/2;
    if (lleft) return 1+f(x1,y1,xm,ym,1,0)+2*f(xm,y1,x2,ym,0,0)+f(xm,ym,x2,y2,0,0);
    if (uright) return 1+f(x1,y1,xm,ym,0,0)+2*f(xm,y1,x2,ym,0,0)+f(xm,ym,x2,y2,0,1);
    return 1+f(x1,y1,xm,ym,0,0)+f(xm,y1,x2,ym,0,0)+f(xm,ym,x2,y2,0,0)+f(x1,ym,xm,y2,0,0);
}

int main() {
    ll n = 1ll<<N;
    ll m = n>>1ll;
    cout << 1+f(0,0,m,m,1,0)+2*f(m,0,n,m,0,0)+f(m,m,n,n,0,1) << endl;
    return 0;
}
