#include <bitset>
#include <iostream>
using namespace std;

bool m[12][12];

int main() {
  int N, M;
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int x, y;
    cin >> x >> y;
    m[x-1][y-1] = m[y-1][x-1] = true;
  }
  int res = 0;
  for (int s = 1; s < 1 << N; s++) {
    const int num = bitset<14>(s).count();
    if (res >= num) continue;
    bool chk = true;
    for (int j = 0; j < 12; j++) {
      for (int k = j + 1; k < 12; k++) {
        if (s >> j & s >> k & 1 && !m[j][k]) {
          chk = false;
        }
      }
    }
    if (chk) res = num;
  }
  cout << res << endl;
}
