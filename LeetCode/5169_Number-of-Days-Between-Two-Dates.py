# straightforward solution
# time: O(1)
# space: O(1)

import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        return abs(int((d1 - d2).days))


if __name__ == "__main__":
    s = Solution()
    print(s.daysBetweenDates("2019-06-29", "2019-06-30"))
    print(s.daysBetweenDates("2020-01-15", "2019-12-31"))
