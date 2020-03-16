# RE solution
# time: average O(n) -- deepends on the complexity of re library
# time: O(len(queries) + len(pattern)) -- deepends on the complexity of re library
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Camelcase Matching.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Camelcase Matching.


class Solution:
    def camelMatch(self, que: List[str], pat: str) -> List[bool]:
        np = "[a-z]*"
        for p in pat:
            np += p
            np += "[a-z]*"
        reg = re.compile(np)
        ans = []
        for q in que:
            res = re.fullmatch(reg,q)
            if not res:
                ans.append(False)
            else:
                ans.append(True)
        return ans
