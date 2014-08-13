#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {
  int N, K;
  cin >> N >> K;
  vector<int> R;
  for (int i=0; i<N; i++) {
    int r;
    cin >> r;
    R.push_back(r);
  }
  sort(R.begin(),R.end(),greater<int>());
  double res = 0;
  for (int i=0; i<K; i++) {
    res = (res + R[K-i-1])/2.;
  }
  cout.setf(ios::fixed);
  cout.precision(6);
  cout << res << endl;
}
