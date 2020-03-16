# brute force solution
# time: O(N^2)
# space: O(N)
# Runtime: 460 ms, faster than 10.66% of Python3 online submissions for Add Bold Tag in String.
# Memory Usage: 15 MB, less than 6.90% of Python3 online submissions for Add Bold Tag in String.


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        sl = [0] * len(s)
        el = [0] * len(s)
        for v in dict:
            # Using lookahead to find all overlapping matches
            # Can simplify by using regex library instead of re
            pos = [x for x in re.finditer("(?="+v+")", s)]
            for p in pos:
                if p.start() != -1:
                    sl[p.start()] += 1
                    el[p.start()+len(v)-1] += 1
        ans = ""
        paren = 0
        for i in range(len(s)):
            if paren:
                ans += s[i]
                if sl[i]:
                    paren += sl[i]
            else:
                if sl[i]:
                    paren = sl[i]
                    ans += "<b>"
                ans += s[i]
            if el[i]:
                paren -= el[i]
                if not paren:
                    ans += "</b>"
        return ans.replace("</b><b>","")
