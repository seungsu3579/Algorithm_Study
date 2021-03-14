# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target: int):
        answer = []
        combs = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer = [i, j]

        return answer


if __name__ == "__main__":
    sol = Solution()
    sol.twoSum([2, 7, 11, 15], 9)

