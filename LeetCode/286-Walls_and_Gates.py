# BFS solution
# time: O(mn)
# space: O(mn)

from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        queue = deque()
        ymax = len(rooms)
        xmax = len(rooms[0])
        for i in range(ymax):
            for j in range(xmax):
                if rooms[i][j] == 0:
                    queue.append((j, i, 0))
        while len(queue):
            x, y, val = queue.popleft()
            if not (0 <= x < xmax and 0 <= y < ymax):
                continue
            if rooms[y][x] == -1:
                continue
            if rooms[y][x] == 0 and val != 0:
                continue
            if 0 < rooms[y][x] <= val:
                continue
            rooms[y][x] = val
            queue.append((x, y - 1, val + 1))
            queue.append((x - 1, y, val + 1))
            queue.append((x + 1, y, val + 1))
            queue.append((x, y + 1, val + 1))
