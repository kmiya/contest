# time: O(n)
# space: almost O(n)
# Runtime: 84 ms, faster than 36.22% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 1
        dic = { s[i]: 1 }
        res = 1
        while i < len(s) - 1 and j < len(s):
            if s[j] not in dic or not dic[s[j]]:
                dic[s[j]] = 1
                res = max(res, j - i + 1)
                j += 1
            else:
                dic[s[i]] = 0
                i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(""), 0)
    print(s.lengthOfLongestSubstring("dvdf"), 3)
    print(s.lengthOfLongestSubstring("aaaaaa"), 1)
    print(s.lengthOfLongestSubstring("abcabcbb"), 3)
    print(s.lengthOfLongestSubstring("pwwkew"), 3)
    print(s.lengthOfLongestSubstring("abcabcd"), 4)
    print(s.lengthOfLongestSubstring("a"), 1)
    print(s.lengthOfLongestSubstring("au"), 2)
