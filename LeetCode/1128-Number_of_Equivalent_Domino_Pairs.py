# time: O(n)
# space: almost O(1)
#Runtime: 236 ms, faster than 99.45% of Python3 online submissions for Number of Equivalent Domino Pairs.
#Memory Usage: 21.9 MB, less than 100.00% of Python3 online submissions for Number of Equivalent Domino Pairs.

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = dominoes
        dic = {}
        for a, b in d:
            num = 10*min(a, b) + max(a, b)
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        res = 0
        for v in dic.values():
            res += v*(v-1) // 2
        return res