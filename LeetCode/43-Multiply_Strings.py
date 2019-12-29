# time: O( len(num1) * len(num2) )
# space: O( len(num1) + len(num2) )
# Runtime: 68 ms, faster than 58.14% of Python3 online submissions for Multiply Strings.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [ord(x) - ord('0') for x in num1]
        num2 = [ord(x) - ord('0') for x in num2]
        if num1 == [0] or num2 == [0]:
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i+j] += n1 * n2
        not_zero = 0
        for i in range(len(res)-1):
            res[i+1] += res[i] // 10
            res[i] %= 10
            if res[i+1] != 0:
                not_zero = i+1
        return ''.join([chr(x + ord('0')) for x in reversed(res[:not_zero+1])])

if __name__ == "__main__":
    s = Solution()
    test = [ [ "123", "456", "56088" ],
             [ "0", "0", "0"],
             [ "1", "1", "1"],
             [ "9", "9", "81"] ]
    for i in test:
        print(s.multiply(i[0], i[1]), i[2])