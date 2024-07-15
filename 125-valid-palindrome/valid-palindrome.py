class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        str_1=""
        for i in range(len(s)):
            if s[i].isalnum():
                str_1+=s[i]

        str_1=str_1.lower()
        return str_1==str_1[::-1]

        