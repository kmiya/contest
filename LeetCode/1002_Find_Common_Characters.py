class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        for i in A[0]:
            index = 1
            for a in A[1:]:
                flag = False
                if i not in a:
                    flag = True
                    break
                b = list(a)
                b.remove(i)
                A[index] = "".join(b)
                index += 1
            if not flag:
                ans.append(i)
        # print(ans)
        return ans