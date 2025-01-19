class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lst=[]
        for i in s:
            count=s.count(i)
            lst.append(count)
        i=0
        check=lst[0]
        for i in lst:
            if check!=i:
                return False
        return True


            
        