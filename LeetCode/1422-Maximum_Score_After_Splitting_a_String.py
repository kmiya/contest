# time: O(#s)
# space: O(1)


class Solution:
    def maxScore(self, s: str) -> int:
        num_ones = s.count('1')
        num_zeros = 0
        score = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                num_zeros += 1
            else:
                num_ones -= 1
            score = max(score, num_zeros + num_ones)
        return score


if __name__ == "__main__":
    s = Solution()
    print(5, s.maxScore("011101"))
    print(5, s.maxScore("00111"))
    print(3, s.maxScore("1111"))
    print(3, s.maxScore("0000"))
