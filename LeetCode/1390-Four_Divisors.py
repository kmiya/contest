# time: O(len(nums) * sqrt(max value in nums))
# space: O(1)

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            if n < 6:
                continue
            div = []
            for i in range(1, int(n**0.5) + 1):
                if len(div) > 4:
                    break
                if n % i == 0:
                    div.append(i)
                    if i != n // i:
                        div.append(n // i)
            if len(div) == 4:
                ret += sum(div)
        return ret


if __name__ == "__main__":
    s = Solution()
    print(32, s.sumFourDivisors([21,4,7]))
    print(64, s.sumFourDivisors([21,4,7,21]))
