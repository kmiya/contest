class Solution:
    def isValid(self, S: str) -> bool:
        abc = "abc"
        jsp = S
        while len(jsp) >= 3:
            jsp = "".join(jsp.split(abc))
            # print(jsp)
            if jsp != "" and abc not in jsp:
                return False
        if jsp == "":
            return True
        else:
            return False