#include <iostream>

using namespace std;

typedef long long ll;

ll gcd(ll x, ll y) {
    ll t;
    while (y!=0) {
        t = x;
        x = y;
        y = t%y;
    }
    return x;
}

int main() {
    //We find the number of solutions to
    //the Diophantine equation
    //2x + 4y - 3 = n
    ll ways=0;
    ll a = 1201763915ll;
    ll b = 2;
    ll c = 2403527830ll;
    ll d = -1;
    ll x,y;
    for (ll t = 1; ; t++) {
        x = a-b*t;
        y = c-d*t;
        if (x<0 or y<0) break;
        if (gcd(x,y)!=1) continue;
        ways++;
    }
    for (ll t = 0; ; t++) {
        x = a+b*t;
        y = c+d*t;
        if (x<0 or y<0) break;
        if (x>=y) break;
        if (gcd(x,y)!=1) continue;
        ways++;
    }
    cout << 2*ways << endl;
    return 0;
}
