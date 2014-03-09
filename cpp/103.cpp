#include <iostream>
#include "mutils.h"

const int N = 9;

bool works(int *test, int n);
void branch(int *test, int n);
int sum(int *a, int n);
void arrcpy(int *a1, int *a2, int n);

int arr[] = {78, 117, 137, 148, 155, 156, 157, 159, 162};

int main(void) {
    using namespace std;
    int test[N];
    for (int i = 0; i < N; i++) test[i] = 0;
    branch(test, 0);
    for (int i = 0; i < N; i++) cout << arr[i];
    cout << endl;
}

bool works(int *test, int n) {
    int total = 1<<n;
    for (int i = 0; i < total; i++) {
        int log = lg(i);
        int jtot = 1<<(n-log-1);
        for (int j = 0; j < jtot; j++) {
            int dj = j<<(log+1);
            int sum1=0,sum2=0,n1=0,n2=0;
            for (int k = 0; k < n; k++) {
                if ((1<<k)&i) {
                    sum1 += test[k];
                    n1++;
                }
                if ((1<<k)&j) {
                    sum2 += test[k];
                    n2++;
                }
            }
            if (sum1==sum2 || (n1>n2 && sum1 < sum2) || (n2>n1 && sum2<sum1)) return false;
        }
    }
    return true;
}

void branch(int *test, int n) {
    if (n==N) {
        if (sum(test,N) < sum(arr,N)) arrcpy(arr,test,N);
    }
    else {
        int last;
        if (n==0) last=0;
        else last = test[n-1];
        int count = last;
        while (true) {
            count += 1;
            int diff = N-n;
            if (sum(test,n) + diff*count + diff*(diff-1)/2 > sum(arr,N)) break;
            test[n] = count;
            if (works(test, n+1)) branch(test, n+1);
        }
    }
}

int sum(int *a, int n) {
    int total = 0;
    for (int i = 0; i < n; i++) total += a[i];
    return total;
}

void arrcpy(int *a1, int *a2, int n) {
    for (int i = 0; i < n; i++) a1[i] = a2[i];
}
