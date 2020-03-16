# time: O(n)
# space: O(1)
# Runtime: 92 ms, faster than 49.79% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 13.2 MB, less than 6.50% of Python3 online submissions for Max Consecutive Ones.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in nums:
            if i:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
