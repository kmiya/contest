#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

int main() {
  string z = "123456";
  ll N;
  cin >> N;
  const int a = N % 30;
  const int b = a / 5;
  for (int i = 1; i <= 6; i++) z[(5 - b + i) % 6] = i + 0x30;
  for (int i = 0; i < a % 5; i++) swap(z[i], z[i+1]);
  cout << z << endl;
}
