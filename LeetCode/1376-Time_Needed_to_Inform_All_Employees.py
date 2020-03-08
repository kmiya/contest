# iterative solution
# time: O(#nodes)
# space: O(#nodes)


from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = 0
        memo = [-1] * n
        for node, id in enumerate(manager):
            sum = 0
            while node != headID:
                if sum <= memo[node]:
                    sum = memo[node] - informTime[headID]
                    break
                memo[node] = sum
                sum += informTime[node]
                node = manager[node]
            ans = max(ans, sum + informTime[headID])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(1, s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
    print(21, s.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]))
    print(3, s.numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
    print(1076, s.numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]))
    print(3665, s.numOfMinutes(10, 3, [8,9,8,-1,7,1,2,0,3,0], [224,943,160,909,0,0,0,643,867,722]))
    print(2600, s.numOfMinutes(13, 0, [-1,6,6,7,12,1,0,0,12,0,2,6,11], [567,670,351,0,0,0,573,17,0,0,0,594,866]))
    print(3225, s.numOfMinutes(17, 8, [9,7,16,12,0,0,14,6,-1,14,1,6,13,16,8,2,8], [984,971,204,0,0,0,749,636,398,767,0,0,913,128,471,0,186]))
    print(5046, s.numOfMinutes(20,12,[19,6,7,19,18,16,0,5,11,4,17,0,-1,15,4,11,4,6,17,12],[585,0,0,0,940,124,543,257,0,0,0,753,772,0,0,910,368,887,553,17]))
