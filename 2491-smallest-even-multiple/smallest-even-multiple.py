class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        mul=1
        while True:
            mul=n*i
            if mul%2==0 and mul % n==0:
                return mul
            i=i+1
            
