# double pointers
# time: O(#S + #T)
# space: O(1)


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skip_i, skip_j = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and S[i] == '#':
                skip_i += 1
                i -= 1
            while j >= 0 and T[j] == '#':
                skip_j += 1
                j -= 1
            if skip_i > 0:
                i = max(i - 1, -1)
                skip_i -= 1
                continue
            if skip_j > 0:
                j = max(j - 1, -1)
                skip_j -= 1
                continue
            # print(i, S[i], j, T[j], skip_i, skip_j)
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return False if i != j else True


if __name__ == "__main__":
    s = Solution()
    print(True, s.backspaceCompare("ab#c", "ad#c"))
    print(True, s.backspaceCompare("ab##", "c#d#"))
    print(True, s.backspaceCompare("a##c", "#a#c"))
    print(False, s.backspaceCompare("a#c", "b"))
    print(True, s.backspaceCompare("###", "###"))
    print(True, s.backspaceCompare("#", "###"))
    print(True, s.backspaceCompare("bxj##tw", "bxo#j##tw"))
    print(False, s.backspaceCompare("bxj##tw", "bxj###tw"))
