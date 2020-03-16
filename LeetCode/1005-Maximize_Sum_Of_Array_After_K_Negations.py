# Short but slow solution
# Time: O(N * N log N)
# Space: O(N)


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        sa = sorted(A)
        for k in range(K):
            sa[0] *= -1
            sa = sorted(sa)
        return sum(sa)
