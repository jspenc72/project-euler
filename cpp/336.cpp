#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)

// strategy: 100% brute force, nothing clever at all

using namespace std;

typedef vector<int> vi;

const int N = 11;
const int M = 2011;
int mem[39916800]; //11!
string ans = "ABCDEFGHIJK";

//const int N = 6;
//const int M = 10;
//int mem[720]; //6!
//string ans = "ABCDEF";


int fact(int n) {
    if (n<=1) return 1;
    int ret = 1;
    FOR(i,2,n+1) ret *= i;
    return ret;
}

int count_right_smaller(vi &arr, int i) {
    int ret=0;
    for (int j=i+1; j<N; j++) {
        if (arr[j] < arr[i]) ret++;
    }
    return ret;
}

int h(vi &arr) {
    int ret=0;
    REP(i,N) {
        ret += count_right_smaller(arr, i) * fact(N-1-i);
    }
    return ret;
}

void reverse(vi &arr, int i) {
    for (int j=i; j<N-(j-i)-1; j++) {
        int t = arr[j];
        arr[j] = arr[N-(j-i)-1];
        arr[N-(j-i)-1] = t;
    }
}

int countdfs(vi &arr) {
// LOL, runs faster w/out memoization
// mem code included just for perm memoization reference
//    int &ret = mem[h(arr)];
//    if (ret != -1) return ret;
    int ret;
    REP(i,N) {
      if (arr[i] == i) continue;
      int j = i;
      while (arr[++j] != i);
      if (j==N-1) {
          reverse(arr,i);
          ret = 1 + countdfs(arr);
          reverse(arr,i);
      } else {
          reverse(arr,j);
          reverse(arr,i);
          ret = 2 + countdfs(arr);
          reverse(arr,i);
          reverse(arr,j);
      }
      return ret;
    }
    return 0;
}

void tostring(vi &arr, /*out*/ string &s) {
    REP(i,N) {
        s[i] = 'A' + arr[i];
    }
}

int main() {
//    memset(mem, -1, sizeof(mem));
//    mem[0] = 0;
    vi arr(N,0);
    REP(i,N) arr[i]=i;
    int worst = -1;
    int counter = 0;
    do {
        int maximix = countdfs(arr);
        if (maximix>worst) {
            worst = maximix;
            counter = 1;
        } else if (maximix==worst) {
            if (++counter == M) {
                tostring(arr, ans);
            }
        }
    } while (next_permutation(arr.begin(),arr.end()));
    cout << ans << endl;
    return 0;
}
