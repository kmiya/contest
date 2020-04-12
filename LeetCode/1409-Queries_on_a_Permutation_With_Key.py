# time: O(#q * m)
# space: (#q + m)

from typing import List
from collections import deque


class Solution:
    def processQueries(self, q: List[int], m: int) -> List[int]:
        ans = []
        d = deque(range(1, m + 1))
        for i in q:
            pos = d.index(i)
            ans.append(pos)
            d.remove(i)
            d.appendleft(i)
        return ans
