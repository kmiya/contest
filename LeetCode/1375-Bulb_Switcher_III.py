# solution based on awice's code of the weekly contest 179
# time: O(len(light))
# space: O(1)

from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = ret = 0
        for i, v in enumerate(light):
            right = max(right, v - 1)
            if i == right:
                ret += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(3, s.numTimesAllBlue([2,1,3,5,4]))
    print(2, s.numTimesAllBlue([3,2,4,1,5]))
    print(1, s.numTimesAllBlue([4,1,2,3]))
    print(3, s.numTimesAllBlue([2,1,4,3,6,5]))
    print(6, s.numTimesAllBlue([1,2,3,4,5,6]))
    print(1, s.numTimesAllBlue([3,2,1]))
