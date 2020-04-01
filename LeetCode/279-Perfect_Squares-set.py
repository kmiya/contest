# BFS solution with set
# time: O(sqrt(n)^2 * max_level)
# space: O(sqrt(n)^2)

from math import floor, sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        level = 0
        q = {0}
        squares = [i ** 2 for i in range(0, floor(sqrt(n)) + 1)]
        while len(q):
            level += 1
            new_q = set()
            for item in q:
                for s in squares:
                    tmp = item + s
                    if tmp == n:
                        return level
                    elif tmp < n:
                        new_q.add(tmp)
                    else:
                        break
            q = new_q
        return level
