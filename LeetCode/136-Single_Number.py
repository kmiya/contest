# time: O(nums)
# space: O(nums)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * (sum(set(nums))) - sum(nums)
