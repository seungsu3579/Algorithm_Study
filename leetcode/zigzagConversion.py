# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        text = [[] for i in range(numRows)]

        cursor = 0
        flag = True

        for ch in s:

            if len(text) == 1:
                text[0].append(ch)
                continue

            # write
            if flag:
                text[cursor].append(ch)
                cursor += 1

                if cursor >= len(text):
                    flag = False
                    cursor -= 2
            else:
                text[cursor].append(ch)
                cursor -= 1

                if cursor == -1:
                    flag = True
                    cursor += 2

        answer = ""
        for line in text:
            print(line)
            answer += "".join(line)

        return answer


s = Solution()

# print(s.convert("PAYPALISHIRING", 3))
print(s.convert("ABC", 1))
