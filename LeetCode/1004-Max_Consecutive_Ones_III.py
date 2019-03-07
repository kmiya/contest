# Sliding Window
# Time: O(N)
# Space: O(N)
# Runtime: 300 ms, faster than 12.03% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones III.
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = cnt = 0
        s, e = 0, -1
        while True:
            if e + 1 >= len(A): break
            if A[e+1] == 1:
                e += 1
                if K == 0 and A[s] == 0:
                    s += 1
                    cnt = max(cnt - 1, 0)
                ans = max(ans, e - s + 1)
            else: # A[e+1] == 0
                if cnt < K:
                    e += 1
                    cnt += 1
                    ans = max(ans, e - s + 1)
                else:
                    if A[s] == 0:
                        cnt = max(cnt - 1, 0)
                    s += 1
                    if e < s:
                        e += 1
            # print(cnt,":",s,e,A[s:e+1],ans)
        return ans