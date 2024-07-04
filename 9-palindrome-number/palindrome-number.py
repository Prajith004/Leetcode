class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1=str(x)
        str1=str1[::-1]
        temp=str(x)
        return str1==temp
            