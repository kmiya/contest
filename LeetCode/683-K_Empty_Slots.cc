// time: O(N)
// space: O(N)
// Runtime: 676 ms, faster than 8.65% of C++ online submissions for K Empty Slots.
// Memory Usage: 73.8 MB, less than 5.77% of C++ online submissions for K Empty Slots.

class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        map<int,int> m;
        for (int i = 0; i < flowers.size(); i++) {
            m.insert(make_pair(flowers[i], i + 1));
        }
        int result = flowers.size() + 1;
        for (int i = 1; i < flowers.size(); i++) {
            const int npos = i + k + 1;
            if (npos > flowers.size()) break;
            const int max_d = max(m[i], m[npos]);
            // printf("%d: %d %d, %d %d\n", max_d, i, npos, m[i], m[npos]);
            bool flag = false;
            for (int j = i + 1; j < npos; ++j) {
                if (m[j] <= max_d){ flag = true; break;}
            }
            if (!flag) {
                result = min(max_d, result);
            }
        }
        if (result > flowers.size()) return -1;
        else return result;
    }
};