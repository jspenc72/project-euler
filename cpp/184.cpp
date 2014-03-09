#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> vi;

const int R = 105;

vi px, py;

// test to see if (xp, yp) is on segment between (x1,y1) and (x2,y2)
bool on_segment(int x1, int y1, int x2, int y2, int xp, int yp) {
    return (min(x1,x2) <= xp && xp <= max(x1,x2) &&
            min(y1,y2) <= xp && xp <= max(y1,y2));
}

int main() {
    for (int x=-R+1; x<R; x++) {
        for (int y=-R+1; y<R; y++) {
            if (x==0 && y==0) continue; // no point in treating this case
            if (x*x+y*y < R*R) {
                px.push_back(x);
                py.push_back(y);
            }
        }
    }
    long long total=0;
    for (int i=0; i<px.size(); i++) {
        int left = 0, right = 0, onseg = 0, offseg = 0;
        int x1 = px[i], y1 = py[i];
        for (int j=0; j<px.size(); j++) {
            if (j==i) continue; // no point in treating this case
            int x2 = px[j], y2 = py[j];
            int crossp = x1*y2 - x2*y1;
            if (crossp < 0) left++;
            else if (crossp > 0) right++;
            else {
                if (on_segment(x1,y1,x2,y2,0,0)) onseg++;
                else offseg++;
            }
        }
        total += left*right*4; // two arms are "catching" center -- adds 4
        total -= left*(left-1); // two arms are missing center -- subtracts 2
        total -= right*(right-1); // same
        total -= onseg*(left+right)*2; // center is on one arm -- subtracts 2 per left, 2 per right
        total += offseg*(left+right); // center is behind one arm -- adds 1 per left, 1 per right
    }
    cout << total/12 << endl;
             
    return 0;
}
