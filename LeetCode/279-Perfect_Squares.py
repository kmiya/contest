# BFS solution with deque
# time: O(sqrt(n) * n)
# space: O(sqrt(n) * n)

from math import floor, sqrt
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        ans = n
        q = deque()
        q.append((0, 0))
        max_num = floor(sqrt(n))
        squares = [i ** 2 for i in range(0, max_num + 1)]
        while len(q):
            num, val = q.popleft()
            for i in range(max_num, 0, -1):
                tmp = val + squares[i]
                if tmp == n:
                    ans = min(ans, num + 1)
                    return ans
                elif tmp < n:
                    q.append((num + 1, tmp))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(42))
