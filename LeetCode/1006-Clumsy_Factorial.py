class Solution:
    def clumsy(self, N: int) -> int:
        ope = ['*', '//', '+', '-']
        ans = ''
        for i in range(N - 1):
            ans += str(N) + ope[i % 4]
            N -= 1
        ans += str(N)
        return eval(ans)
