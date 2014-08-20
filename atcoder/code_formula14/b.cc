#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  char pin[10];
  int a, b;
  cin >> a >> b;
  vector<int> p(a), q(b);
  for (int i = 0; i < a; i++) cin >> p[i];
  for (int i = 0; i < b; i++) cin >> q[i];

  for (int i = 0; i < 10; i++) pin[i] = 'x';
  for (int i = 0; i < a; i++) pin[p[i]] = '.';
  for (int i = 0; i < b; i++) pin[q[i]] = 'o';
  printf("%c %c %c %c\n", pin[7], pin[8], pin[9], pin[0]);
  printf(" %c %c %c\n"  , pin[4], pin[5], pin[6]);
  printf("  %c %c\n"    , pin[2], pin[3]);
  printf("   %c\n"      , pin[1]);
}
