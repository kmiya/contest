# double pointers
# time: O(n)
# space: O(1)
# Runtime: 56 ms, faster than 95.29% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.7 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums): return 0
        if len(nums) == 1: return 1
        w = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[w-1]:
                nums[w] = nums[r]
                w += 1
        return w
