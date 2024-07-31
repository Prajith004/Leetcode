class Solution:
    def isPalindrome(self, s: str) -> bool:
        t_s=""
        s=s.lower()
        for ele in s:
            if ele.isalnum():
                t_s+=ele
        return t_s==t_s[::-1]


        