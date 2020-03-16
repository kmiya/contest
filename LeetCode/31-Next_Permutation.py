# time: O(n)
# space: O(1)
# Runtime: 36 ms, faster than 94.52% of Python3 online submissions for Next Permutation.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Next Permutation.

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for k in range(len(nums)-1, i, -1):
                    if nums[k] > nums[i]:
                        nums[k], nums[i] = nums[i], nums[k]
                        break
                for j in range(0, (len(nums) - 1 - i) // 2):
                    nums[i+1+j], nums[-j-1] = nums[-j-1], nums[i+1+j]
                return

        nums.reverse()


def test(test, expect):
    s = Solution()
    s.nextPermutation(test)
    print(test, expect)


if __name__ == "__main__":
    test([1,2,3],[1,3,2])
    test([3,2,1],[1,2,3])
    test([1,1,5],[1,5,1])
    test([1,1],[1,1])
    test([1,9],[9,1])
    test([1,2,3,4,5],[1,2,3,5,4])
    test([1,4,3,6,4],[1,4,4,3,6])
    test([1,1,1,5,1,1,1],[1,1,5,1,1,1,1])
    test([8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8])
    test([7,6,5,4,3,2,1],[1,2,3,4,5,6,7])
