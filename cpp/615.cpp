#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

typedef long long ll;

typedef pair<int, int> factor_t;
typedef vector<factor_t> f11n_t;
typedef pair<int, f11n_t> f11n_meta_t;
typedef pair<double, f11n_meta_t> cf_t;

#define BASE first
#define EXP second
#define START_IDX first
#define FACTORS second
#define LOGVAL first
#define META second

ll modval(const f11n_t &factors) {
    ll ret = 1;
    ll mod = 123454321;
    for (auto& f : factors) {
        for (int i=0; i<f.EXP; i++) {
            ret = (ret * f.BASE) % mod;
        }
    }
    return ret;
}

const int N = 1000000;

int main() {
    const int M = 10*N;
    vector<bool> prime(M+1, true);
    prime[0]=prime[1]=false;
    for (int i=0; i*i<=M; i++) {
        if (!prime[i]) continue;
        for (int j=i*i; j<=N; j+=i) prime[j] = false;
    }
    vector<int> primes;
    for (int i=0; i<=M; i++) if(prime[i]) primes.push_back(i);
    priority_queue<cf_t> q;
    f11n_meta_t twos;
    twos.FACTORS = f11n_t({factor_t(2, N)});
    twos.START_IDX = 0;
    q.push(cf_t(N*log(2.), twos));
    cf_t cur = q.top(); q.pop();
    int counter = 1;
    while (counter < N) {
        if (cur.META.FACTORS.size() == 1) {
            auto& curf = cur.META.FACTORS[0];
//            cout << "pushing something: " << curf.BASE << " " << curf.EXP+1 << " " << (cur.LOGVAL - log(curf.BASE)) << endl;
            curf.EXP++;
            cf_t to_push(cur.LOGVAL - log(curf.BASE), f11n_meta_t(cur.META.START_IDX, f11n_t(cur.META.FACTORS)));
            q.push(to_push);
            curf.EXP--;
        }
//        if (counter%10000==0) cout << counter << " " << modval(cur.META.FACTORS) << " " << cur.LOGVAL << endl;
        if (cur.META.START_IDX+1 >= cur.META.FACTORS.size()) {
            cur.META.FACTORS.push_back(factor_t(primes.at(cur.META.START_IDX+1), 0));
        }
        if (cur.META.START_IDX+2 >= cur.META.FACTORS.size()) {
            cur.META.FACTORS.push_back(factor_t(primes.at(cur.META.START_IDX+2), 0));
        }
        auto& curf = cur.META.FACTORS[cur.META.START_IDX];
        auto& nextf = cur.META.FACTORS[cur.META.START_IDX+1];
        auto& nextnextf = cur.META.FACTORS[cur.META.START_IDX+2];
        if (curf.EXP > 0) {
            curf.EXP--;
            nextf.EXP++;
            cf_t to_push(cur.LOGVAL + log(curf.BASE) - log(nextf.BASE), f11n_meta_t(cur.META.START_IDX, f11n_t(cur.META.FACTORS)));
            q.push(to_push);
            curf.EXP++;
            nextf.EXP--;
        }
        if (nextf.EXP > 0) {
            nextf.EXP--;
            nextnextf.EXP++;
            cf_t to_push(cur.LOGVAL + log(nextf.BASE) - log(nextnextf.BASE), f11n_meta_t(cur.META.START_IDX+1, f11n_t(cur.META.FACTORS)));
            q.push(to_push);
            nextf.EXP++;
            nextnextf.EXP--;
        }
        cur = q.top(); q.pop();
        counter++;
    }
    cout << modval(cur.META.FACTORS) << endl;
}
