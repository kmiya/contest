# time: O(mn)
# space: O(m+n)
# Runtime: 40 ms, faster than 80.52% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 13.2 MB, less than 5.34% of Python3 online submissions for Intersection of Two Arrays.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))