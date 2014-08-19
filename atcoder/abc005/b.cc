#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int N;
  cin >> N;
  int res = 101;
  for (int i = 0; i < N; i++) {
    int t;
    cin >> t;
    res = min(res,t);
  }
  cout << res << endl;
}
