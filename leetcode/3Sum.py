# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        answer = dict()

        count_num = dict()
        for num in nums:
            count_num[num] = count_num.get(num, 0) + 1
        
        nums = [ [num]*min(3, count) for num, count in count_num.items()]
        pre_nums = []
        for li in nums:
            pre_nums += li
        nums = pre_nums

        dict_nums = dict()
        for i in range(len(nums)):
            dict_nums[nums[i]] = dict_nums.get(nums[i], []) + [i, ]

        for n in range(len(nums)):
            for m in range(n + 1, len(nums)):
                tmp = nums[n] + nums[m]
                target = dict_nums.get(-tmp, [])[:]

                c = 0
                if nums[n] == -tmp:
                    c += 1
                if nums[m] == -tmp:
                    c += 1

                if len(target) - c > 0:
                    answer[tuple(sorted([nums[n], nums[m], -tmp]))] = 1
        
        answer = [list(v) for v in list(answer.keys())]

        return answer

if __name__ == "__main__":
    s = Solution()
    v = s.threeSum([-1,0,1,2,-1,-4])
    print(v)