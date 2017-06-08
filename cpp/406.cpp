#include <cstdio>
#include <utility>
#include <queue>
#include <cmath>
#include <set>
#include <map>

// basic idea: instead of finding lowest cost for particular n,
// find largest n for particular budget. this works because cost
// is monotonic in n (easy exercise: prove this)

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const double EPS = 1e-6;

double C(ll n, double a, double b) {
    priority_queue<pair<double,pii>, std::vector<pair<double,pii>>, std::greater<pair<double,pii>>> costheap;
    costheap.push(make_pair(a, pii(1,0)));
    costheap.push(make_pair(b, pii(0,1)));
    map<double,ll> mem;
    set<pii> used;
    mem[0.0] = 1;
    used.insert(pii(0,0));
    while (true) {
        auto cur_node = costheap.top();
        double cur = cur_node.first;
        pii move = cur_node.second;
        costheap.pop();
        if (used.find(move) != used.end()) {
            continue;
        }
        used.insert(move);
        ll best_using_cur_cost = 1;
        if (cur >= a) best_using_cur_cost += (--mem.upper_bound(cur-a+EPS))->second;
        if (cur >= b) best_using_cur_cost += (--mem.upper_bound(cur-b+EPS))->second;
        if (best_using_cur_cost >= n) {
            return cur;
        }
        mem[cur] = best_using_cur_cost;
        costheap.push(make_pair(cur+a, pii(move.first+1, move.second)));
        costheap.push(make_pair(cur+b, pii(move.first, move.second+1)));
    }
}

#define PRINT(N) printf("%.8f\n", (N))

int main() {
//    PRINT(C(5, 2, 3));
//    PRINT(C(500, sqrt(2.), sqrt(3.)));
//    PRINT(C(20000, 5, 7));
//    PRINT(C(2000000, sqrt(5.), sqrt(7.)));
    double ans = 0.;
    ll fkprev = 0;
    ll fk = 1;
    for (int k=1; k<=30; k++) {
        ans += C(1000000000000ll, sqrt(k), sqrt(fk));
        ll fksaved = fk;
        fk += fkprev;
        fkprev = fksaved;
    }
    PRINT(ans);
}
