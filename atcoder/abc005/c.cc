#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T, N, M;
  cin >> T >> N;
  vector<int> a(N);
  for (int i = 0; i < N; i++) cin >> a[i];
  cin >> M;
  vector<int> b(M);
  for (int i = 0; i < M; i++) cin >> b[i];

  bool dp[N+1][M+1];
  for (int i = 0; i <= N; i++) {
    for (int j = 0; j <= M; j++) {
      if (i < j) dp[i][j] = false;
      else if (!j) dp[i][j] = true;
      else {
        bool f = (a[i-1] + T >= b[j-1] && a[i-1] <= b[j-1]) ? true : false;
        dp[i][j] = dp[i-1][j] | (dp[i-1][j-1] & f);
      }
      if (i == N && !dp[i][j]) {
        cout << "no" << endl;
        return 0;
      }
    }
  }
  cout << "yes" << endl;
}
