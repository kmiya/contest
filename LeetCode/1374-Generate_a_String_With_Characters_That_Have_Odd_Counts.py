# straightforward solution
# time: O(n)
# space: O(n)


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        return 'a' * n


if __name__ == "__main__":
    s = Solution()
    print(s.generateTheString(0))
    print(s.generateTheString(2))
    print(s.generateTheString(3))
