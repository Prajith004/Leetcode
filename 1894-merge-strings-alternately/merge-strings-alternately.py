class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str=''
        n1=len(word1)
        n2=len(word2)
        n=max(n1,n2)
        for i in range(n):
            if i<n1:
                str=str+word1[i]
                
            if i<n2:
                str=str+word2[i]

            
        return str


        