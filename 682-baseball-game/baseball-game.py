class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        
        for ele in operations:
            if ele.lstrip('-').isdigit():
                lst.append(int(ele))
            elif ele=="+":
                sum_p=(lst[-1])+(lst[-2])
                lst.append(sum_p)
            elif ele=='D':
                mul=2*(lst[-1])
                lst.append(mul)
            elif ele=='C':
                lst.pop()
                
            
        return sum(lst)
            
        