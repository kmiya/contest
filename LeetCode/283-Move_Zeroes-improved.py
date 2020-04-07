# double pointers (Solution #3)
# time: O(n)
# space: O(1)

from typing import List


class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r in range(len(n)):
            if n[r] != 0:
                n[r], n[w] = 0, n[r]
                w += 1
