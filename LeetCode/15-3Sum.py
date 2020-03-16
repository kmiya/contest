# time: O(n*n)
# space: O(1)
# Runtime: 732 ms, faster than 86.32% of Python3 online submissions for 3Sum.
# Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            while len(nums) > i > 0 and nums[i-1] == nums[i]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sumup = nums[i] + nums[j] + nums[k]
                if sumup < 0:
                    j += 1
                elif sumup > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1],[-1, -1, 2]])
    print(s.threeSum([]), [])
    print(s.threeSum([1]), [])
    print(s.threeSum([-1,1]), [])
    print(s.threeSum([0]), [])
    print(s.threeSum([0, 0]), [])
    print(s.threeSum([0, 0, 0]), [[0, 0, 0]])
    print(s.threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0]), [[0, 0, 0]])
    print(s.threeSum([-1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]), [[-1, 0, 1], [0, 0, 0]])
    print(s.threeSum([-1, -1, 0, 1]), [[-1, 0, 1]])
    print(s.threeSum([1,2,3]), [])
    print(s.threeSum([1,1,-2]), [[-2,1,1]])
    print(s.threeSum([-2,1,1]), [[-2,1,1]])
    print(s.threeSum([-1,0,1,0]), [[-1,0,1]])
    input = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    expect = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    print(s.threeSum(input), '\n', expect)
#             0   1   2   3   4   5   6   7  8  9 10 11 12 13 14 15
    input = [-5, -5, -4, -4, -4, -2, -2, -2, 0, 0, 0, 1, 1, 3, 4, 4]
    expect = [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
    print(s.threeSum(input), '\n', expect)
