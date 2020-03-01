# ref: huzecong's code of Weekly Contest 178
# time: O(#teams * #votes)
# space: O(#teams * #votes)


from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        num = len(votes[0])
        dic = defaultdict(lambda: [0] * num)
        for vote in votes:
            for i, team in enumerate(vote):
                dic[team][i] += 1
        rank = sorted(dic.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return ''.join([k for k, v in rank])


if __name__ == "__main__":
    s = Solution()
    print("ACB", s.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    print("XWYZ", s.rankTeams(["WXYZ","XYZW"]))
    print("ZMNAGUEDSJYLBOPHRQICWFXTVK", s.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print("ABC", s.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
    print("M", s.rankTeams(["M", "M", "M"]))