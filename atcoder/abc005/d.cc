#include <algorithm>
#include <iostream>
using namespace std;

int D[51][51];
int sq[51][51];
int Qs[2501];

int main() {
  int N, Q;
  cin >> N;
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++) cin >> D[i][j];
  cin >> Q;
  vector<int> q(Q);
  for (int i = 0; i < Q; i++) cin >> q[i];

  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      sq[i][j] = D[i][j] + sq[i-1][j] + sq[i][j-1] - sq[i-1][j-1];

  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= N; j++)
      for (int k = i; k <= N; k++)
        for (int l = j; l <= N; l++) {
          int val = sq[k][l] - sq[k][j-1] - sq[i-1][l] + sq[i-1][j-1];
          Qs[(k-i+1)*(l-j+1)] = max(Qs[(k-i+1)*(l-j+1)], val);
        }

  int maxd = 0;
  for (int i = 1; i <= N*N; i++) {
    maxd  = max(maxd, Qs[i]);
    Qs[i] = maxd;
  }
  for (int i : q) cout << Qs[i] << endl;
}
