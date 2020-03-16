# DFS solution
# time: O(mn)
# space: O(mn)
# Runtime: 100 ms, faster than 100.00% of Python3 online submissions for Number of Enclaves.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Number of Enclaves.


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def rec(x, y):
            if x < 0 or y < 0 or x >= len(A[0]) or y >= len(A):
                return
            if A[y][x]:
                A[y][x] = 0
                rec(x,y-1)
                rec(x-1,y)
                rec(x+1,y)
                rec(x,y+1)
        for x in range(len(A[0])):
            rec(x,0)
            rec(x,len(A)-1)
        for y in range(len(A)):
            rec(0,y)
            rec(len(A[0])-1,y)
        return sum(sum(row) for row in A)
