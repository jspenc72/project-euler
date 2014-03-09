#include <iostream>

using namespace std;

typedef long long ll;
const int N=int(1E6);

int parent[N], rank[N], card[N];
int S[55];

void make_set(int x) {
    parent[x]=x;
    rank[x]=0;
    card[x]=1;
}

int find(int x) {
    if (parent[x]==x) return x;
    return parent[x]=find(parent[x]);
}

void unite(int x, int y) {
    int xr=find(x), yr=find(y);
    if (xr!=yr) {
        card[xr]=card[yr]=card[xr]+card[yr];
        if (rank[xr]>rank[yr]) parent[yr]=xr;
        else if (rank[yr]>rank[xr]) parent[xr]=yr;
        else {
            parent[yr]=xr;
            rank[xr]++;
        }
    }
}

inline int s(int k) {
    int x=k+1;
    return (100003 - 200003*x + ll(300007)*x*x*x)%N;
}

int main() {
    int k=0, mis=0;
    for (int i=0; i<N; i++) make_set(i);
    while(card[find(524287)] < N/100*99) {
        int u, v;
        if (k<55) u = S[k] = s(k);
        else u = S[k%55] = (S[(k-24+55)%55] + S[k%55])%N;
        k++;
        if (k<55) v = S[k] = s(k);
        else v = S[k%55] = (S[(k-24+55)%55] + S[k%55])%N;
        k++;
        if (u==v) mis++;
        else unite(u,v);
    }
    cout << k/2-mis << endl;
    return 0;
}
