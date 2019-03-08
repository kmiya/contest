class Solution:
    def isValid(self, S: str) -> bool:
        abc = "abc"
        jsp = S
        while len(jsp) >= 3:
            jsp = "".join(jsp.split(abc))
            if jsp and abc not in jsp:
                return False
        return True if not jsp else False