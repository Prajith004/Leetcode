class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        res=[]

        def b_t(o,c):
            if o==c==n:
                res.append("".join(lst))
                return
            if o<n:
                lst.append("(")
                b_t(o+1,c)
                lst.pop()
            if c<o:
                lst.append(")")
                b_t(o,c+1)
                lst.pop()
            
        b_t(0,0)
        return res


        