# Greedy solution
# time: O(n)
# space: O(1)
# Runtime: 140 ms, faster than 61.77% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.5 MB, less than 44.21% of Python3 online submissions for Container With Most Water.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        while l != r:
            area = min(height[l], height[r]) * (r - l)
            result = max(result, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result


s = Solution()
print(49, s.maxArea([1,8,6,2,5,4,8,3,7]))
print(4, s.maxArea([1,2,4,3]))
print(17, s.maxArea([2,3,4,5,18,17,6]))
print(72, s.maxArea([9,6,14,11,2,2,4,9,3,8]))
print(72, s.maxArea([8,6,14,11,2,2,4,9,3,9]))
test = [75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]
print(14608, s.maxArea(test))
print(25, s.maxArea([10,9,8,7,6,5,4,3,2,1]))
print(18048, s.maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]))