# bruteforce solution
# time: O(n^3)
# space: O(1)

from typing import List


class Solution:
    def numTeams(self, r: List[int]) -> int:
        ret = 0
        for i in range(len(r)):
            for j in range(i, len(r)):
                for k in range(j, len(r)):
                    if r[i] < r[j] < r[k] or r[i] > r[j] > r[k]:
                        ret += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(3, s.numTeams([2,5,3,4,1]))
    print(0, s.numTeams([2,1,3]))
    print(4, s.numTeams([1,2,3,4]))
