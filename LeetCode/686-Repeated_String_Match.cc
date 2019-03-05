// Runtime: 1296 ms, faster than 6.71% of C++ online submissions for Repeated String Match.
// Memory Usage: 280.4 MB, less than 12.26% of C++ online submissions for Repeated String Match.

class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int result = -1;
        for (int i = 0; i < A.size(); ++i) {
            result = repeat(A, B, i);
            if (result != -1) break;
        }
        return result;
    }
    int repeat(string A, string B, int pa) {
        int pb = 0;
        while (pb < B.size()) {
            //cout << pa << "," << pb << "," << A[pa % A.size()] << "," << B[pb] << endl;
            if (A[pa++ % A.size()] != B[pb++]) return -1;
        }
        return ceil(double(pa) / A.size());
    }
};