class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp=num
        rev=0
        while num!=0:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        num=rev
        rev=0
        while num!=0:
            rem=num%10
            rev=rev*10+rem
            num=num//10
        
        return temp==rev
        