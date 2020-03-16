# time: O(n*n)
# space: O(1)
# Runtime: 32 ms, faster than 86.84% of Python3 online submissions for Rotate Image.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate Image.

from typing import List


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(m)
        for i in range(l//2):
            for j in range(i, l-1-i):
                # can use '~x' instead of 'l-1-x'
                n1 = m[i][j]
                n2 = m[j][l-1-i]
                n3 = m[l-1-i][l-1-j]
                m[i][j] = m[l-1-j][i]
                m[j][l-1-i] = n1
                m[l-1-i][l-1-j] = n2
                m[l-1-j][i] = n3


if __name__ == "__main__":
    test = [ [ [ [ 5, 1, 9,11],
                 [ 2, 4, 8,10],
                 [13, 3, 6, 7],
                 [15,14,12,16] ],
               [ [15,13, 2, 5],
                 [14, 3, 4, 1],
                 [12, 6, 8, 9],
                 [16, 7,10,11] ]
             ],
             [
                 [[1]],[[1]]
             ],
             [
                 [[1,2],[3,4]],
                 [[3,1],[4,2]]
             ]
    ]
    s = Solution()
    for i in test:
        s.rotate(i[0])
        print(i[0])
        print(i[1])