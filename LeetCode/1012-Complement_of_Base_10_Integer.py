class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a = list(bin(N))
        for n in range(2,len(a)):
            a[n] = "1" if a[n] == "0" else "0"
        return int("".join(a[2:]),2)
