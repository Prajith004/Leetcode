class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        str_age=""
        for ele in details:
            str_age=ele[11]+ele[12]
            str_int=int(str_age)
            if str_int>60:
                count+=1
        return count



        