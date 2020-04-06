# solution using set
# time: O(log(n))
# space: O(lon(n))


class Solution:
    def isHappy(self, n: int) -> bool:
        t = n
        hist = set()
        while t != 1:
            ans = 0
            for i in str(t):
                ans += int(i) ** 2
            if ans in hist:
                return False
            hist.add(ans)
            t = ans
        return True
