# Time: O(1) 4^4 constant solution
# Space: O(1)
# Runtime: 44 ms, faster than 39.07% of Python3 online submissions for Next Closest Time.
# Memory Usage: 13.1 MB, less than 5.55% of Python3 online submissions for Next Closest Time.


class Solution:
    def nextClosestTime(self, time: str) -> str:
        allowed = [time[0], time[1], time[3], time[4]]
        current = int(time[:2]) * 60 + int(time[3:])
        result = 24 * 60
        for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
            if (int(h1+h2) >= 24): continue
            if (int(m1+m2) >= 60): continue
            comp = int(h1 + h2) * 60 + int(m1+m2)
            if comp == current: continue
            result = min(result, (comp - current) % (24 * 60))
        out = (current + result) % (24 * 60)
        return "{:02}:{:02}".format(out // 60, out % 60)
