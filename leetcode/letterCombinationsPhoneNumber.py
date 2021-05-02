# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str):
        mapper = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z']
        }

        comb = []
        for i in range(len(digits)):
            if i == 0:
                comb = mapper[int(digits[i])]
            else:
                tmp = []
                for k in mapper[int(digits[i])]:
                    for c in comb:
                        tmp.append(c + k)
                comb = tmp

        return comb

if __name__ == "__main__":
    s = Solution()
    v = s.letterCombinations("23")
    print(v)