class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wl=s.split()
        n=len(wl)
        return len(wl[n-1])    
        