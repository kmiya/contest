# straightforward solution
# time: average O(len(s)), worst O(len(s)^2)
# space: O(s)

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        res = []
        sort_l = sorted(count)
        rev = sort_l[::-1]
        while len(res) != len(s):
            for k in sort_l:
                if count[k]:
                    res.append(k)
                    count[k] -= 1
            for k in rev:
                if count[k]:
                    res.append(k)
                    count[k] -= 1
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.sortString("aaaabbbbcccc"))
    print(s.sortString("rat"))
    print(s.sortString("leetcode"))
    print(s.sortString("ggggggg"))
    print(s.sortString("spo"))
    print(s.sortString(""))
