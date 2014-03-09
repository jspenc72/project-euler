#include <iostream>
#include <vector>

using namespace std;

/* This function return the gcd of a and b followed by
	the pair x and y of equation ax + by = gcd(a,b)*/
pair<int, pair<int, int> > extendedEuclid(int a, int b) {
	int x = 1, y = 0;
	int xLast = 0, yLast = 1;
	int q, r, m, n;
	while(a != 0) {
		q = b / a;
		r = b % a;
		m = xLast - q * x;
		n = yLast - q * y;
		xLast = x, yLast = y;
		x = m, y = n;
		b = a, a = r;
	}
	return make_pair(b, make_pair(xLast, yLast));
}

int modInverse(int a, int m) {
    return (extendedEuclid(a,m).second.first + m) % m;
}

const int N=1E8;

int main() {
    vector<bool> prime(N,1);
    prime[0]=prime[1]=0;
    for (int i=0; i*i<N; i++) {
        if (!prime[i]) continue;
        for (int j=i<<1; j<N; j+=i) prime[j]=0;
    }
    long long total=0;
    for (int p=5; p<N; p++) {
        if (!prime[p]) continue;
        int sum=p-1;
        long long prev=p-1;
        for (int k=1; k<5; k++) {
            long long inv=modInverse(p-k,p);
            prev = (prev*inv)%p;
            sum = (sum+prev)%p;
        }
        total += sum;
    }
    cout << total << endl;
    return 0;
}
