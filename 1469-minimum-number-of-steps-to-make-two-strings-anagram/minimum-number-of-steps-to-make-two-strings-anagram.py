class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        
        if len(s) <= 5 * (10 ** 4) and len(s) == len(t):
            n = len(s)
            check_a = 0
            s = s.lower()
            t = t.lower()
            
            
            count_s = {}
            count_t = {}
            
            for char in s:
                count_s[char] = count_s.get(char, 0) + 1
                
            for char in t:
                count_t[char] = count_t.get(char, 0) + 1
            
            
            for char in count_s:
                if count_s[char] > count_t.get(char, 0):
                    count += count_s[char] - count_t.get(char, 0)
            
            return count
        
        return 0
