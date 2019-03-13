# Time: O(N)
# Space: O(N)
# Runtime: 124 ms, faster than 23.85% of Python3 online submissions for License Key Formatting.
# Memory Usage: 13.3 MB, less than 25.61% of Python3 online submissions for License Key Formatting.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        tmp = S.replace("-", "").upper()
        if K >= len(tmp): return tmp
        ans = ""
        i = 1
        while len(tmp) > K:
            if i == K:
                ans = tmp[-i:] + "-" + ans if ans else tmp[-i:]
                tmp = tmp[:-i]
            i = (i + 1) % (K + 1)
        return tmp + "-" + ans if tmp else ans