#include <iostream>
#include <string>
using namespace std;

string a = "atcoder";

int main() {
  string s,t;
  bool win = true;
  cin >> s >> t;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] != t[i]) {
      if (s[i] == '@') {
        if (a.find(t[i],0)==string::npos) {
          win = false;
          break;
        }
      } else if (t[i] == '@'){
        if (a.find(s[i],0)==string::npos) {
          win = false;
          break;
        }
      } else {
        win = false;
        break;
      }
    }
  }
  if (win) cout << "You can win" << endl;
  else cout << "You will lose" << endl;
}
