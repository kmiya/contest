# straight forward
# time: O(M)
# space: O(M)
# Runtime: 620 ms, faster than 48.39% of Python3 online submissions for Image Smoother.
# Memory Usage: 14.1 MB, less than 8.33% of Python3 online submissions for Image Smoother.


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        d = (-1,0,1)
        xlen = len(M[0])
        ylen = len(M)
        ans = []
        for y in range(ylen):
            tmp = [0] * xlen
            for x in range(xlen):
                cnt = 0
                sum = 0
                for dy in d:
                    for dx in d:
                        if x+dx < 0 or x+dx >= xlen or y+dy < 0 or y+dy >= ylen:
                            continue
                        sum += M[y+dy][x+dx]
                        cnt += 1
                tmp[x] = math.floor(sum/cnt) if cnt else 0
            ans.append(tmp)
        return ans
