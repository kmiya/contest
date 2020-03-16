# stack solution
# time: O(n)
# space: O(n)
# Runtime: 36 ms, faster than 84.52% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.


class Solution:
    def isValid(self, s: str) -> bool:
        def isPair(t, l):
            if not l:
                return False
            if l[-1] == t:
                l.pop()
                return True
            return False

        if not s: return True
        l = []
        for i in s:
            if i in '({[':
                l.append(i)
            elif i == ')':
                if not isPair('(', l):
                    return False
            elif i == '}':
                if not isPair('{', l):
                    return False
            elif i == ']':
                if not isPair('[', l):
                    return False
        return len(l) == 0
