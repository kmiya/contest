#include <bitset>
#include <iostream>
using namespace std;

typedef long long ll;

const ll MOD = 1000000007;
ll pas[900][900];

ll bi(const int x, const int y) {
  if (x < y) return 0;
  if (pas[x-y][y]) return pas[x-y][y];
  for (int i=0; i<=x-y; i++) {
    for (int j=0; j<=y; j++) {
      if (!i || !j) pas[i][j] = 1;
      else pas[i][j] = (pas[i][j-1] + pas[i-1][j]) % MOD;
    }
  }
  return pas[x-y][y];
}

int main() {
  int R, C, X, Y, D, L;
  cin >> R >> C >> X >> Y >> D >> L;
  ll dl = bi(X*Y,D) * bi(X*Y-D,L);
  for (int f=1; f<1<<4; f++) {
    int x = X, y = Y;
    bitset<5> fb(f);
    if (fb[0]) x--;
    if (fb[1]) x--;
    if (fb[2]) y--;
    if (fb[3]) y--;
    if (x <= 0 || y <= 0) continue;
    if (fb.count() % 2)
      dl -= bi(x*y,D) * bi(x*y-D,L);
    else
      dl += bi(x*y,D) * bi(x*y-D,L);
  }
  dl = (dl % MOD + MOD) % MOD;
  int space = (C-Y+1) * (R-X+1);
  ll res = (dl * space) % MOD;
  cout << res << endl;
}
