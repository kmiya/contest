# straight forward solution
# time: O(n)
# space: O(n)
# Runtime: 912 ms, faster than 25.00% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cat = ""
        ans = []
        for s in A:
            cat += str(s)
            dec = int(cat, 2)
            ans.append(dec % 5 == 0)
        return ans
