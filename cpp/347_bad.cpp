#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>

struct factors {
    int x;
    int y;
    factors(int m, int n) {
        x=m;
        y=n;
    }
};

using namespace std;

const int N = 10000000;

int main() {
    vector<bool> prime(N+1, true);
    map<int,int> fact1;
    map<int,int> fact2;
    map<int,int> pmap;
    vector<bool> containsf1(N+1, false);
    vector<bool> containsf2(N+1, false);
    vector<bool> finished(N+1, false);

    for (int i = 2; i <= (int)sqrt(N)+1; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j <= N; j += i) {
            prime[j] = false;
            if (finished[j]) continue;
            if (!containsf1[j]) {
                containsf1[j] = true;
                fact1[j] = i;
            }
            else if (!containsf2[j]) {
                containsf2[j] = true;
                fact2[j] = i;
            }
            else {
                finished[j] = true;
                fact1.erase(j);
                fact2.erase(j);
            }
        }
    }

    unsigned long sum = 0;
    int pindex = 0;
    for (int i = 2; i <= N; i++) {
        if (prime[i]) pmap[i] = pindex;
        pindex++;
    }
    int pn = pindex;
    pindex = 0;

    for (int i = 2; i <= N; i++) {
        if (i%1000==0) cout << i << endl;
        if (!prime[i]) continue;
        pindex++;
        int maxes[pn-pindex];
        for (int j = i<<1; j <= N; j += i) {
            if (finished[j] || !containsf1[j] || !containsf2[j]) continue;
            if (j > maxes[pmap[fact2[j]]-pindex]) maxes[pmap[fact2[j]]-pindex] = j;
        }
        for (int j = 0; j < pn-pindex; j++) sum += maxes[j];
    }

//    for (int i = 2; i <= 100; i++) {
//        if (prime[i]) cout << i << " is prime" << endl;
//        if (!finished[i] && containsf1[i] && containsf2[i]) cout << i << " is awesome" << endl;
//    }
    cout << sum << endl;
    return 0;
}
