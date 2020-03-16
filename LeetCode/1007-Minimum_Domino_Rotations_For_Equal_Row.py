# Time: O(N)


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        def calc(i, A, B):
            ans = 20001
            count = 0
            finish = True
            for j in range(len(A)):
                if A[j] == i: continue
                else:
                    if B[j] == i: count += 1
                    else:
                        finish = False
                        break
            if finish: ans = min(ans, count)
            return ans

        ans = 20001
        for i in range(1,7):
            ans1 = calc(i, A, B)
            ans2 = calc(i, B, A)
            ans = min(ans, ans1, ans2)
        return ans if ans != 20001 else -1
