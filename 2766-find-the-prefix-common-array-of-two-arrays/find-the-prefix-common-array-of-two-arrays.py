class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        n=len(A)
        

        for i in range(n):
            count=0
            for ele in A[0:i+1]:
                if ele in B[0:i+1]:
                    count+=1
            c.append(count)

        return c



        