# bruteforce with pruning solution
# time: O(sqrt(num))
# space: O(1)

import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        n1 = num + 1
        n2 = num + 2
        high = int(math.sqrt(n2))
        ans = [1, n2]
        for i in range(high, 0, -1):
            if n2 % i == 0:
                d1, d2 = int(n2 / i), i
                if abs(d1 - d2) < ans[1] - ans[0]:
                    ans = [min(d1, d2), max(d1, d2)]
        for i in range(high, ans[0] - 1, -1):
            if n1 % i == 0:
                d1, d2 = int(n1 / i), i
                if abs(d1 - d2) < ans[1] - ans[0]:
                    ans[0], ans[1] = min(d1, d2), max(d1, d2)
        return ans


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        print(i, s.closestDivisors(i))
    print(s.closestDivisors(123))
    print(s.closestDivisors(999))
