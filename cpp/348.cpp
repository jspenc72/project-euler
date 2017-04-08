#include <iostream>
#include <utility>
#include <unordered_map>
#include <queue>
#include <set>

// just do the obvious thing. probably not smart, but was fast to code.
// runs in ~1m after optimizing.

using namespace std;

typedef pair<int,int> pii;
typedef pair<int,pii> node;
typedef long long ll;

int log10pow(int n) {
    int ret=1;
    n/=10;
    while (n>0) {
        n/=10;
        ret*=10;
    }
    return ret;
}

bool is_palindrome(int n) {
    int div = log10pow(n);
    int mod = 10;
    while (div >= mod) {
        if (n/div != n%mod) {
            return false;
        }
        n%=div;
        n/=10;
        div /= 100;
    }
    return true;
}

int main() {
    int found = 0;
    set<pii> seen;
    unordered_map<int,int> ways;
    priority_queue<node, vector<node>, greater<node> > q;
    q.push(make_pair(12, make_pair(2,2)));
    seen.insert(make_pair(2,2));
    vector<int> pals;
    while (found < 5) {
        node next = q.top();
        q.pop();
        int p = next.first;
        int s = next.second.first;
        int c = next.second.second;
        if (is_palindrome(p)) {
            int& nways = ways[p];
            ++nways;
            if (nways == 4 && q.top().first > p) {
                found++;
                pals.push_back(p);
            }
        }
        if (seen.find(make_pair(s+1,c)) == seen.end()) {
            seen.insert(make_pair(s+1,c));
            q.push(make_pair((s+1)*(s+1)+c*c*c, make_pair(s+1,c)));
        }
        if (seen.find(make_pair(s,c+1)) == seen.end()) {
            seen.insert(make_pair(s,c+1));
            q.push(make_pair(s*s+(c+1)*(c+1)*(c+1), make_pair(s,c+1)));
        }
    }
    ll total = 0;
    for (int p : pals) {
        total += p;
//        cout << p << " ";
    }
//    cout << endl;
    cout << total << endl;
    return 0;
}
