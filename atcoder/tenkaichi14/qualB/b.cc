#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const ull MOD = 1000000007;
ull dp[100][1000];

int main() {
  int N;
  string S;
  cin >> N >> S;
  vector<string> T(N);
  for (int i=0; i<N; i++) cin >> T[i];

  for (int i = 0; i < N; i++)
    if (T[i].size() <= S.size())
      if (T[i] == S.substr(0,T[i].size())) dp[i][T[i].size()-1]++;

  for (int j = 0; j < S.size(); j++) {
    for (int i = 0; i < N; i++) {
      for (int k = 0; k < N; k++) {
        if (j - T[k].size() < 0) continue;
        if (dp[k][j-1] > 0) {
          if (T[i].size() + j - 1 > S.size()) continue;
          if (T[i] == S.substr(j,T[i].size()))
            dp[i][j+T[i].size()-1] = (dp[i][j+T[i].size()-1] + dp[k][j-1]) % MOD;
        }
      }
    }
  }
  ll res = 0;
  for (int i = 0; i < 100; i++) res = (res + dp[i][S.size()-1]) % MOD;
  cout << res << endl;
}
