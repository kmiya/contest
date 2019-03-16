# Two pointers solution
# time: O(N)
# space: O(k)
# Runtime: 112 ms, faster than 33.30% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
# Memory Usage: 13.3 MB, less than 5.79% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> int:
        if not s or not k: return 0
        d = dict()
        b = e = ans = 0
        while e < len(s):
            d[s[e]] = d.get(s[e], 0) + 1
            e += 1
            while len(d) > k and b < e:
                key = s[b]
                if d.get(key,0) > 0:
                    d[key] = d[key] - 1
                    if not d[key]:
                        del d[key]
                b += 1
            ans = max(ans, e-b)
        return ans