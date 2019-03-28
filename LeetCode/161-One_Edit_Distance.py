# time: O(n)
# space: O(1)
# Runtime: 40 ms, faster than 68.32% of Python3 online submissions for One Edit Distance.
# Memory Usage: 13.1 MB, less than 5.05% of Python3 online submissions for One Edit Distance.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            s, t = t, s
        if len(s) - len(t) > 1:
            return False
        if len(s) - len(t) == 1:
            for i in range(len(s)):
                if s[0:i] + s[i+1:] == t:
                    return True
            return False
        cnt = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if cnt:
                    return False
                cnt = True
        return cnt