#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;

const int N = 150000;

void factor(int n, vi &fact) {
    for (int p=2; n>1; p++) {
        if (n%p==0) {
            int x=1;
            do {
                n/=p;
                x*=p;
            } while (n%p==0);
            fact.push_back(x);
        }
    }
}

bool zerosum(vi &fact, vb &used, int p=1, int q=1, int r=1, int i=0, int n=0) {
    if (n==3) {
        int a = p*q, b = p*r, c = q*r;
        if (a-b-c==1 || b-a-c==1 || c-a-b==1) return true;
        return false;
    }
    if (i==fact.size()) return zerosum(fact, used, p, q, r, 0, n+1);
    bool ret;
    if (!used[i]) {
        used[i] = true;
        ret = zerosum(fact, used, n==0?p*fact[i]:p, n==1?q*fact[i]:q, n==2?r*fact[i]:r, i+1, n);
        used[i] = false;
        if (n<2) ret |= zerosum(fact, used, p,q,r, i+1, n);
    }
    else ret = zerosum(fact, used, p,q,r, i+1, n);
    return ret;
}

int main() {
    int cnt=0;
    for (int i=1; cnt<N; i++) {
        vi fact;
        vb used;
        factor(i, fact);
        for (int j=0; j<fact.size(); j++) used.push_back(false);
        if (zerosum(fact,used)) {
            cout << cnt << " " << i << endl;
            cnt++;
        }
    }
    return 0;
}
