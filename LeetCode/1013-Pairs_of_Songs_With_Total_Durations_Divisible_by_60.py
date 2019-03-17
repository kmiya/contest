class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        a = [0] * 60
        for i in time: a[i%60] += 1
        ans = 0
        for i in range(1,30):
            ans += a[i] * a[60-i]
        ans += a[0] * (a[0]-1) // 2
        ans += a[30] * (a[30]-1) // 2
        return ans