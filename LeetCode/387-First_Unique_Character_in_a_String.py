# time: O(n)
# space: O(n)
# Runtime: 116 ms, faster than 68.81% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13.3 MB, less than 5.04% of Python3 online submissions for First Unique Character in a String.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        ans = 0
        for i in s:
            if c[i] == 1:
                return ans
            else:
                ans += 1
        return -1
