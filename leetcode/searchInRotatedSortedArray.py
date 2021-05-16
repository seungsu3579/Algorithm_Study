# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list, target: int):

        start = 0
        end = len(nums) - 1

        # find max
        max_v, max_idx = self.find_max_binary(nums, start, end, int((start + end)/2))

        tmp_idx = self.binary_search(nums, start, end, target, max_idx + 1)

        if tmp_idx == -1:
            return -1

        return (tmp_idx + max_idx + 1) % len(nums)


    def binary_search(self, nums, start, end, target, max_idx):

        while(start <= end):
            mid = int((start + end) / 2)

            if nums[(mid + max_idx) % len(nums)] == target:
                return mid

            if nums[(mid + max_idx) % len(nums)] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1


    def find_max_binary(self, nums, start, end, mid):

        if start == mid or mid == end:
            if nums[start] > nums[end]:
                return (nums[start], start)
            else:
                return (nums[end], end)

        elif nums[start] < nums[mid] and nums[mid] < nums[end]:
            return (nums[end], end)

        elif nums[end] < nums[start] and nums[start] < nums[mid]:
            tmp = int((mid + end)/2)
            return self.find_max_binary(nums, mid, end, tmp)

        elif nums[mid] < nums[end] and nums[end] < nums[start]:
            tmp = int((mid + start)/2)
            return self.find_max_binary(nums, start, mid, tmp)
        

if __name__ == "__main__":
    s = Solution()

    nums = [1, 3, 5]
    start = 0
    end = len(nums) - 1
    mid = int((start + end)/2)
    print(s.search(nums, 0))