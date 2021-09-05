from typing	import List

class Solution:
	def trap_time_x(self, height: List[int]) -> int:
		trace_dict = dict()
		trace_dict[0] = 0
		prev_h = 0
		answer = 0
		
		for idx, h in enumerate(height):
			
			if prev_h >= h:
				for tmp_h in range(1, h+1):
					trace_dict[tmp_h] = idx
				prev_h = h
				
			else:
				for tmp_h in range(1, h+ 1):
					prev_h_idx = trace_dict.get(tmp_h, idx - 1)
					trace_dict[tmp_h] = idx
					l = idx - prev_h_idx - 1
					answer += l
				
				prev_h = h
		return answer
		
	def trap(self, height: List[int]) -> int:
		pass
		
if __name__ == "__main__":
	
	s = Solution()
	
	v = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
	#k = s.trap([4,2,0,3,2,5])
	
	print(v)
	
#	print(k)


					print("prev_h. ",prev_h, prev_h_idx)
					print("h.      ", h, idx)
					print(f"{tmp_h} | {l}")
					print()

