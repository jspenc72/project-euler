#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MAX3(a,b,c) MAX(MAX(a,b),c)
#define MAX4(a,b,c,d) MAX(MAX3(a,b,c),d)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MIN3(a,b,c) MIN(MIN(a,b),c)
#define MIN4(a,b,c,d) MIN(MIN3(a,b,c),d)
#define SZ size()
#define PB push_back

using namespace std;
typedef vector<int> VE;

const int N = pow(10,6);

int main() {
    vector<bool> prime(N,true);
    prime[0]=prime[1]=false;
    for (int i = 2; i*i < N; i++) {
        if (!prime[i]) continue;
        for (int j = i<<1; j < N; j += i) prime[j]=false;
    }
    int total=0;
    int test = 0;
    for (int a = 1; 3*(a*a+a)+1 < N; a++) {
        int b = a+1;
        if (prime[b*b*b-a*a*a]) total++;
    }
    cout << total << endl;
    return 0;
}
