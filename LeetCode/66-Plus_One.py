# Runtime: 56 ms, faster than 19.63% of Python3 online submissions for Plus One.
# Memory Usage: 13.2 MB, less than 5.29% of Python3 online submissions for Plus One.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(x) for x in digits])) + 1
        return [int(x) for x in str(num)]