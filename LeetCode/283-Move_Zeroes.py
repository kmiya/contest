# double pointers
# time: O(n)
# space: O(1)
# Runtime: 48 ms, faster than 78.56% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.2 MB, less than 5.21% of Python3 online submissions for Move Zeroes.


class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r in range(len(n)):
            if n[r] != 0:
                n[w] = n[r]
                w += 1
        while w < len(n):
            n[w] = 0
            w += 1
