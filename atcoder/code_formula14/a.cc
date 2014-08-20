#include <iostream>
using namespace std;

typedef long long ll;

int main() {
  ll A;
  cin >> A;
  for (ll i = 1; i <= 100; i++) {
    if (i * i * i == A) {
      cout << "YES" << endl;
      return 0;
    }
  }
  cout << "NO" << endl;
}
