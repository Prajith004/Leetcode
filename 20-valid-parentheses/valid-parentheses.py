class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]

        for ele in s:
            if ele=='{' or ele=='(' or ele=="[":
                lst.append(ele)
                print(ele)
            if ele=='}':
                print(ele)
                if  len(s)>1 and len(lst)>=1 :
                    if lst[len(lst)-1]=='{':
                        lst.pop(len(lst)-1)
                    else:
                        return False
                else:
                    return False



            if ele==')':
                print(ele)
                if  len(s)>1 and len(lst)>=1 :
                    if lst[len(lst)-1]=='(':
                        lst.pop(len(lst)-1)
                    else:
                        return False
                else:
                    return False
                    
                
           

            if ele==']':
                print(ele)
                if  len(s)>1 and len(lst)>=1 :
                    if lst[len(lst)-1]=='[':
                        lst.pop(len(lst)-1)
                    else:
                        return False
                else:
                    return False


        return lst==[]