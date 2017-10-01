#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int N = 100000000;
const int mod = 1000000007;

// just go through all pi-sequences and count how many primes they have

int main() {
    vector<bool> prime(N+1, true);
    prime[0] = prime[1] = false;
    for (int i=2; i*i<=N; i++) {
        if (!prime[i]) continue;
        for (int j=i*i; j<=N; j+=i) prime[j] = false;
    }
    vector<int> pi(N+1);
    map<int,int> k_seqs;
    for (int i=2; i<=N; i++) {
        pi[i] = pi[i-1] + prime[i];
        int cur = i;
        int cur_c = (1 - prime[i]);
        while (cur > 1) {
            cur = pi[cur];
            cur_c += (1-prime[cur]);
            k_seqs[cur_c] += 1;
        }
    }

    long long ans = 1;
    for (auto kv : k_seqs) {
        ans = (ans*kv.second)%mod;
    }

    cout << ans << endl;
}
