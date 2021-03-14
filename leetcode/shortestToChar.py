# https://leetcode.com/problems/shortest-distance-to-a-character/
import time


class Solution:
    def shortestToChar(self, s: str, c: str):
        answer = []
        pid = -1
        tmp = s

        while True:
            tmp = tmp[pid + 1 :]
            if len(tmp) == 0:
                break

            prev = pid
            pid = tmp.find(c)
            print(tmp, pid, prev, answer)
            time.sleep(1)
            if pid == -1:
                answer += [i for i in range(1, len(s) - len(answer) + 1)]
                break

            for i in range(pid + 1):
                if prev == -1:
                    answer.append(pid - i)
                else:
                    idx = prev + 1 + i
                    answer.append(min(pid - i, 1 + i))

        return answer


if __name__ == "__main__":
    sol = Solution()
    # print(f"solution : {sol.shortestToChar('loveleetcode', 'e')}")
    print(f"solution : {sol.shortestToChar('aaba', 'b')}")
