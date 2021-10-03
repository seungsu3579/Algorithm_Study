# https://leetcode.com/problems/gas-station/submissions/
# greedy


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        answer = -1

        for cursor in range(len(gas)):
            my_gas, my_cost = 0, 0
            flag = True
            for i in range(len(gas)):
                idx = (cursor + i) % len(gas)
                my_gas += gas[idx]
                my_cost += cost[idx]

                if my_gas - my_cost < 0:
                    flag = False
                    break

            if flag:
                answer = cursor
                break
            else:
                cursor += 1

        return answer

