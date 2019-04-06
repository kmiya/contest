#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(int, char**) {
    int T = 0;
    cin >> T;
    for (auto t = 0; t < T; t++) {
        string N;
        cin >> N;
        string ans1 = "";
        string ans2 = "";
        for (auto i = 0; i < N.length(); i++) {
            const int n = N[i] - '0';
            if (n == 4) {
                ans1 += '1';
                ans2 += '3';
            } else {
                ans1 += N[i];
                if (ans2 != "") ans2 += '0';
            }
        }
        cout << "Case #" << t + 1 << ": " << ans1 << " " << ans2 << endl;
    }
}
