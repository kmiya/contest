# straight forward solution
# time: O(h*w)
# space: O(h*w)
# Runtime: 40 ms, faster than 57.63% of Python3 online submissions for Game of Life.
# Memory Usage: 13.4 MB, less than 5.79% of Python3 online submissions for Game of Life.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        hlen = len(board)
        wlen = len(board[0])
        dx = (-1, 0, 1)
        dy = (-1, 0, 1)
        ans = []
        for h in range(hlen):
            b = [0] * wlen
            for w in range(wlen):
                cnt = 0
                for y in dy:
                    for x in dx:
                        if not x and not y: continue
                        if w + x < 0 or h + y < 0 or w + x >= wlen or h + y >= hlen: continue
                        cnt += board[h + y][w + x]
                if cnt < 2: b[w] = 0
                elif cnt == 2: b[w] = board[h][w]
                elif cnt == 3: b[w] = 1
                else: b[w] = 0
            ans.append(b)
        for h in range(hlen):
            for w in range(wlen):
                board[h][w] = ans[h][w]