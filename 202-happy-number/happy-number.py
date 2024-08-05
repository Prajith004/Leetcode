class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen=set()      
        while n!=1 and n not in seen :
            seen.add(n)
            digit=0
            while n>0:
                
                
                rem=n%10
                
                
                digit+=rem*rem
                
                n=n//10
                
            n=digit
            
            
            
            
            
        return n==1
        