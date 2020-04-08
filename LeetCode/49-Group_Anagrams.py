# hash solution
# time: average O(#strs * s * log(s)) where s is the maximum length of a string in strs
# space: O(#strs * s)

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key not in group:
                group[key] = [i]
            else:
                group[key].append(i)
        return group.values()
