// 4. Median of Two Sorted Arrays
// Time O(m+n), Space O(m+n) solution
// Success
// Runtime: 44 ms, faster than 97.04% of C++ online submissions for Median of Two Sorted Arrays.
// Memory Usage: 21.8 MB, less than 26.40% of C++ online submissions for Median of Two Sorted Arrays.

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> a;
        const size_t total_size = nums1.size() + nums2.size();
        a.reserve(total_size);
        size_t p1 = 0;
        size_t p2 = 0;
        for (int i = 0; i < total_size; ++i) {
            if (p1 >= nums1.size() && p2 < nums2.size()) {
                for (int j = i; j < total_size; ++j) {
                    a[j] = nums2[p2++];
                }
                break;
            }
            if (p1 < nums1.size() && p2 >= nums2.size()) {
                for (int j = i; j < total_size; ++j) {
                    a[j] = nums1[p1++];
                }
                break;
            }
            if (p1 >= nums1.size() && p2 >= nums2.size()) {
                break;
            }
            // cout << i << ":: " << p1 << ":" << nums1[p1] << "," << p2 << ":" << nums2[p2] << endl;
            if (nums1[p1] < nums2[p2]) {
                a[i] = nums1[p1++];
            } else {
                a[i] = nums2[p2++];
            }
        }
        if (total_size % 2 == 1) {
            return a[total_size / 2];
        } else {
            return (a[total_size/2 - 1] + a[total_size/2]) / 2.;
        }
    }
};