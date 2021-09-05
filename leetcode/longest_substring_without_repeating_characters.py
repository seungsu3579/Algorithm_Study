class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	
    	check_list = list()
    	tmp_dict = dict()
    	ranks = dict()
    	for cursor in range(len(s)):
    		
    		next = []
    		for ss in check_list:
    			
    			if not ss.get(s[cursor], False):
    				# 추가
    				ss["substring"] = ss["substring"] + s[cursor]
    				ss[s[cursor]] = True
    				
    				next.append(ss)
    				
    			else:
    				# 이미 char이 무ㄴ자여ㄹ에 이ㅆ으ㅁ
    				ranks[len(ss["substring"])] = ranks.get(len(ss["substring"]), [])
    				ranks[len(ss["substring"])].append(ss)
    		
    		check_list = next
    			
    		# 시자ㄱ
    		tmp = dict()
    		tmp["substring"] = s[cursor]
    		tmp[s[cursor]] = True
    		
    		check_list.append(tmp)
    	
    	# pop all checklist value for aggregation
    	for ss in check_list:
    		
    		ranks[len(ss["substring"])] = ranks.get(len(ss["substring"]), [])
    		ranks[len(ss["substring"])].append(ss)
    	
    	# find max length
    	
    	return_value = 0 if len(ranks.keys()) == 0 else max(list(ranks.keys()))

    	return return_value

if __name__ == "__main__":
	
	s = Solution()
	inputs = ["bbbbb", "abcabcbb", "pwwkew"]
	for input in inputs:
		v = s.lengthOfLongestSubstring(input)
		print(f"input : {input}.  output : {v}")
		
