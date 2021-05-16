# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list, val: int):

        answer = []
        n = 0
        while n < len(nums):
            if nums[n] == val:
                nums.pop(n)
            else:
                n += 1
        
        return len(nums)

if __name__ == "__main__":

    s = Solution()

    print(s.removeElement([3, 2, 2, 3], 3))