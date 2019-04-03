# time: O(n)
# space: O(1)
# Runtime: 104 ms, faster than 66.56% of Python3 online submissions for Max Consecutive Ones II.
# Memory Usage: 13.4 MB, less than 5.55% of Python3 online submissions for Max Consecutive Ones II.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre = cnt = ans = 0
        has0 = False
        for i in range(len(nums)):
            if not nums[i]:
                if has0:
                    cnt = i - (pre + 1)
                else:
                    has0 = True
                pre = i
            cnt += 1
            ans = max(ans, cnt)
        return ans