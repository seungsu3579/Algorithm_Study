# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:

        tmp = s.lstrip()

        if len(tmp) == 0:
            return 0

        pn = "+"
        if tmp[0] in "+-":
            pn = tmp[0]
            tmp = tmp[1:]

        for i in range(len(tmp)):
            if tmp[i] not in "0123456789":
                tmp = tmp[:i]
                break

        number = pn + tmp

        try:
            number = int(float(number))
        except:
            return 0

        if number > (2 ** 31 - 1):
            number = 2 ** 31 - 1
        elif number < (-1) * (2 ** 31):
            number = (-1) * (2 ** 31)

        return number


s = Solution()
print(s.myAtoi("   -42"))
