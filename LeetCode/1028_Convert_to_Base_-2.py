# https://en.wikipedia.org/wiki/Negative_base#Calculation
# time: O(log(N,-2))
# space: O(log(N,-2))
# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Convert to Base -2.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Convert to Base -2.
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        res = N
        ans = ""
        while res:
            res, a = divmod(res, -2)
            if a < 0:
                res, a = res + 1, a + 2
            ans = str(a) + ans
        return ans