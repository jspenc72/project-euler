#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

// idea: traverse points backwards (by x coord) and maintain set sorted by y coord.
// essentially finds a longest increasing subsequence. probably would have been more
// elegant / efficient to use LIS algorithm directly.
// runs in about 3m30s on my macbook. i'll take it.

using namespace std;

typedef pair<int,int> pt;
typedef pair<pt, int> pt_id;

vector<pt_id> get_points(int n) {
    int cur_x = 1;
    int cur_y = 1;
    set<pt> pts;
    for (int i=0; i<=2*n; i++) {
        if (!(cur_x==0 && cur_y==0)) {
            // edge case for s(1)
            pts.insert(make_pair(cur_x, cur_y));
        }
        cur_x = (cur_x*2)%n;
        cur_y = (cur_y*3)%n;
    }
    vector<pt_id> ret;
    int cur_id = 0;
    for (auto p : pts) {
        ret.push_back(make_pair(p, cur_id++));
    }
    sort(ret.begin(), ret.end(), greater<pt_id>());
    return ret;
}

int s(int n) {
    vector<pt_id> pts = get_points(n);
    vector<int> longest_from(n);
    set<pt> seen;
    for (auto p : pts) {
        int x = p.first.first;
        int y = p.first.second;
        int i = p.second;
        pt new_pt = make_pair(y, i);
        auto it = seen.lower_bound(new_pt);
        if (it == seen.end()) {
            longest_from[i] = 1;
        } else {
            longest_from[i] = 1 + longest_from[it->second];
            while (it != seen.begin() && longest_from[i] > longest_from[prev(it)->second]) {
                seen.erase(prev(it));
            }
        }
        seen.insert(new_pt);
    }
    return *max_element(longest_from.begin(), longest_from.end());
}

int main() {
    int ans = 0;
    for (int k=1; k<=30; k++) {
        int sk = s(k*k*k*k*k);
        ans += sk;
//        cout << k << " " << sk << endl;
    }
    cout << ans << endl;
    return 0;
}
