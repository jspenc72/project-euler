#include <iostream>
#include <cstring>

using namespace std;

const int N = 27*124+1;
bool done[N];

int main() {
    int t1,t2,t3,tn;
    bool div;
    int count=0;
    memset(done,false,sizeof(done));
    for (int i=27; ; i+=2) {
        if (count==124) {
            cout << i-2 << endl;
            break;
        }
        if (done[i]) {
            count++;
            continue;
        }
        div = false;
        t1=t2=t3=1;
        do {
            tn = (t1+t2+t3)%i;
            t1=t2; t2=t3; t3=tn;
            if (!tn) {
                div=true;
                break;
            }
        } while(t1!=1||t2!=1||t3!=1);
        if (!div) {
            for (int j=i<<1; j<N; j+=i) done[j]=true;
            count++;
        }
    }
    return 0;
}
