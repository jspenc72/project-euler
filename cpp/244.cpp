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
typedef pair<string,int> psi;
typedef long long ll;

const int oo = INT_MAX>>1;
const int mod = 100000007;

int mem[1<<19];

void swap(int &x, int &y) {
    int t=x; x=y; y=t;
}

int chck(string &s) {
    ll ret=0;
    REP(i,s.length()) {
        ret = (ret*243+s[i])%mod;
    }
    return ret;
}

int hsh(int board[4][4]) {
    int white;
    int rest=0;
    for (int i=3; i>=0; i--) {
        for (int j=3; j>=0; j--) {
            if (board[i][j]==2) {
                white = 4*i+j;
                continue;
            }
            rest = rest*2 + board[i][j];
        }
    }
    return (rest<<4) + white;
}

void genstates(int stat, string &moves, queue<psi> &q) {
    int board[4][4];
    int white = stat%16;
    int dist = moves.length();
    int wx, wy;
    stat >>= 4;
    REP(i,4) REP(j,4) {
        if (4*i+j==white) {
            wy=i; wx=j;
            board[i][j]=2;
            continue;
        }
        board[i][j]=stat&1;
        stat >>= 1;
    }
    REP(i,2) {
        int y = wy + 2*i-1;
        int x = wx + 2*i-1;
        if (0<=y && y<4) {
            swap(board[y][wx], board[wy][wx]);
            stat = hsh(board);
            if (mem[stat]==-1 || mem[stat]==dist+1) {
                mem[stat] = dist+1;
                q.push(psi(moves+(i?"U":"D"),stat));
            }
            swap(board[y][wx], board[wy][wx]);
        }
        if (0<=x && x<4) {
            swap(board[wy][x], board[wy][wx]);
            stat = hsh(board);
            if (mem[stat]==-1 || mem[stat]==dist+1) {
                mem[stat] = dist+1;
                q.push(psi(moves+(i?"L":"R"),stat));
            }
            swap(board[wy][x], board[wy][wx]);
        }
    }
}

int main() {
    memset(mem,-1,sizeof(mem));
    int start[4][4];
    int end[4][4];
    REP(i,4) REP(j,4) {
        if (i+j==0) {
            start[i][j]=2;
            end[i][j]=2;
            continue;
        }
        start[i][j] = (j<2);
        end[i][j] = !((i+j)&1);
//        end[i][j] = (i<2); // red in upper half
    }
    int hs = hsh(start);
    int he = hsh(end);
    queue<psi> q;
    q.push(psi("",hs));
    int last = oo;
    mem[hs]=0;
    ll ans=0;
    int pths=0;
    while (q.SZ > 0) {
        psi stat = q.front();
        q.pop();
        if (stat.first.length() > last) break;
        if (stat.second==he) {
            last=stat.first.length();
            ans += chck(stat.first);
            pths++;
        }
        genstates(stat.second, stat.first, q);
    }
    cout << pths << endl;
    cout << ans << endl;
    return 0;
}
