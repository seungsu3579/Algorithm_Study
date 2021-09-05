from typing import List

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		
		 comb_sum_list =  self.recursive_combination_sum(target, [], candidates)
		 
		 tmp = set(comb_sum_list)
		 
		 return list(map(lambda x: list(x), tmp))
	
	def recursive_combination_sum(self, target: int, candidate_list : List[int], candidates: List[int]):
		
		return_list = []
		
		for cd in candidates:
			
			if cd < target:
				v = self.recursive_combination_sum(target - cd, candidate_list + [cd, ], candidates)
				return_list += v
			elif cd == target:
				tmp = candidate_list + [cd, ]
				return_list.append(tuple(sorted(tmp)))
		
		return return_list
		


if __name__ == "__main__":
	s = Solution()
	
	v= s.combinationSum([2,3,5], 8)
	print(v)
