class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        for ele in tokens:
            if ele=="+":
                lst.append(lst.pop()+lst.pop())
            elif ele=="-":
                
                num1=lst.pop()
                num2=lst.pop()
                lst.append(int(num2-num1))
            elif ele=="*":
                lst.append(lst.pop()*lst.pop())
            elif ele=="/":
                num1=lst.pop()
                num2=lst.pop()
                lst.append(int(num2/num1))
            else:
                lst.append(int(ele))
        return int(lst.pop())
        