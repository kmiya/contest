# time: O(n^2)
# space: O(n)

from typing import List
import copy


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = [nums[0]]
        for i in range(1, len(nums)):
            left = ret[0:index[i]] + [nums[i]] + ret[index[i]:]
            ret = copy.deepcopy(left)
        return ret


if __name__ == "__main__":
    s = Solution()
    print("[0,4,1,3,2]", s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
    print("[0,1,2,3,4]", s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
    print("[1]", s.createTargetArray([1], [0]))
