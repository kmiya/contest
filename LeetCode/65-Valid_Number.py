# time 100% DFA solution
# time: O(n)
# space: O(1)
# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Valid Number.
# Memory Usage: 13.1 MB, less than 5.71% of Python3 online submissions for Valid Number.
class Solution:
    def isNumber(self, s: str) -> bool:
        if s.count('e') > 1: return False
        if s.count('.') > 1: return False
        if s == '.': return False
        if s.find('e') != -1 and s.find('.') != -1 and s.find('e') < s.find('.'): return False
        s = s.strip()
        status = "start"
        for i in s:
            if i == ' ': return False
            if status == "start" or status == "exp":
                if   i == 'e': return False
                elif i == '-' or i == '+':
                    status = "sign"
                elif i == '.':
                    status = "point"
                elif i.isdigit():
                    status = "digit"
                else: return False
            elif status == "sign":
                if i.isdigit():
                    status = "digit"
                elif i == '.':
                    status = "point"
                else: return False
            elif status == "digit":
                if i.isdigit():
                    continue
                elif i == 'e':
                    status = "exp"
                elif i == '.':
                    status = "npoint"
                else: return False
            elif status == "point":
                if i.isdigit():
                    status = "digit"
                else: return False
            elif status == "npoint":
                if i.isdigit():
                    status = "digit"
                elif i == 'e':
                    status = "exp"
                else: return False
        return status == "digit" or status == "npoint"