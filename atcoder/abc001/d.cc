#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
using namespace std;

int main() {
  int N;
  vector<pair<int, int> > in;
  cin >> N;
  for (int i=0; i<N; i++){
    int s, e;
    char c;
    cin >> s >> c >> e;
    s = s - s%5;
    if (e%5) {
      e += 5 - e%5;
      if (e % 100 == 60) e += 40;
    }
    in.push_back(make_pair(s,0));
    in.push_back(make_pair(e,1));
  }
  sort(in.begin(), in.end());
  int cnt = 0;
  for (int i=0; i<2*N; ++i) {
    if (!cnt)
      cout << setw(4) << setfill('0') << in[i].first << "-";
    if (in[i].second) {
      cnt--;
      if (!cnt)
        cout << setw(4) << setfill('0') << in[i].first << endl;
    } else {
      cnt++;
    }
  }
}
