# dynamic programming
# time: O(mn)
# space: O(mn)
# Runtime: 192 ms, faster than 79.39% of Python3 online submissions for Edit Distance.
# Memory Usage: 16.9 MB, less than 15.76% of Python3 online submissions for Edit Distance.


class Solution:
    def minDistance(self, s: str, t: str) -> bool:
        tmp = [0]
        for i in range(1,len(s)+1):
            tmp += [i]
        mat = [tmp]
        for i in range(1,len(t)+1):
            mat.append([i] + [0] * len(s))
        for ti in range(1,len(t)+1):
            for si in range(1,len(s)+1):
                if s[si-1] == t[ti-1]:
                    mat[ti][si] = min(mat[ti-1][si]+1, mat[ti][si-1]+1, mat[ti-1][si-1])
                else:
                    mat[ti][si] = min(mat[ti-1][si]+1, mat[ti][si-1]+1, mat[ti-1][si-1]+1)
        return mat[len(t)][len(s)]
