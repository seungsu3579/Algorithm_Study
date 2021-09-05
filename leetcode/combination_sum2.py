from typing import List

class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		
		 comb_sum_list =  self.recursive_combination_sum(target, [], candidates)
		 
		 tmp = set(comb_sum_list)
		 
		 return list(map(lambda x: list(x), tmp))
	
	def recursive_combination_sum(self, target: int, candidate_list : List[int], candidates: List[int]):
		
		return_list = []
		
		# set()으로 서ㄹ저ㅇ하지 아ㄴㅎ으며ㄴ time limit exception에 거ㄹ리ㄴ다. 부ㄹ피ㄹ요하ㄴ 가ㅂㅅ드ㄹ까지 재구ㅣ로 계사ㄴ하기 때무ㄴ이다.
		for cd in set(candidates):
			
			if cd < target:
				tmp = candidates[:]
				tmp.remove(cd)
				if len(tmp) == 0:
					break
				v = self.recursive_combination_sum(target - cd, candidate_list + [cd, ], tmp)
				return_list += v
			elif cd == target:
				tmp = candidate_list + [cd, ]
				return_list.append(tuple(sorted(tmp)))
		
		return return_list
		


if __name__ == "__main__":
	s = Solution()
	v= s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27)
	print(v)
