# time: O(n)
# space: O(n)
# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = ""
        ans = ""
        cnt = 0
        for s in S:
            l += s
            cnt = cnt + 1 if s == '(' else cnt - 1
            if not cnt:
                ans += l[1:-1]
                l = ""
        return ans
