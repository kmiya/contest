# BFS solution
# time: O(10^4 * 4^2 + #deadends)
# space: O(10^4 + #deadends)

from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        hist = [False] * 10000
        q = deque()
        q.append((0, 0, 0, 0, 0))
        deads = set(deadends)
        while len(q):
            a, b, c, d, num = q.popleft()
            wheels = "".join([str(v) for v in [a, b, c, d]])
            if wheels == target:
                return num
            if wheels in deads:
                continue
            wheel_num = [a, b, c, d]
            for i, v in enumerate(wheel_num):
                tmp = wheel_num[:]
                for diff in [1, -1]:
                    tmp[i] = (wheel_num[i] + diff) % 10
                    index = 1000 * tmp[0] + 100 * tmp[1] + 10 * tmp[2] + tmp[3]
                    if not hist[index]:
                        q.append((tmp[0], tmp[1], tmp[2], tmp[3], num + 1))
                        hist[index] = True
        return -1
