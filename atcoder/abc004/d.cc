#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;

ll dp[1001][901];
const ll INT_MAX = 1000000007;

int main() {
  int r, g, b;
  cin >> r >> g >> b;
  const int MAX = r + g + b;
  for (int i = 0; i < 1001; i++) {
    for (int j = 0; j <= MAX; j++) {
      int cost = 0;
      if (j <= r)          cost = abs(400 - i);
      else if (j <= r + g) cost = abs(500 - i);
      else if (j <= MAX)   cost = abs(600 - i);

      if (!j) dp[i][j] = 0;
      else if (i + 1 < j)    dp[i][j] = INT_MAX;
      else if (!i && j == 1) dp[i][j] = cost;
      else {
        const int y = dp[i-1][j-1] + cost;
        const int n = dp[i-1][j];
        dp[i][j] = min(y, n);
      }
    }
  }
  ll res = INT_MAX;
  for (int i = 0; i < 1001; i++)
    res = min(res, dp[i][MAX]);

  cout << res << endl;
}
