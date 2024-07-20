class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s_dct={}
            t_dct={}
            for char in s:
                s_dct[char]=s_dct.get(char,0)+1
            for char in t:
                t_dct[char]=t_dct.get(char,0)+1
            for ele in s_dct:
                if s_dct.get(ele)!=t_dct.get(ele):
                    return False
                    break
            return True
            
            
        else:
            return False

        