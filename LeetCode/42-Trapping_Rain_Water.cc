// brute force solution; TLE if written in python
// time: O(N * h) where h is the max height
// space: O(1)
// Runtime: 1420 ms, faster than 5.06% of C++ online submissions for Trapping Rain Water.
// Memory Usage: 10.9 MB, less than 52.49% of C++ online submissions for Trapping Rain Water.
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {return 0;}
        int ans = 0;
        const auto max_i = *max_element(height.begin(),height.end());
        int min_x = 0;
        int max_x = height.size();
        for (int h = 0; h < max_i; h++) {
            bool flag = false;
            int water = 0;
            const int max_size = max_x;
            for (int x = min_x; x < max_size; x++) {
                if (!flag){
                    if (height[x] - h > 0) {
                        flag = true;
                        min_x = x;
                    }
                } else {
                    if (height[x] - h > 0){
                        ans += water;
                        water = 0;
                        max_x = x + 1;
                    } else water += 1;
                }
            }
        }
        return ans;
    }
};