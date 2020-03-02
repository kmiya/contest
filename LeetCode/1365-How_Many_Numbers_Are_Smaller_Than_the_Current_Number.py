# straightforward solution
# time: O(#nums * #nums)
# space: O(#nums)


from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    ret[i] += 1
        return ret
