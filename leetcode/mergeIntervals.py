# https://leetcode.com/problems/merge-intervals

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        before_length = pow(10, 5)
        intervals.sort(key=lambda x: x[0])

        while before_length != len(intervals):

            before_length = len(intervals)

            tmp = list()
            idx = 0
            while idx < len(intervals) and len(intervals) != 1:

                if idx == len(intervals) - 1:
                    tmp.append(intervals[idx])
                else:
                    a = intervals[idx]
                    b = intervals[idx + 1]

                    if a[1] >= b[0]:
                        new = [min(a[0], b[0]), max(a[1], b[1])]
                        tmp.append(new)
                        idx += 1
                    else:
                        tmp.append(a)
                idx += 1

            if len(intervals) != 1:
                intervals = tmp

        return intervals


if __name__ == "__main__":

    s = Solution()
    # print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge1([[1, 4], [0, 2], [3, 5]]))

