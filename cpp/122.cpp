#include <iostream>
#include <queue>

const int N = 200;

struct node {
    int val;
    int depth;
    node *parent;
    node(int v, int d, node *p) {
        val = v;
        depth = d;
        parent = p;
    }
};


int main() {
    using namespace std;
    int count = 0;
    int fewest[N+1];
    for (int i = 0; i <= N; i++) fewest[i] = -1;
    fewest[0] = 0;
    queue<node*> q;
    node *n = new node(1, 0, NULL);
    q.push(n);
    while (count < N) {
        node *t = q.front();
        q.pop();
        int v = t->val;
        int d = t->depth;
        node *p = t->parent;
        node *temp = p;
        int tempv = v;
        if (v <= N && fewest[v] == -1) {
            fewest[v] = d;
            count++;
        }
        q.push(new node(v<<1, d+1, t));
        while (temp != NULL) {
            tempv = temp->val;
            q.push(new node(v + tempv, d+1, t));
            temp = temp->parent;
        }
    }
    int sum = 0;
    for (int i = 1; i <= N; i++) sum += fewest[i];
    cout << sum << endl;
}
