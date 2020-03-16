# time: O(n)
# space: O(n), O(1) if one uses (double) pointer(s)
# Runtime: 64 ms, faster than 68.04% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.8 MB, less than 18.67% of Python3 online submissions for Valid Palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.findall('[a-z0-9]*', s.lower())
        joined = "".join(t)
        return joined == joined[::-1]
