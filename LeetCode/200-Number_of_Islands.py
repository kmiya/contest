# DFS solution
# time: O(mn)
# space: O(mn)

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
        xmax, ymax = len(grid[0]), len(grid)
        count = 0
        for y in range(ymax):
            for x in range(xmax):
                if grid[y][x] == "1":
                    count += 1
                    q = deque()
                    q.append((x, y))
                    while q:
                        i, j = q.popleft()
                        for dx, dy in delta:
                            if not (0 <= i + dx < xmax and 0 <= j + dy < ymax):
                                continue
                            if grid[j + dy][i + dx] == "1":
                                grid[j + dy][i + dx] = "0"
                                q.append((i + dx, j + dy))
        return count
