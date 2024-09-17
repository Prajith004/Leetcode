class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        str_1 = ""
        
        for ele in s:
            if ele not in str_1:
                str_1 += ele
            else:
                lst.append(str_1)  
                
                str_1 = str_1[str_1.index(ele) + 1:] + ele
        
        
        lst.append(str_1)
        
       
        if lst:
            return len(max(lst, key=len))
        else:
            return 0
