# hash solution
# time: average O(#arr)
# space: O(#arr)

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        ans = 0
        for i in arr:
            if i + 1 in s:
                ans += 1
        return ans
