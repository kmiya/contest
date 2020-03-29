# time: average O(n)
# space: O(n)

from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ret = -1
        d = Counter(arr)
        for k, v in d.items():
            if k == v:
                ret = max(ret, k)
        return ret
