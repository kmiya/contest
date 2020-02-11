# Algorithm explained in Solution page
# time: O(N)
# space: O(1)
# Runtime: 32 ms, faster than 79.23% of Python3 online submissions for First Missing Positive.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # case: nums = []
        if not nums:
            return 1

        if 1 not in nums:
            return 1

        if [1] == nums:
            return 2

        for i, n in enumerate(nums):
            if n <= 0 or n > len(nums):
                nums[i] = 1

        for i, n in enumerate(nums):
            if abs(n) == len(nums):
                nums[0] = -1 * abs(nums[0])
            else:
                nums[abs(n)] = -1 * abs(nums[abs(n)])

        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return len(nums)

        return len(nums) + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
    print(s.firstMissingPositive([1]))
    print(s.firstMissingPositive([0]))
    print(s.firstMissingPositive([2, 1, 3]))
