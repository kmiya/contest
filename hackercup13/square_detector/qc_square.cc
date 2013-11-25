// Square Detector
// 正方形の幅が w だとすると，各行と各列毎の # の数も w になる．
// そこで，各行と各列毎の # の数 n を計算し，すべての n が等しいか確認．
// ただし，以下のような正方形でないパターンに注意．
//   220
// 2 ##.
// 0 ...
// 2 ##.


#include <iostream>
#include <vector>
#include <string>

using namespace std;
int judge(const int& N, const vector<int>& sum);

int main() {
  int T = 0;
  cin >> T;
  cin.ignore();

  for (auto t = 0; t < T; ++t) {
    cout << "Case #" << t + 1 << ": ";
    int N = 0;
    cin >> N;
    cin.ignore();
    vector<int> sum_x(N, 0), sum_y(N, 0);
    for (auto y = 0; y < N; ++y) {
      for (auto x = 0; x < N; ++x) {
        char s;
        cin >> s;
        if (s == '#') { // # は 1 で . は 0
          ++sum_x[x];
          ++sum_y[y];
        }
      }
    }
    if (judge(N, sum_x) && judge(N, sum_y)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}

int judge(const int& N, const vector<int>& sum) {
  int len = sum[0]; // 正方形の一辺の長さ
  int cnt = len;
  for (auto i = 0; i < N; ++i) {
    if (!len) {
      if (sum[i]) {
        len = sum[i];
        cnt  = len - 1;
      }
    } else {
      if (sum[i] == len) --cnt;
      if ( (cnt < 0 && cerr << "e1,")                          // 一辺が大きい
        || (cnt != 0 && sum[i] == 0 && cerr << "e2,")          // 一辺が大きい
        || (sum[i] != len && sum[i] != 0 && cerr << "e3,") ) { // 中空な箱か不要な # がある
        return 0;
      }
    }
  }
  if ( (!len && cerr << "e4,")        // 全要素が 0 なので No
    || (cnt > 0 && cerr << "e5,") ){  // 要素が多すぎるので No
    return 0;
  }
  return 1;
}
