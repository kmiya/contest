#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
  string s[4];
  for (int i = 0; i < 4; i++) {
    string c;
    getline(cin, c);
    if (*c.rbegin() == '\r')
      c.erase(c.length() - 1);
    reverse(c.begin(), c.end());
    s[i] = c;
  }
  for (int i = 0; i < 4; i++) {
    cout << s[3 - i] << endl;
  }
}
