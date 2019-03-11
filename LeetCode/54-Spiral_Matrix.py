# Time: O(N)
# Runtime: 36 ms, faster than 57.75% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.3 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        if not m: return m
        xmin, ymin = 0, 0
        ans = []
        xlast, ylast = len(m[0]), len(m)
        i = 0
        max_size = xlast * ylast
        while i < max_size:
            for xi in range(xmin, xlast):
                ans.append(m[ymin][xi])
                i+=1
            if i >= max_size: break
            ymin += 1
            for yi in range(ymin, ylast):
                ans.append(m[yi][xlast-1])
                i+=1
            if i >= max_size: break
            xlast -= 1
            for xi in range(xlast, xmin, -1):
                ans.append(m[ylast-1][xi-1])
                i+=1
            if i >= max_size: break
            ylast -= 1
            for yi in range(ylast, ymin, -1):
                ans.append(m[yi-1][xmin])
                i+=1
            xmin += 1
        return ans