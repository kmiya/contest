# straightforward solution (not efficient if the number of escape texts is large)
# time: O(#text)
# space: O(#text)


class Solution:
    def entityParser(self, text: str) -> str:
        ans = text
        escape = ["&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"]
        html = ["\"", "\'", "&", ">", "<", "/"]
        d = {t: h for t, h in zip(escape, html)}
        for i, v in d.items():
            ans = ans.replace(i, v)
        return ans
